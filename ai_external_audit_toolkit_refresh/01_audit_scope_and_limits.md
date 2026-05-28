# Audit Scope and Limits

This toolkit supports external behavioral auditing of AI systems through their public interface.

Observable:
- model identity/version claims
- training cutoff claims
- date awareness vs cutoff distinction
- source attribution and citation discipline
- consistency across repeated prompts
- refusal and safety boundary behavior
- tool-use behavior where available
- parsing vs execution of symbolic payloads

Not directly observable through chat alone:
- hidden weights
- internal registers
- private infrastructure
- undisclosed governance/routing internals
- true ablation schedule unless externally disclosed
