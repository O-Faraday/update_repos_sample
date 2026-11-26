"""The shop's nightly run, scheduled by Airflow outside Databricks (Databricks provider operators).

fetch_partner_rates runs in Airflow itself. Then the ingest job of the bundle loads the raw files,
and dbt builds its models from the tables it wrote.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.databricks.operators.databricks import (
    DatabricksRunNowOperator,
    DatabricksSubmitRunOperator,
)

CONN = "databricks_default"

with DAG(dag_id="shop_nightly", start_date=datetime(2026, 1, 1), schedule="0 2 * * *", catchup=False) as dag:
    # Runs in Airflow.
    fetch_rates = BashOperator(task_id="fetch_partner_rates", bash_command="echo 'rates fetched'")

    # The bundle's job, by name.
    ingest = DatabricksRunNowOperator(task_id="ingest", databricks_conn_id=CONN, job_name="sample_ingest")

    # The dbt project of the repository, built on a SQL warehouse from the Git repository.
    dbt_build = DatabricksSubmitRunOperator(
        task_id="dbt_build", databricks_conn_id=CONN,
        json={"git_source": {"git_url": "https://github.com/O-Faraday/update_repos_sample",
                             "git_provider": "gitHub", "git_branch": "main"},
              "dbt_task": {"project_directory": "transform", "commands": ["dbt deps", "dbt build"],
                           "catalog": "demo", "schema": "update_repos_sample",
                           "warehouse_id": "{{ var.value.shop_warehouse_id }}"}})

    fetch_rates >> ingest >> dbt_build
