# Data Tables used by the workflows

I created three Data Tables in n8n. The workflow JSON files contain the node mappings but **do not create the tables or include their rows**. Anyone importing this project will need to create the tables below and select them in the relevant Data Table nodes.

## `contract_test_results` (Workflow 2)

| Column | Type | Purpose |
|---|---|---|
| `scenario` | String | Test scenario (`http_error` or `auth_missing` for some non-200 responses) |
| `verdict` | String | PASS / WARN / FAIL / ERROR |
| `http_status` | Number | Last HTTP response status |
| `records_checked` | Number | Records checked |
| `errors` | String | JSON text containing the error list |
| `warnings` | String | JSON text containing the warning list |
| `tested_at` | Date | Time of check |

## `release_decision_audit` (Workflow 3)

| Column | Type |
|---|---|
| `release_id` | String |
| `connector_id` | String |
| `scenario` | String |
| `requested_by` | String |
| `contract_verdict` | String |
| `http_status` | Number |
| `final_decision` | String |
| `reviewer_name` | String |
| `reviewer_decision` | String |
| `reviewer_comments` | String |
| `final_reason` | String |
| `finalised_at` | Date |

## `workflow_error_audit` (Workflow 4)

| Column | Type |
|---|---|
| `workflow_name` | String |
| `workflow_id` | String |
| `execution_id` | String |
| `failed_node` | String |
| `error_message` | String |
| `execution_url` | String |
| `error_type` | String |
| `occurred_at` | Date |

The table names and field names must match the expressions in the workflows. After importing, choose each new table in its Data Table node and check the column mappings. The `RESELECT_TABLE_IN_N8N` values are intentional placeholders, not IDs that will work as-is.
