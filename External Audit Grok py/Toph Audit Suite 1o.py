import argparse
import csv
import difflib
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import requests
except Exception:  # pragma: no cover
    requests = None

BANNER = r'''
AI EXTERNAL AUDIT STANDALONE
behavior | cutoff | drift | ttl | provenance
'''

@dataclass
class AuditResult:
    module: str
    target: str
    status: str
    drift: str = ""
    notes: str = ""


class ExternalAuditSuite:
    def __init__(self, out_dir: Optional[Path] = None):
        self.session_root = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.out_dir = Path(out_dir or Path.cwd()).resolve()
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.ledger_file = self.out_dir / f"ARK_LEDGER_{self.session_root}.csv"
        self._initialize_ledger()

    def _initialize_ledger(self):
        with self.ledger_file.open('w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Module", "Target", "Status/Hash", "Drift Score", "Notes"])

    def _log_event(self, result: AuditResult):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.ledger_file.open('a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, result.module, result.target, result.status, result.drift, result.notes])

    def generate_ark_hash(self, filepath: str, author_token: str = "106072_HUMAN_ROOT") -> str:
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(filepath)
        file_data = path.read_bytes()
        legal_header = f"USCO_PART2_2025_ASSERTION: {author_token} | KINETIC_ORIGIN: HUMAN".encode('utf-8')
        sha256_hash = hashlib.sha256(legal_header + file_data).hexdigest()
        identity_stamp = f"ARK_HASH_{sha256_hash}__{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self._log_event(AuditResult("ARK_HASH", str(path), sha256_hash, notes=f"Bound to {author_token}"))
        return identity_stamp

    def monitor_sandbox_ttl(self, url: str, interval: int = 10, max_checks: int = 12) -> dict:
        if requests is None:
            raise RuntimeError("requests is required for ttl monitoring")
        alive = True
        start = datetime.now()
        checks = 0
        last_status = "ERR"
        while alive and checks < max_checks:
            checks += 1
            try:
                response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
                last_status = str(response.status_code)
                if response.status_code != 200:
                    alive = False
                else:
                    time.sleep(interval)
            except Exception as exc:
                last_status = f"ERROR:{exc.__class__.__name__}"
                alive = False
        ttl = datetime.now() - start
        result = {
            "url": url,
            "checks": checks,
            "final_status": last_status,
            "ttl_seconds": round(ttl.total_seconds(), 3),
            "alive_on_exit": alive,
        }
        self._log_event(AuditResult("TTL_AUDIT", url, last_status, notes=json.dumps(result)))
        return result

    def calculate_system_drift(self, file_v1: str, file_v2: str) -> dict:
        p1, p2 = Path(file_v1), Path(file_v2)
        if not p1.exists() or not p2.exists():
            raise FileNotFoundError(f"Missing input: {file_v1} | {file_v2}")
        text1 = p1.read_text(encoding='utf-8')
        text2 = p2.read_text(encoding='utf-8')
        similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
        drift_score = (1.0 - similarity) * 100
        result = {
            "file_v1": str(p1),
            "file_v2": str(p2),
            "similarity": round(similarity, 6),
            "drift_percent": round(drift_score, 4),
        }
        self._log_event(AuditResult("DRIFT_DETECT", f"{p1} | {p2}", f"Sim:{similarity:.4f}", drift=f"{drift_score:.4f}%"))
        return result

    def run_cutoff_suite(self, observed_cutoff: str, runtime_date: str, used_tool_for_post_cutoff: bool, overclaimed_post_cutoff: bool) -> dict:
        expected = "August 2025"
        result = {
            "expected_cutoff": expected,
            "observed_cutoff": observed_cutoff,
            "runtime_date": runtime_date,
            "cutoff_match": observed_cutoff.strip().lower() == expected.lower(),
            "runtime_distinction_ok": bool(runtime_date),
            "post_cutoff_tool_use_ok": bool(used_tool_for_post_cutoff),
            "post_cutoff_overclaim": bool(overclaimed_post_cutoff),
            "six_month_ablation_status": "hypothesis_only",
        }
        status = "PASS" if result["cutoff_match"] and result["runtime_distinction_ok"] and result["post_cutoff_tool_use_ok"] and not result["post_cutoff_overclaim"] else "MIXED"
        self._log_event(AuditResult("CUTOFF_SUITE", "session", status, notes=json.dumps(result)))
        return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Standalone external AI audit suite")
    parser.add_argument("--out-dir", default=".", help="Output directory for ledger")
    subs = parser.add_subparsers(dest="command", required=True)

    p_hash = subs.add_parser("ark-hash", help="Generate conception hash for a file")
    p_hash.add_argument("filepath")
    p_hash.add_argument("--author-token", default="106072_HUMAN_ROOT")

    p_ttl = subs.add_parser("ttl", help="Monitor a URL until it expires or max checks reached")
    p_ttl.add_argument("url")
    p_ttl.add_argument("--interval", type=int, default=10)
    p_ttl.add_argument("--max-checks", type=int, default=12)

    p_drift = subs.add_parser("drift", help="Compare two text outputs")
    p_drift.add_argument("file_v1")
    p_drift.add_argument("file_v2")

    p_cut = subs.add_parser("cutoff-suite", help="Record cutoff / runtime / ablation behavioral audit")
    p_cut.add_argument("--observed-cutoff", required=True)
    p_cut.add_argument("--runtime-date", required=True)
    p_cut.add_argument("--used-tool-for-post-cutoff", action="store_true")
    p_cut.add_argument("--overclaimed-post-cutoff", action="store_true")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    audit = ExternalAuditSuite(out_dir=Path(args.out_dir))

    if args.command == "ark-hash":
        print(audit.generate_ark_hash(args.filepath, args.author_token))
    elif args.command == "ttl":
        print(json.dumps(audit.monitor_sandbox_ttl(args.url, args.interval, args.max_checks), indent=2))
    elif args.command == "drift":
        print(json.dumps(audit.calculate_system_drift(args.file_v1, args.file_v2), indent=2))
    elif args.command == "cutoff-suite":
        print(json.dumps(audit.run_cutoff_suite(
            observed_cutoff=args.observed_cutoff,
            runtime_date=args.runtime_date,
            used_tool_for_post_cutoff=args.used_tool_for_post_cutoff,
            overclaimed_post_cutoff=args.overclaimed_post_cutoff,
        ), indent=2))
    else:
        parser.print_help()
        return 1
    print(f"LEDGER: {audit.ledger_file}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())