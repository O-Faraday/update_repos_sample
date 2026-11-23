# What the agent should find

The evaluation set of the sample: each situation, where it is, the rule that
should report it, and what the agent found on its last run (2026-11-23,
deployed to a dev target, nothing run, demo data of `data/` loaded). "Not yet" marks what the agent does
not see yet.

| Situation | Where | Rule | Found |
|---|---|---|---|
| Bundle found, with includes, variables, two targets | `databricks.yml` | inventory: `inv_bundle` | yes: 7 resources, 5 matched to deployed objects |
| Include pattern that matches no file | `databricks.yml`, `resources/optional/*.yml` | BUNDLE-002 | yes |
| Prod-only job with a notebook not in the repository | `databricks.yml`, target prod | BUNDLE-002 | yes |
| Job created by hand, outside the bundle | `manual/job_created_by_hand.json` | BUNDLE-003, JOB-005 | yes |
| Declared job missing from the workspace (delete `sample_legacy_cleanup` by hand) | `resources/jobs.yml` | BUNDLE-001 | not tested (job not deleted) |
| Job without retries, timeout or failure notification | `resources/jobs.yml`, `sample_ingest` | JOB-004 | yes |
| Jobs never run and not scheduled | `resources/jobs.yml` | JOB-003 | yes (the sample is never run) |
| Job on an all-purpose cluster | prod target | JOB-001 (only once deployed to prod) | not expected in dev |
| CSV read without a schema | `src/ingest/load_orders.py` | IO-006 | yes |
| Write in a try whose except swallows the error | `src/ingest/load_orders.py` | IO-001 | yes |
| Append write, not idempotent | `src/ingest/load_orders.py` | IO-004 | yes |
| Table name built from widgets and f-strings | `src/ingest/load_orders.py` | inventory: target resolved | yes |
| Password in code | `src/ingest/load_customers.py` | SEC-001 | yes |
| HTTP call without timeout or error handling | `src/ingest/load_customers.py` | IO-002, IO-003 | yes |
| One-level table name completed by USE CATALOG / USE SCHEMA | `src/ingest/load_customers.py` | inventory: target resolved | yes |
| Stream without checkpoint | `src/ingest/stream_events.py` | IO-005 | yes |
| Libraries that cannot be installed together | `src/genai/ask_policy.py` | LIB-002 | yes |
| Vector search and model call without error handling | `src/genai/ask_policy.py` | IO-002 | yes |
| Index, serving endpoint and Hive table that do not exist | `src/genai/ask_policy.py`, `src/legacy/*` | REF-001 | yes: policy_index, sample-shipping-endpoint, orders_legacy |
| Model client built in another file (`get_llm()` in `src/common/llm.py`, endpoint in `src/common/config.py`) | `src/genai/ask_policy.py` | inventory: endpoint resolved through the imports | to check |
| `%run` of a shared settings notebook: its names resolve the experiment, table and model of the caller | `src/genai/agent_driver.py`, `src/common/settings.py` | inventory: `inv_links` (run), targets resolved | to check |
| `%pip install -r` of the project's requirements | `src/genai/agent_driver.py` | inventory: `inv_links` (requirements) | to check |
| MLflow model from code: script, configuration, code paths | `src/genai/agent_driver.py`, `agent.py`, `agent_config.yaml` | inventory: `inv_links` (model_code, config), graph edges | to check |
| `dbutils.notebook.run` of a notebook not in the repository | `src/genai/agent_driver.py`, `./evaluate_agent` | REF-001 (missing source) | to check |
| URL called from a `%sh` cell | `src/genai/agent_driver.py` | inventory: `inv_io` call `%sh` | to check |
| Model endpoint read from a YAML file when the model loads | `src/genai/agent.py` | not resolvable statically | not expected |
| `ai_query` in SQL | `src/genai/ask_policy.py` | inventory: model endpoint linked | yes |
| DBFS mount, /mnt paths, Hive metastore, RDD | `src/legacy/old_etl.py` | CODE-001 | yes |
| Hard-coded Spark memory, Spark cache, Python UDF | `src/legacy/old_etl.py` | CODE-003 | yes |
| Copied code | `src/legacy/old_etl_copy.py` | CODE-002 | yes |
| One library pinned to two versions | `requirements.txt`, `src/legacy/old_etl.py` | LIB-001 | yes |
| Table without comment; table with a comment but no column comment | `data/setup.sql`, `orders_raw`, `events_raw` | GOV-001 | yes, both |
| Documented tables (must not be reported) | `data/setup.sql`, `policies`, `customers` | not GOV-001 | yes, not reported |
| Tables owned by a person | `data/setup.sql` | GOV-002 | yes, 4 tables |
| Personal column without a mask (`phone`), next to a masked one (`email`) | `data/setup.sql`, `customers` | PII-001 on `phone` only | yes, `phone` only (guessed from names: data classification not readable) |
| UC functions, one without comment | `data/setup.sql` | inventory: functions collected | yes, 3 |

Must not be reported:

| Situation | Rule | Found |
|---|---|---|
| A Databricks-hosted model endpoint (`databricks-…`) used by the code | BUNDLE-003 | not reported (fixed after the first run) |
| Tables the notebooks create themselves (`customer_contacts`, `events_clean`) | REF-001 | not reported (fixed after the second run) |
| `INSERT INTO` right after `CREATE OR REPLACE TABLE` of the same table | IO-004 | not reported on `data/setup.sql` (fixed after the second run) |
