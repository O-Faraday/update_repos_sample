# Runbook: Airflow DAG `shop_nightly`

Defined in `airflow/dags/nightly.py`; scheduled and run by Airflow, outside Databricks.

## Tasks, in order

| Task | Does | After |
|---|---|---|
| `fetch_partner_rates` | runs in Airflow (BashOperator) | - |
| `ingest` | runs the Databricks job `sample_ingest` | `fetch_partner_rates` |
| `dbt_build` | runs dbt on Databricks (`dbt deps`, `dbt build`) | `ingest` |

## Runs on Databricks

- job `sample_ingest` (see [its runbook](job_sample_ingest.md))
- `transform/dbt_project.yml`

## If it fails

Airflow reports the failed task; the Databricks runs it started keep their own history. Rerun from the failed task in Airflow.
