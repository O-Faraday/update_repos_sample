# What the agent should find

The evaluation set of the sample: each situation, where it is, and the rule
that should report it. "Not yet" marks what the agent does not see yet.

| Situation | Where | Rule |
|---|---|---|
| Bundle found, with includes, variables, two targets | `databricks.yml` | inventory: `inv_bundle` |
| Include pattern that matches no file | `databricks.yml`, `resources/optional/*.yml` | BUNDLE-002 |
| Prod-only job with a notebook not in the repository | `databricks.yml`, target prod | BUNDLE-002 |
| Job created by hand, outside the bundle | `manual/job_created_by_hand.json` | BUNDLE-003, JOB-005 |
| Declared job missing from the workspace (delete `sample_legacy_cleanup` by hand) | `resources/jobs.yml` | BUNDLE-001 |
| Job without retries, timeout or failure notification | `resources/jobs.yml`, `sample_ingest` | JOB-004 |
| Job on an all-purpose cluster | prod target | JOB-001 (only once deployed to prod) |
| CSV read without a schema | `src/ingest/load_orders.py` | IO-006 |
| Write in a try whose except swallows the error | `src/ingest/load_orders.py` | IO-001 |
| Append write, not idempotent | `src/ingest/load_orders.py` | IO-004 |
| Table name built from widgets and f-strings | `src/ingest/load_orders.py` | inventory: target resolved |
| Password in code | `src/ingest/load_customers.py` | SEC-001 |
| HTTP call without timeout or error handling | `src/ingest/load_customers.py` | IO-002, IO-003 |
| One-level table name completed by USE CATALOG / USE SCHEMA | `src/ingest/load_customers.py` | inventory: target resolved |
| Stream without checkpoint | `src/ingest/stream_events.py` | IO-005 |
| Libraries that cannot be installed together | `src/genai/ask_policy.py` | LIB-002 |
| Vector search and model call without error handling | `src/genai/ask_policy.py` | IO-002 |
| Index, vector search endpoint and serving endpoint that do not exist | `src/genai/ask_policy.py` | REF-001 |
| Model client built in another file | `src/common/llm.py` | not yet (endpoint unresolved) |
| `ai_query` in SQL | `src/genai/ask_policy.py` | inventory: model endpoint linked |
| DBFS mount, /mnt paths, Hive metastore, RDD | `src/legacy/old_etl.py` | CODE-001 |
| Hard-coded Spark memory, Spark cache, Python UDF | `src/legacy/old_etl.py` | CODE-003 |
| Copied code | `src/legacy/old_etl_copy.py` | CODE-002 |
| One library pinned to two versions | `requirements.txt`, `src/legacy/old_etl.py` | LIB-001 |
| Schema and tables without comments, owned by a person | `resources/schema.yml` | GOV-001, GOV-002 (once tables exist) |
