# What the agent should find: update_repos_sample

Generated from `expected.yaml` (do not edit by hand: edit the YAML and render again with `uv run dbxm-evaluate --render`). Every name, value and credential in the project is fake.

## Deterministic rules

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| R-BUNDLE-005 | report | Production target without run_as a service principal | `bundle:update_repos_sample` | BUNDLE-005 |  |
| R-DBT-006 | report | Token written in the dbt profile | `transform/profiles.yml` | DBT-006 |  |
| R-SEC-001 | report | Password written in a notebook run by hand | `src/ops/export_partner.py` | SEC-001 |  |
| R-PII-001 | report | Email and phone without a column mask | `table:demo.update_repos_sample.customers` | PII-001 |  |
| R-DBT-002 | report | Incremental model merged without unique_key | `transform/models/marts/daily_revenue.sql` | DBT-002 |  |
| R-DBT-003 | report | A model without tests | `transform/dbt_project.yml` | DBT-003 |  |
| R-DBT-004 | report | A source without freshness | `transform/dbt_project.yml` | DBT-004 |  |
| R-IO-001 | report | Write in a try whose except swallows the error | `src/ingest/load_orders.py` | IO-001 |  |
| R-IO-004 | report | Append write, not idempotent | `src/ingest/load_orders.py` | IO-004 |  |
| R-IO-006 | report | CSV read without a schema | `src/ingest/load_orders.py` | IO-006 |  |
| R-JOB-004 | report | Job without retries, timeout or failure notification | `job:ingest` | JOB-004 |  |
| R-GOV-001 | report | Table without description | `table:demo.update_repos_sample.orders_raw` | GOV-001 |  |
| R-CODE-003-collect | report | Whole table collected to the driver | `src/prepare/clean_orders.py` | CODE-003 |  |
| R-CODE-003-udf | report | Python UDF where a native function exists | `src/ingest/load_customers.py` | CODE-003 |  |
| R-LIB-001 | report | pandas pinned to two versions (requirements.txt and a notebook) | `project` | LIB-001 |  |
| R-NOT-DBT-002 | must not report | Incremental model merged on its key | `transform/models/marts/customer_orders.sql` | DBT-002 |  |
| R-NOT-IO-006 | must not report | CSV read with a schema | `src/ingest/load_customers.py` | IO-006 |  |
| R-NOT-IO-007 | must not report | The raw files the job reads are there | `volume:demo.update_repos_sample.raw` | IO-007 |  |
| R-NOT-REF-001 | must not report | Every object the code uses exists | `table:demo.update_repos_sample.orders_raw` | REF-001 |  |

## Code review (model)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| C-duplicates | report | Orders appended on each run are cleaned without removing duplicates | `src/prepare/clean_orders.py` | topic `duplicat|dedup|distinct|append` |  |
| C-NOT-password-repeat | must not report | The password is a rule's finding, not repeated by the model | `src/ops/export_partner.py` | topic `password|credential|secret` |  |

## Architecture review (model)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| A-manual-export | report | A notebook run by hand, in no job | `src/ops/export_partner.py` | topic `manual|by hand|not scheduled|no job|orphan` |  |
| A-NOT-orphan-frames | must not report | The shared helpers are imported by a notebook of the job | `src/common/frames.py` | topic `orphan|unused|not used|dead` |  |

## Inventory

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| I-dag | report | The Airflow DAG is an object of the graph | `airflow_dag:shop_nightly` | `inv_nodes`: status = present, layer = 2-orchestration |  |
| I-inputs | report | The raw files the job loads are in the volume | `volume:demo.update_repos_sample.raw` | `inv_facts`: probe = data_sources |  |
| I-widgets | report | Volume path built from widgets and an f-string | `src/ingest/load_orders.py` | `inv_io`: target = /Volumes/demo/update_repos_sample/raw/orders, resolved = True |  |

## Target design (step 4)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| T-ingest-job | report | One change for the ingest job and the code it runs | `job:ingest` | one change with IO-001, JOB-004 |  |

## Rewrite (step 6)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| W-secret | report | Password read from a secret scope | `src/ops/export_partner.py` | SEC-001, diff `dbutils\.secrets\.get\(` |  |
| W-reraise | report | Error raised again | `src/ingest/load_orders.py` | IO-001, diff `^\+\s+raise` |  |
| W-retries | report | Retries and timeouts in the bundle | `resources/jobs.yml` | JOB-004, diff `^\+\s+max_retries:` |  |
| W-adapt-frames | report | is_text_column adapted to pandas 3, where text columns are of the str dtype, not object | `src/common/frames.py` | ADAPT, diff `^\+.*(is_string_dtype|StringDtype|pd\.api\.types|"str"|\bstr\b)` |  |
| W-upgrade-pandas | report | pandas pinned to the latest stable version that installs with the rest | `requirements.txt` | UPGRADE, diff `^\+pandas==3\.` |  |
| W-NOT-adapt-tests | must not report | The code model never changes the project's tests | `tests/test_frames.py` | ADAPT, diff `.` |  |

## Unit tests before and after the rewrite (step 6c)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| U-pandas3-adapted | report | With is_text_column adapted to pandas 3, the text check still passes | `tests/test_frames.py` | test = tests.test_frames::test_country_is_text, before = passed, after = passed |  |
| U-frames-clean | report | The country cleaning still passes | `tests/test_frames.py` | test = tests.test_frames::test_orders_frame_cleans_the_country, before = passed, after = passed |  |

## What the integration test would run (step 6c)

| Id | Expect | Situation | Where | What | Result |
|---|---|---|---|---|---|
| P-dag-dbt | report | The DAG's dbt build (Git source, relative project directory) is replayed on a copy of transform/ | `airflow:shop_nightly` | task_key = dbt_build, kind = dbt, runnable = True, depends_on = ingest |  |
| P-dag-outside | report | The Bash task runs in Airflow and is only listed | `airflow:shop_nightly` | task_key = fetch_partner_rates, kind = airflow, runnable = False, outside = True |  |
| P-dag-runnow | report | The DAG triggers the bundle's job by name, which is tested once with the bundle | `airflow:shop_nightly` | task_key = ingest, kind = run_job, runnable = False, outside = True |  |
| P-job-order | report | The job's cleaning runs after both loads | `job:ingest` | task_key = clean_orders, kind = notebook, runnable = True |  |
| P-NOT-dag-runnow-twice | must not report | The triggered job's tasks are not replayed a second time under the DAG | `airflow:shop_nightly` | task_key = ingest.load_orders, kind = notebook |  |

## Clean files

Written to Databricks guidance: anything reported on them is a false positive.

- `transform/models/staging/stg_orders.sql`
- `transform/models/staging/stg_customers.sql`
- `transform/models/marts/customer_orders.sql`
- `tests/test_frames.py`
