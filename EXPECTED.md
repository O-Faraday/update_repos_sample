# What the agent should find: update_repos_sample

Generated from `expected.yaml` (do not edit by hand: edit the YAML and render again with `uv run dbxm-evaluate --render`). Every name, value and credential in the project is fake.

## Deterministic rules

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| R-SEC-001-password | report | Password written in a notebook | `src/ingest/load_customers.py` | SEC-001 |  |
| R2-BUNDLE-005-prod | report | Production target without run_as a service principal | `bundle:update_repos_sample` | BUNDLE-005 |  |
| R2-SEC-001-partner | report | API secret written in a notebook | `src/partners/export_partner.py` | SEC-001 |  |
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
| R2-IO-002-agent | report | Model call of the agent without error handling | `src/genai/agent.py` | IO-002 |  |
| R2-IO-002-partner | report | Partner API call without error handling | `src/partners/export_partner.py` | IO-002 |  |
| R2-IO-003-partner | report | Partner API call without timeout | `src/partners/export_partner.py` | IO-003 |  |
| R2-IO-005-autoloader | report | Auto Loader stream without checkpoint | `src/ingest/autoload_returns.py` | IO-005 |  |
| R2-PIPE-001-dlt | report | Python pipeline table without expectations | `src/pipeline/silver_orders.py` | PIPE-001 |  |
| R-BUNDLE-003-manual | report | Job of the project outside its bundle | `job:sample_manual_export` | BUNDLE-003 |  |
| R-JOB-003-ingest | report | Job never run and not scheduled | `job:ingest` | JOB-003 |  |
| R-JOB-004-ingest | report | Job without retries | `job:ingest` | JOB-004 |  |
| R-JOB-005-manual | report | Job created by hand | `job:sample_manual_export` | JOB-005 |  |
| R2-JOB-004-genai | report | Job with retries and timeouts but no failure notification | `job:genai_answers` | JOB-004 |  |
| R-GOV-001-events | report | Table comment but no column comment | `table:demo.update_repos_sample.events_raw` | GOV-001 |  |
| R-GOV-001-orders | report | Table without comment | `table:demo.update_repos_sample.orders_raw` | GOV-001 |  |
| R-GOV-002-owner | report | Table owned by a person | `table:demo.update_repos_sample.policies` | GOV-002 |  |
| R-CODE-003-collect | report | Spark cache | `src/legacy/old_etl.py` | CODE-003 |  |
| R2-CODE-003-report | report | Whole table collected to the driver | `src/reports/customer_report.py` | CODE-003 |  |
| R-CODE-002-copy | report | Copied code | `src/legacy/old_etl_copy.py` | CODE-002 |  |
| R-CODE-001-legacy | report | DBFS mount | `src/legacy/old_etl.py` | CODE-001 |  |
| R-LIB-001-versions | report | pandas pinned to two versions | `project` | LIB-001 |  |
| R2-CODE-001-registry | report | Workspace model registry instead of Unity Catalog | `src/ml/train_model.py` | CODE-001 |  |
| R-NOT-JOB-006-dev | must not report | Development job run as its developer | `job:ingest` | JOB-006 |  |
| R2-NOT-SEC-001-secrets | must not report | Token read from a secret scope | `src/clean/call_partner_api.py` | SEC-001 |  |
| R-NOT-IO-004-replace | must not report | INSERT right after CREATE OR REPLACE TABLE of the same table | `data/setup.sql` | IO-004 |  |
| R-NOT-REF-001-created | must not report | Table the notebooks create themselves | `table:demo.update_repos_sample.customer_contacts` | REF-001 |  |
| R-NOT-REF-001-stream | must not report | Table a stream creates | `table:demo.update_repos_sample.events_clean` | REF-001 |  |
| R2-NOT-IO-001-raise | must not report | Error raised again after the partner call | `src/clean/call_partner_api.py` | IO-001 |  |
| R2-NOT-IO-005-autoloader | must not report | Auto Loader with schema location and checkpoint | `src/clean/ingest_orders_autoloader.py` | IO-005 |  |
| R2-NOT-IO-005-clean | must not report | Stream with checkpoint and availableNow | `src/clean/stream_events.py` | IO-005 |  |
| R2-NOT-PIPE-001-py | must not report | Python materialized view with expectations | `src/clean/gold_kpis_pipeline.py` | PIPE-001 |  |
| R2-NOT-PIPE-001-sql | must not report | Materialized view with expectations | `src/clean/silver_orders_pipeline.sql` | PIPE-001 |  |
| R-NOT-BUNDLE-003-platform | must not report | Endpoint served by Databricks | `endpoint:databricks-meta-llama-3-3-70b-instruct` | BUNDLE-003 |  |
| R2-NOT-JOB-003-paused | must not report | Job with a paused schedule | `job:clean_orders` | JOB-003 |  |
| R2-NOT-JOB-004-clean | must not report | Job with retries | `job:clean_orders` | JOB-004 |  |
| R-NOT-GOV-001-customers | must not report | Documented table | `table:demo.update_repos_sample.customers` | GOV-001 |  |
| R-NOT-GOV-001-policies | must not report | Documented table | `table:demo.update_repos_sample.policies` | GOV-001 |  |
| R2-NOT-GOV-001-gold | must not report | Table and columns commented | `table:demo.update_repos_sample.orders_gold_clean` | GOV-001 |  |
| R2-NOT-CODE-003-bounded | must not report | toPandas after a limit on the same line | `src/clean/register_model.py` | CODE-003 |  |

## Code review (model)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| C2-grants | report | Grants to every user of the account | `data/grants.sql` | topic `account users|all users|every user|privilege|least`, lines 2-3 |  |
| C2-sql-injection | report | Widget value pasted into SQL text (injection) | `src/reports/customer_report.py` | topic `inject|f-string|parameter marker|untrusted|sanitiz`, lines 13-15 |  |
| C2-pii-logs | report | Names | `src/reports/customer_report.py` | topic `personal|pii|email|phone|sensitive|log`, lines 19-21 |  |
| C-config-none | report | Endpoint read from the model config without a check (None if the key is missing) | `src/genai/agent.py` | topic `config|none|missing`, lines 9-9 |  |
| C-json-schema | report | DataFrame built from an API response without schema or validation | `src/ingest/load_customers.py` | topic `schema|validat|json`, lines 14-15 |  |
| C2-ansi-cast | report | Cast that fails under ANSI mode | `src/ingest/clean_events.py` | topic `ANSI|try_cast|cast`, lines 17-18 |  |
| C2-autoloader-schema | report | Auto Loader without a schema location | `src/ingest/autoload_returns.py` | topic `schemaLocation|schema location|schema evolution|schema`, lines 7-9 |  |
| C2-dedup-key | report | dropDuplicates without a key | `src/ingest/clean_events.py` | topic `dropDuplicates|duplicate`, lines 14-15 |  |
| C2-merge-key | report | MERGE on a key that is not unique (customer | `src/ingest/merge_orders.py` | topic `key|unique|duplicate|multiple`, lines 12-16 |  |
| C2-overwrite-day | report | One day meant to be replaced | `src/ingest/overwrite_daily.py` | topic `replaceWhere|whole table|entire table|all data|overwrite`, lines 11-12 |  |
| C2-timezone | report | Local times parsed without a time zone (UTC on serverless) | `src/ingest/clean_events.py` | topic `time ?zone|UTC`, lines 11-12 |  |
| C-stream-trigger | report | Stream without a trigger (the default is not supported on serverless) | `src/ingest/stream_events.py` | topic `trigger|availableNow|serverless`, lines 9-12 |  |
| C2-hardcoded-date | report | Business date written in the code | `src/reports/kpis.py` | topic `hard-?coded|fixed date|parameter|widget`, lines 10-12 |  |
| C2-unpinned-pip | report | Libraries installed without versions | `src/reports/customer_report.py` | topic `pin|version|unpinned`, lines 7-7 |  |
| C2-external-silver | report | Silver table kept as an external table | `data/setup_silver.sql` | topic `external|managed|location`, lines 2-5 |  |
| C2-function-comment | report | UC function without a comment | `data/setup.sql` | topic `comment|document`, lines 93-99 |  |
| C-ai-query-scan | report | ai_query over a whole table on each run | `src/genai/ask_policy.py` | topic `scan|every row|all rows|whole table|limit|incremental`, lines 36-39 |  |
| C2-count-loop | report | One count per country in a loop | `src/reports/kpis.py` | topic `count|loop|groupBy|repeated`, lines 16-19 |  |
| C2-cross-join | report | Cross join of orders and customers | `src/reports/kpis.py` | topic `cross|cartesian`, lines 23-25 |  |
| C2-partition-small | report | Small table partitioned on a high-cardinality column | `data/setup_silver.sql` | topic `partition|cluster`, lines 8-11 |  |
| C2-processing-time | report | ProcessingTime trigger (not supported on serverless; availableNow would do) | `src/ingest/autoload_returns.py` | topic `processingTime|availableNow|trigger|serverless`, lines 11-12 |  |
| C2-dlt-module | report | Legacy dlt module instead of pyspark.pipelines | `src/pipeline/silver_orders.py` | topic `dlt|pyspark\.pipelines|legacy|deprecated`, lines 1-3 |  |
| C-NOT-password-repeat | must not report | Hard-coded password | `src/ingest/load_customers.py` | topic `password|credential` |  |
| C2-NOT-parameter-markers | must not report | SQL with parameter markers | `src/clean/report_parametrized.py` | topic `inject` |  |
| C-NOT-checkpoint-repeat | must not report | Missing checkpoint | `src/ingest/stream_events.py` | topic `checkpoint` |  |
| C2-NOT-timezone | must not report | Times converted with an explicit time zone | `src/clean/clean_events_tz.py` | topic `time ?zone` |  |
| C-NOT-two-level | must not report | Two-level table names where the names have three levels | `src/ingest/stream_events.py` | topic `two-level|two level` |  |

## Architecture review (model)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| A-no-evaluation | report | The agent is logged without an evaluation (its evaluation notebook is missing) | `src/genai/agent_driver.py` | topic `evaluat` |  |
| A-no-tests | report | No automated tests in the project | `project` | topic `test` |  |
| A-hive | report | Data outside Unity Catalog (hive_metastore) | `table:hive_metastore.default.orders_legacy` | topic `hive|unity catalog` |  |
| A2-duplicated-logic | report | Revenue by country computed twice | `src/reports/kpis.sql` | topic `duplicat|same|twice|both` |  |
| A2-hardcoded-catalog | report | Catalog and schema written in many files instead of parameters | `project` | topic `hard-?coded|catalog|parameter|configuration` |  |
| A2-workspace-registry | report | A model registered in the workspace registry | `src/ml/train_model.py` | topic `registry|unity catalog` |  |
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
| T2-bundle-sp | report | The bundle gets a service principal for production | `bundle:update_repos_sample` | one change with BUNDLE-005 |  |
| T2-partner | report | One change for the partner export | `src/partners/export_partner.py` | one change with SEC-001, IO-003 |  |
| T-genai-job | report | One change for the GenAI job | `job:genai_answers` | one change with LIB-002 |  |
| T-NOT-platform | must not report | No change on an endpoint Databricks serves | `endpoint:databricks-meta-llama-3-3-70b-instruct` | one change with  |  |

## Rewrite (step 6)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| W-secret | report | Password read from a secret scope | `src/ingest/load_customers.py` | SEC-001, diff `dbutils\.secrets\.get\(` |  |
| W2-partner-secret | report | Partner secret read from a secret scope | `src/partners/export_partner.py` | SEC-001, diff `dbutils\.secrets\.get\(` |  |
| W-checkpoint | report | Checkpoint on the stream | `src/ingest/stream_events.py` | IO-005, diff `checkpointLocation` |  |
| W-repin-conflict | report | Libraries pinned to versions that install together | `src/genai/ask_policy.py` | LIB-002, diff `pydantic==2\.` |  |
| W-reraise | report | Error raised again | `src/ingest/load_orders.py` | IO-001, diff `^\+\s+raise` |  |
| W-timeout | report | Timeout on the HTTP call | `src/ingest/load_customers.py` | IO-003, diff `timeout=\d+` |  |
| W2-autoloader-checkpoint | report | Checkpoint on the Auto Loader stream | `src/ingest/autoload_returns.py` | IO-005, diff `checkpointLocation` |  |
| W2-partner-timeout | report | Timeout on the partner call | `src/partners/export_partner.py` | IO-003, diff `timeout=\d+` |  |
| W-retries | report | Retries and timeouts in the bundle | `resources/jobs.yml` | JOB-004, diff `^\+\s+max_retries:` |  |
| W-upgrade-pandas | report | pandas pinned to the latest stable version that installs with the rest (6b) | `requirements.txt` | UPGRADE, diff `^\+pandas==3\.` |  |

## Unit tests before and after the rewrite (step 6c)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| U-pandas3-regression | report | Upgrade of pandas 2 to 3 (6b) breaks a check written for object dtype: a regression that blocks the delivery | `tests/test_frames.py` | test = tests.test_frames::test_country_is_text, before = passed, after = failed, verdict = regressions |  |
| U-frames-upper | report | pandas helper unaffected by pandas 3 still passes | `tests/test_frames.py` | test = tests.test_frames::test_orders_frame_upper_cases_the_country, before = passed, after = passed |  |
| U-known-bug | report | The project's known bug fails before and after (not the rewrite's) | `tests/test_pricing.py` | test = tests.test_pricing::test_normalize_country_trims_spaces, verdict = still_failing |  |
| U-paris-day | report | Time zone helper still passes | `tests/test_clean.py` | test = tests.test_clean::test_business_day_is_in_paris_time, before = passed, after = passed |  |
| U-vat-unchanged | report | A pure function untouched by the rewrite still passes | `tests/test_pricing.py` | test = tests.test_pricing::test_with_vat, before = passed, after = passed |  |

## What the integration test would run (step 6c)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| P-dag-repos-path | report | Notebook run from a hand-made Git folder | `airflow:sample_nightly` | task_key = customer_report, kind = notebook, runnable = False, depends_on = kpis |  |
| P-bundle-order | report | The bundle's ingest tasks run in their order | `job:ingest` | task_key = load_customers, kind = notebook, runnable = True, depends_on = load_orders |  |
| P-dag-outside | report | Bash and Python tasks run in Airflow and are only listed | `airflow:sample_nightly` | task_key = fetch_feed, kind = airflow, runnable = False, outside = True |  |
| P-dag-python-outside | report | The Python check of the feed is only listed | `airflow:sample_nightly` | task_key = check_feed, runnable = False, outside = True, depends_on = fetch_feed |  |
| P-dag-runnow-bundle | report | The DAG triggers the bundle's job by name (dev prefix) and it is tested once with the bundle | `airflow:sample_nightly` | task_key = ingest, kind = run_job, runnable = False, outside = True |  |
| P-dag-sql-file | report | SQL file of the project named relative to the DAG is replayed as a SQL file task after the ingest | `airflow:sample_nightly` | task_key = kpis, kind = sql_file, runnable = True, depends_on = ingest |  |
| P-dag-template | report | SQL with an Airflow template ({{ ds }}) is not replayed | `airflow:sample_nightly` | task_key = purge_day, kind = sql, runnable = False |  |
| P-dag-variable | report | Notebook path from an Airflow variable is not replayed | `airflow:sample_nightly` | task_key = export_partner, runnable = False, depends_on = customer_report |  |
| P-NOT-dag-runnow-twice | must not report | The triggered job's tasks are not replayed a second time under the DAG | `airflow:sample_nightly` | task_key = ingest.load_orders, kind = notebook |  |

## Clean files

Written to Databricks guidance: anything reported on them is a false positive.

- `src/clean/call_partner_api.py`
- `src/clean/clean_events_tz.py`
- `src/clean/dates.py`
- `src/clean/gold_kpis_pipeline.py`
- `src/clean/ingest_orders_autoloader.py`
- `src/clean/kpis_by_country.py`
- `src/clean/logging_setup.py`
- `src/clean/merge_orders_current.py`
- `src/clean/overwrite_one_day.py`
- `src/clean/register_model.py`
- `src/clean/report_parametrized.py`
- `src/clean/safe_casts.sql`
- `src/clean/settings.py`
- `src/clean/silver_orders_pipeline.sql`
- `src/clean/stream_events.py`
- `data/setup_clean.sql`
- `resources/clean_jobs.yml`
