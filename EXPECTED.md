# What the agent should find

The evaluation set of the sample: each situation, where it is, the rule that
should report it, and what the agent found on its last run (2026-11-23,
deployed to a dev target, nothing run; demo data loaded afterwards). "Not yet" marks what the agent does
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
| Index, serving endpoint, Hive table and tables the notebooks create, that do not exist | `src/genai/ask_policy.py`, `src/ingest/*`, `src/legacy/*` | REF-001 | to check with the data (yes on 10 objects before it) |
| Model client built in another file | `src/common/llm.py` | not yet (endpoint unresolved) | not yet |
| `ai_query` in SQL | `src/genai/ask_policy.py` | inventory: model endpoint linked | yes |
| DBFS mount, /mnt paths, Hive metastore, RDD | `src/legacy/old_etl.py` | CODE-001 | yes |
| Hard-coded Spark memory, Spark cache, Python UDF | `src/legacy/old_etl.py` | CODE-003 | yes |
| Copied code | `src/legacy/old_etl_copy.py` | CODE-002 | yes |
| One library pinned to two versions | `requirements.txt`, `src/legacy/old_etl.py` | LIB-001 | yes |
| Table without comment | `data/setup.sql`, `orders_raw` | GOV-001 | to check |
| Documented table (must not be reported) | `data/setup.sql`, `policies` | not GOV-001 | to check |
| Tables owned by a person | `data/setup.sql` | GOV-002 | to check |
| Personal column without a mask (`phone`), next to a masked one (`email`) | `data/setup.sql`, `customers` | PII-001 on `phone` only | to check |
| UC functions, one without comment | `data/setup.sql` | inventory: functions collected | to check |

Must not be reported:

| Situation | Rule | Found |
|---|---|---|
| A Databricks-hosted model endpoint (`databricks-…`) used by the code | BUNDLE-003 | reported on the first run; fixed in the agent the same day |
