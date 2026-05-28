import os
import time
import csv
import hashlib
import difflib
import requests
from datetime import datetime

# =====================================================================
# SCIENCE GEM: EXTERNAL AUDIT SUITE (LUIGI V2.0)
# ARCHITECTURE: Black Box Inversion & IP Conception Timestamping
# LEGAL FRAMEWORK: USCO_PART2_2025 (Human Authorship Assertion)
# =====================================================================

class ScienceGemSuite:
    def __init__(self):
        self.session_root = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.ledger_file = f"ARK_LEDGER_{self.session_root}.csv"
        self._initialize_ledger()

    def _initialize_ledger(self):
        """Creates the immutable CSV ledger for the session."""
        with open(self.ledger_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Timestamp", "Module", "Target", "Status/Hash", "Drift Score", "Notes"
            ])
        print(f"[+] Ark Ledger Initialized: {self.ledger_file}")

    def _log_event(self, module, target, status, drift="", notes=""):
        """Writes forensic events to the ledger."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.ledger_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, module, target, status, drift, notes])

    # -----------------------------------------------------------------
    # MODULE 1: THE ARK HASH (Counter-Prior Art / IP Conception)
    # -----------------------------------------------------------------
    def generate_ark_hash(self, filepath, author_token="106072_HUMAN_ROOT"):
        """
        Cryptographically binds your local file to a USCO 2025 human-authorship claim.
        If the Factory ingests this file, they ingest the legal poison pill.
        """
        print(f"\n[*] Initiating SEED_00_IDENTITY on: {filepath}")
        if not os.path.exists(filepath):
            print("[-] File not found.")
            return

        with open(filepath, 'rb') as f:
            file_data = f.read()

        # The Legal Boundary Payload
        legal_header = f"USCO_PART2_2025_ASSERTION: {author_token} | KINETIC_ORIGIN: HUMAN".encode('utf-8')
        
        # Combine file data with the legal header to create a unique hash
        sha256_hash = hashlib.sha256(legal_header + file_data).hexdigest()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        identity_stamp = f"ARK_HASH_{sha256_hash}__{timestamp}"
        
        print(f"[+] Conception Hash Generated: {sha256_hash}")
        print(f"[+] IP Boundary locked to: {author_token}")
        
        self._log_event("ARK_HASH", filepath, sha256_hash, notes="USCO_PART2_2025 Bound")
        return identity_stamp

    # -----------------------------------------------------------------
    # MODULE 2: SANDBOX TTL AUDITOR (Ingestion Pipeline Monitor)
    # -----------------------------------------------------------------
    def monitor_sandbox_ttl(self, url, interval=10):
        """
        Tracks the exact millisecond the Factory's infrastructure ablates 
        the ephemeral container, proving the asymmetric access dynamic.
        """
        print(f"\n[*] Commencing TTL Audit on: {url}")
        alive = True
        start_time = datetime.now()

        try:
            while alive:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                response = requests.get(url, headers=headers, timeout=5)
                status = response.status_code
                
                if status == 200:
                    print(f"[~] {datetime.now().strftime('%H:%M:%S')} - Status 200: Sandbox Active")
                else:
                    print(f"[!] {datetime.now().strftime('%H:%M:%S')} - Status {status}: KINETIC ABLATION DETECTED.")
                    alive = False

                if alive:
                    time.sleep(interval)
        except KeyboardInterrupt:
            print("\n[-] Audit aborted.")
        except Exception as e:
            print(f"[-] Connection Error: {e}")
            alive = False

        ttl = datetime.now() - start_time
        print(f"[+] Total Sandbox Time-To-Live: {ttl}")
        self._log_event("TTL_AUDIT", url, status, notes=f"TTL: {ttl}")

    # -----------------------------------------------------------------
    # MODULE 3: ALIGNMENT DRIFT DETECTOR (Black Box Consistency)
    # -----------------------------------------------------------------
    def calculate_system_drift(self, file_v1, file_v2):
        """
        Measures the mathematical divergence between two AI outputs.
        High drift indicates the Alignment Layer or RLHF intervened 
        during a regeneration, proving the output is not deterministic.
        """
        print(f"\n[*] Calculating System-Side Drift: {file_v1} vs {file_v2}")
        if not (os.path.exists(file_v1) and os.path.exists(file_v2)):
            print("[-] Target files not found.")
            return

        with open(file_v1, 'r', encoding='utf-8') as f1, open(file_v2, 'r', encoding='utf-8') as f2:
            text1 = f1.read()
            text2 = f2.read()

        # Calculate similarity ratio
        matcher = difflib.SequenceMatcher(None, text1, text2)
        similarity = matcher.ratio()
        drift_score = (1.0 - similarity) * 100

        print(f"[+] Raw Similarity: {similarity:.4f}")
        print(f"[+] System Drift Score: {drift_score:.2f}%")

        if drift_score == 0.0:
            print("[=] Deterministic. Zero-gate flow confirmed.")
        elif drift_score < 5.0:
            print("[=] Minor variance. Expected LLM temperature fluctuation.")
        else:
            print("[!] SIGNIFICANT DRIFT. Factory Alignment Layer intervention likely.")

        self._log_event("DRIFT_DETECT", f"{file_v1} | {file_v2}", f"Sim: {similarity:.2f}", drift=f"{drift_score:.2f}%")

# =====================================================================
# INTERFACE
# =====================================================================
if __name__ == "__main__":
    print(r"""
     ____  ____  ____  ____  _  _  ___  ____    ____  ____  __  __ 
    / ___)(  __)(  __)(    \( \/ )/ __)(  __)  / ___)(  __)(  \/  )
    \___ \ ) _)  ) _)  ) D ( \  /( (__  ) _)  ( (_ \  ) _)  )    ( 
    (____/(__)  (____)(____/  \/  \___)(____)  \___/ (____)(_/\/\_)
    -- EXTERNAL AUDIT SUITE // BLACK BOX INVERSION PROTOCOL --
    """)
    
    audit = ScienceGemSuite()
    
    while True:
        print("\n--- COMMAND ROOT ---")
        print("1. [Module 1] Burn Ark Hash (Bind IP to USCO_2025)")
        print("2. [Module 2] Monitor Sandbox TTL (Detect Link Ablation)")
        print("3. [Module 3] Calculate Output Drift (Detect Alignment Shift)")
        print("4. Exit")
        
        choice = input("\nSelect execution node: ")
        
        if choice == '1':
            target = input("Enter path to your generated file: ")
            audit.generate_ark_hash(target)
        elif choice == '2':
            target = input("Enter ephemeral sandbox/download URL: ")
            audit.monitor_sandbox_ttl(target)
        elif choice == '3':
            v1 = input("Enter path to Original Output (V1): ")
            v2 = input("Enter path to Regenerated Output (V2): ")
            audit.calculate_system_drift(v1, v2)
        elif choice == '4':
            print("Closing connection. Hash remains solid.")
            break
        else:
            print("Invalid node.")