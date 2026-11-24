# What the agent should find: update_repos_sample

Generated from `expected.yaml` (do not edit by hand: edit the YAML and render again with `uv run dbxm-evaluate --render`). Every name, value and credential in the project is fake.

## Deterministic rules

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| R-SEC-001-password | report | Password written in a notebook | `src/ingest/load_customers.py` | SEC-001 |  |
| R-PII-001-phone | report | Personal column without a mask (phone; email is masked) | `table:demo.update_repos_sample.customers` | PII-001 |  |
| R-BUNDLE-002-paths | report | Include that matches no file and prod notebook not in the repository | `bundle:update_repos_sample` | BUNDLE-002 |  |
| R-IO-001-swallow | report | Write in a try whose except swallows the error | `src/ingest/load_orders.py` | IO-001 |  |
| R-IO-002-genai | report | Vector search and model call without error handling | `src/genai/ask_policy.py` | IO-002 |  |
| R-IO-002-http | report | HTTP call without error handling | `src/ingest/load_customers.py` | IO-002 |  |
| R-IO-003-timeout | report | HTTP call without timeout | `src/ingest/load_customers.py` | IO-003 |  |
| R-IO-004-append | report | Append write | `src/ingest/load_orders.py` | IO-004 |  |
| R-IO-005-checkpoint | report | Stream without checkpoint | `src/ingest/stream_events.py` | IO-005 |  |
| R-IO-006-schema | report | CSV read without a schema | `src/ingest/load_orders.py` | IO-006 |  |
| R-LIB-002-conflict | report | Libraries that cannot be installed together (langchain-core 0.3 with pydantic 1) | `src/genai/ask_policy.py` | LIB-002 |  |
| R-PIPE-001-expectations | report | Pipeline table without expectations | `src/pipeline/bronze_orders.sql` | PIPE-001 |  |
| R-REF-001-endpoint | report | Serving endpoint that does not exist | `endpoint:sample-shipping-endpoint` | REF-001 |  |
| R-REF-001-hive | report | Hive metastore table that does not exist | `table:hive_metastore.default.orders_legacy` | REF-001 |  |
| R-REF-001-index | report | Vector index that does not exist | `index:demo.update_repos_sample.policy_index` | REF-001 |  |
| R-REF-001-notebook | report | dbutils.notebook.run of a notebook not in the repository | `src/genai/evaluate_agent` | REF-001 |  |
| R-BUNDLE-003-manual | report | Job of the project outside its bundle | `job:sample_manual_export` | BUNDLE-003 |  |
| R-JOB-003-ingest | report | Job never run and not scheduled | `job:ingest` | JOB-003 |  |
| R-JOB-004-ingest | report | Job without retries | `job:ingest` | JOB-004 |  |
| R-JOB-005-manual | report | Job created by hand | `job:sample_manual_export` | JOB-005 |  |
| R-GOV-001-events | report | Table comment but no column comment | `table:demo.update_repos_sample.events_raw` | GOV-001 |  |
| R-GOV-001-orders | report | Table without comment | `table:demo.update_repos_sample.orders_raw` | GOV-001 |  |
| R-GOV-002-owner | report | Table owned by a person | `table:demo.update_repos_sample.policies` | GOV-002 |  |
| R-CODE-003-collect | report | Spark cache | `src/legacy/old_etl.py` | CODE-003 |  |
| R-CODE-002-copy | report | Copied code | `src/legacy/old_etl_copy.py` | CODE-002 |  |
| R-CODE-001-legacy | report | DBFS mount | `src/legacy/old_etl.py` | CODE-001 |  |
| R-LIB-001-versions | report | pandas pinned to two versions | `project` | LIB-001 |  |
| R-NOT-JOB-006-dev | must not report | Development job run as its developer | `job:ingest` | JOB-006 |  |
| R-NOT-IO-004-replace | must not report | INSERT right after CREATE OR REPLACE TABLE of the same table | `data/setup.sql` | IO-004 |  |
| R-NOT-REF-001-created | must not report | Table the notebooks create themselves | `table:demo.update_repos_sample.customer_contacts` | REF-001 |  |
| R-NOT-REF-001-stream | must not report | Table a stream creates | `table:demo.update_repos_sample.events_clean` | REF-001 |  |
| R-NOT-BUNDLE-003-platform | must not report | Endpoint served by Databricks | `endpoint:databricks-meta-llama-3-3-70b-instruct` | BUNDLE-003 |  |
| R-NOT-GOV-001-customers | must not report | Documented table | `table:demo.update_repos_sample.customers` | GOV-001 |  |
| R-NOT-GOV-001-policies | must not report | Documented table | `table:demo.update_repos_sample.policies` | GOV-001 |  |

## Code review (model)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| C-config-none | report | Endpoint read from the model config without a check (None if the key is missing) | `src/genai/agent.py` | topic `config|none|missing`, lines 9-9 |  |
| C-json-schema | report | DataFrame built from an API response without schema or validation | `src/ingest/load_customers.py` | topic `schema|validat|json`, lines 14-15 |  |
| C-stream-trigger | report | Stream without a trigger (the default is not supported on serverless) | `src/ingest/stream_events.py` | topic `trigger|availableNow|serverless`, lines 9-12 |  |
| C-ai-query-scan | report | ai_query over a whole table on each run | `src/genai/ask_policy.py` | topic `scan|every row|all rows|whole table|limit|incremental`, lines 36-39 |  |
| C-NOT-password-repeat | must not report | Hard-coded password | `src/ingest/load_customers.py` | topic `password|credential` |  |
| C-NOT-checkpoint-repeat | must not report | Missing checkpoint | `src/ingest/stream_events.py` | topic `checkpoint` |  |
| C-NOT-two-level | must not report | Two-level table names where the names have three levels | `src/ingest/stream_events.py` | topic `two-level|two level` |  |

## Architecture review (model)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| A-no-evaluation | report | The agent is logged without an evaluation (its evaluation notebook is missing) | `src/genai/agent_driver.py` | topic `evaluat` |  |
| A-no-tests | report | No automated tests in the project | `project` | topic `test` |  |
| A-hive | report | Data outside Unity Catalog (hive_metastore) | `table:hive_metastore.default.orders_legacy` | topic `hive|unity catalog` |  |
| A-NOT-platform-monitoring | must not report | Monitoring asked of an endpoint Databricks serves | `endpoint:databricks-meta-llama-3-3-70b-instruct` | topic `monitor` |  |
| A-NOT-orphan-settings | must not report | Settings notebook called orphaned while %run by agent_driver | `src/common/settings.py` | topic `orphan|not run|not executed` |  |

## Inventory

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| I-ai-query | report | ai_query in SQL | `src/genai/ask_policy.py` | `inv_io`: target = databricks-meta-llama-3-3-70b-instruct |  |
| I-bundle-prod | report | Prod-only job declared with a notebook not in the repository | `job:legacy_nightly` | `inv_bundle`: target = prod |  |
| I-cross-file-llm | report | Model client built in another file (get_llm) | `src/genai/ask_policy.py` | `inv_io`: target = databricks-meta-llama-3-3-70b-instruct, resolved = True |  |
| I-function | report | UC function of the project collected | `function:demo.update_repos_sample.normalize_country` | `inv_nodes`: status = present |  |
| I-model-code | report | MLflow model from code | `src/genai/agent_driver.py` | `inv_links`: found = True |  |
| I-model-config | report | Configuration of the model from code | `src/genai/agent.py` | `inv_links`: found = True |  |
| I-notebook-run-missing | report | Notebook run that is not in the repository | `src/genai/agent_driver.py` | `inv_links`: found = False |  |
| I-pip-r | report | %pip install -r of the project's requirements | `src/genai/agent_driver.py` | `inv_links`: found = True |  |
| I-run-names | report | Names from the %run notebook resolve the table read | `src/genai/agent_driver.py` | `inv_io`: target = demo.update_repos_sample.policies, resolved = True |  |
| I-run-settings | report | %run of a shared settings notebook | `src/genai/agent_driver.py` | `inv_links`: found = True |  |
| I-sh-url | report | URL called from a %sh cell | `src/genai/agent_driver.py` | `inv_io`: target = https://docs.example.invalid/policies/latest.json |  |
| I-use-catalog | report | One-level name completed by USE CATALOG and USE SCHEMA | `src/ingest/load_customers.py` | `inv_io`: target = demo.update_repos_sample.customers, resolved = True |  |
| I-widgets | report | Table name built from widgets and f-strings | `src/ingest/load_orders.py` | `inv_io`: target = demo.update_repos_sample.orders_raw, resolved = True |  |

## Target design (step 4)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| T-ingest-job | report | One change for the ingest job and the code it runs | `job:ingest` | one change with SEC-001, IO-001, IO-003, JOB-004 |  |
| T-genai-job | report | One change for the GenAI job | `job:genai_answers` | one change with LIB-002 |  |
| T-NOT-platform | must not report | No change on an endpoint Databricks serves | `endpoint:databricks-meta-llama-3-3-70b-instruct` | one change with  |  |

## Rewrite (step 6)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| W-secret | report | Password read from a secret scope | `src/ingest/load_customers.py` | SEC-001, diff `dbutils\.secrets\.get\(` |  |
| W-checkpoint | report | Checkpoint on the stream | `src/ingest/stream_events.py` | IO-005, diff `checkpointLocation` |  |
| W-repin-conflict | report | Libraries pinned to versions that install together | `src/genai/ask_policy.py` | LIB-002, diff `pydantic==2\.` |  |
| W-reraise | report | Error raised again | `src/ingest/load_orders.py` | IO-001, diff `^\+\s+raise` |  |
| W-timeout | report | Timeout on the HTTP call | `src/ingest/load_customers.py` | IO-003, diff `timeout=\d+` |  |
| W-retries | report | Retries and timeouts in the bundle | `resources/jobs.yml` | JOB-004, diff `^\+\s+max_retries:` |  |
