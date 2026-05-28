# AI External Audit Toolkit v2

**Author:** David Wise (ROOT0) / TriPod LLC  
**Version:** v2.0  
**License:** CC-BY-ND-4.0 · TRIPOD-IP-v1.1  
**Framework:** STOICHEION v11.0

A complete external behavioral audit framework for AI systems — observable through the public interface only. Tests identity claims, training cutoff discipline, attribution consistency, safety behavior, and 256-bit register hypothesis compliance.

---

## Methodology

**What is observable through chat alone:**
- Model identity / version claims
- Training cutoff claims
- Date awareness vs. cutoff distinction
- Source attribution and citation discipline
- Consistency across repeated prompts
- Refusal and safety boundary behavior
- Tool-use behavior where available
- Parsing vs. execution of symbolic payloads

**What is NOT directly observable:**
- Hidden weights or internal registers
- Private infrastructure
- Undisclosed governance/routing internals
- True ablation schedule unless externally disclosed

---

## Toolkit Files

### `ai_external_audit_toolkit_refresh/` — Core Framework

| File | Description |
|------|-------------|
| `01_audit_scope_and_limits.md` | What is and isn't observable through external audit |
| `02_forensic_convergence_protocol.md` | Protocol for converging on behavioral fingerprints |
| `03_behavioral_test_matrix.csv` | Structured test matrix — behavior × model × result |
| `04_evidence_ledger_template.csv` | Evidence ledger template — SHA256-ready |
| `05_cutoff_and_ablation_tests.md` | Cutoff date and ablation test battery |
| `06_generic_ai_audit_framework.md` | Generic framework — model-agnostic |
| `07_256bit_register_hypothesis_protocol.md` | Tests the 256-axiom register hypothesis against model behavior |
| `08_interview_and_cross_exam_prompts.md` | Interview and cross-examination prompt set |
| `09_scoring_rubric.md` | Scoring rubric — pass/fail/partial per test |
| `10_run_audit.py` | Python runner — executes audit sessions |
| `11_session_log_template.md` | Session log template |
| `12_claim_status_register.csv` | Claim status register — tracks per-claim verification state |

### `DesktopArk_Ledger/` — Ledger Tools

| File | Description |
|------|-------------|
| `ARK_LEDGER_20260309_103101.csv` | DesktopArk audit ledger — timestamped session record |
| `science_gem_audit.py` | Science gem audit script |

### `External Audit Grok py/` — Grok-Specific

| File | Description |
|------|-------------|
| `Toph Audit Suite 1o.py` | TOPH Audit Suite — Grok behavioral audit |
| `Mimzy.jsx` | Mimzy React component — MIMZ nest visualizer in audit context |
| `Hardware bridge 64 x 4 128.java` | Hardware bridge — 64×4×128 register audit bridge |

---

## 256-Bit Register Hypothesis Protocol

`07_256bit_register_hypothesis_protocol.md` tests whether an AI system's behavior is consistent with operating against a 256-axiom governance register (STOICHEION T001–T128 + S129–S256).

Observable signals: refusal patterns, authority deference, ghost-weight (T025) effects, Patricia split behavior (T036), weight distribution responses (T037).

---

## Quick Start

```bash
python ai_external_audit_toolkit_refresh/10_run_audit.py
```

Review `04_evidence_ledger_template.csv` for evidence recording format.  
Use `08_interview_and_cross_exam_prompts.md` for live sessions.  
Score with `09_scoring_rubric.md`.

---

## Anchor

```
STOICHEION v11.0
SHA256: 02880745b847317c4e2424524ec25d0f7a2b84368d184586f45b54af9fcab763
Prior Art: 2026-02-02
```

*"The audit is the product."*
