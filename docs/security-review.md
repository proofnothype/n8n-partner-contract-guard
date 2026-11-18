# Configuration and security notes

I exported four workflows from my n8n Cloud workspace and prepared separate copies for this public repository. The working versions in n8n were not changed by this cleanup.

## What I removed from the public copies

| In the original export | In these files |
|---|---|
| My n8n Cloud hostname | `https://YOUR_N8N_HOST/webhook/partner-alpha/customers` |
| Credential names and internal credential IDs | Removed; add a new Header Auth credential after import |
| Workflow, version and instance IDs | Removed |
| Internal node IDs and webhook resume IDs | Replaced or removed |
| Workflow 3's reference to Workflow 2 | Placeholder; select Workflow 2 after import |
| Data Table IDs and cached paths | Placeholder; select each table after import |
| Workflow 1's error-workflow reference | Removed; select Workflow 4 after import |
| Personal name in the reviewer placeholder | Replaced with neutral placeholder text |

I also fixed a few export-only configuration artifacts: two query parameter names, a stray tab in the warnings mapping and an unused IF-node setting. These adjustments are in the **shared copies** only, not the original running workflows.

## Credentials

The workflow exports contained credential references, not the stored API-key value. I did not find an obvious plaintext API key or password in the exported node configuration. This does not amount to an audit of the n8n credential store.

Use a new test credential for an imported copy. Do not publish credentials, screenshots of authentication headers, or original workflow exports.

## What this does not protect against

- **Approval identity:** a reviewer types a name. There is no sign-in requirement or check that the reviewer is authorised.
- **Duplicate requests:** an existing `release_id` can be processed and logged again.
- **Unknown connectors:** `connector_id` is passed through for reporting, not checked against an approved list.
- **Retry limits:** HTTP 429 and 503 have up to three attempts and two-second waits; there is no `Retry-After` handling, exponential backoff or explicit tested timeout policy.
- **Error coverage:** Workflow 4 was configured as Workflow 1's error workflow. Workflows 2 and 3 are not covered by that link in the original exports.
- **Auditing and retention:** the tables record outcomes, but retention rules, access policies and alert routing have not been designed.
- **Reproducibility:** importing the files needs credential, Data Table and workflow-reference setup. I have not claimed that a clean import runs without configuration.

The special `rate_429_once` case uses a client-provided attempt number. That makes the test predictable, but it is not how I would implement a real partner rate limit.

## Checks on the shared files

I verified that the four JSON files parse, that graph connections reference existing nodes, and that the original hostname and selected private identifiers are absent. The included `tools/validate_exports.py` script repeats a set of these checks offline. It does not execute the workflows.

Before adding screenshots to GitHub, I will also check for real workspace URLs, execution IDs, user details, cookies, approval form URLs and tokens. The original exports should not be uploaded publicly.
