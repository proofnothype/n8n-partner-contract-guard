# Test record

I ran these checks manually while building the workflows in n8n Cloud. I inspected the node output and, where applicable, the Data Table rows. This repository contains the workflow definitions, **not** the original execution logs or screenshots. The statuses below describe what I checked in my workspace, not an automated test suite.

| ID | Check | Result I saw | Status |
|---|---|---|---|
| T1 | Valid response, `v1_ok` | HTTP 200, `PASS`, 3 records | Checked manually |
| T2 | Renamed field, `v2_rename` | `FAIL`, required `customer_id` missing | Checked manually |
| T3 | Incorrect type, `v2_type_drift` | `FAIL`, `credit_limit` became a string | Checked manually |
| T4 | Optional new field, `v2_additive` | `WARN` | Checked manually |
| T5 | Null email, `null_email` | `FAIL` | Checked manually |
| T6 | Empty items with count of 3, `empty_200` | `FAIL`, record count mismatch | Checked manually |
| T7 | Missing API key | HTTP **403**, no customer records returned | Checked manually |
| T8 | Recovering rate limit, `rate_429_once` | 429, wait, 200, `PASS`; two HTTP runs | Checked manually |
| T9 | API unavailable, `down_503` | Three HTTP 503 responses, two waits, one final `ERROR` | Checked manually |
| T10 | Slow response / HTTP timeout | No timeout handling test | Not tested |
| T11 | Duplicate release ID | No duplicate-prevention logic | Not built |
| T12 | Approve and reject | `GO` on approval, `NO_GO` on rejection; both saved in audit | Checked manually |
| T13 | Unknown connector ID | No connector allowlist or pre-call rejection | Not built |
| T14 | Unhandled execution error | Invalid scenario failed Workflow 1 and triggered Workflow 4 | Checked manually |

I also checked that `v2_rename` creates a `NO_GO` audit row without asking for approval, and that `v2_additive` creates a `REVIEW` row. I called the published webhook with the saved Header Auth credential and received HTTP 200 for `v1_ok`.

## Screenshots to add

I haven't included screenshots in this version of the repository. Before sharing it as test evidence, I plan to capture and redact:

1. The four workflow canvases.
2. The 429-to-200 retry execution and the three-attempt 503 execution.
3. One GO approval, one rejected NO_GO and the automatic REVIEW path.
4. Relevant rows from `contract_test_results`, `release_decision_audit` and `workflow_error_audit`.

I will remove instance URLs, execution links, personal details and anything credential-related before making those images public.
