"""Nightly orchestration of the sample by Airflow, outside Databricks (Databricks provider operators).

Evaluation material for dbx_modernizer (expected.yaml, step integration_plan): what the
integration test of a rewrite would replay on Databricks, and what it would only list.
Synthetic: no connection, host or credential of a real workspace.
"""

from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.databricks.operators.databricks import (
    DatabricksNotebookOperator,
    DatabricksRunNowOperator,
    DatabricksSubmitRunOperator,
)
from airflow.providers.databricks.operators.databricks_sql import DatabricksSqlOperator

CONN = "databricks_default"
WAREHOUSE = "sample_warehouse"
# A Git folder checked out by hand: not the code the bundle deploys (stale after each merge).
REPO = "/Workspace/Repos/data/update_repos_sample"


def check_partner_feed(**_):
    """Runs in Airflow: nothing of it reaches Databricks."""
    return True


with DAG(dag_id="sample_nightly", start_date=datetime(2026, 1, 1), schedule="0 2 * * *", catchup=False) as dag:
    # Outside Databricks: listed for information, never replayed.
    fetch_feed = BashOperator(task_id="fetch_feed",
                              bash_command="curl -s https://partner.example.com/feed -o /tmp/feed.json")
    check_feed = PythonOperator(task_id="check_feed", python_callable=check_partner_feed)

    # The bundle's job: tested once, with the bundle.
    ingest = DatabricksRunNowOperator(task_id="ingest", databricks_conn_id=CONN, job_name="sample_ingest")

    # SQL file of the project, relative to this DAG: replayed as a SQL file task.
    kpis = DatabricksSqlOperator(task_id="kpis", databricks_conn_id=CONN, sql_warehouse_name=WAREHOUSE,
                                 sql="../../src/reports/kpis.sql")

    # Airflow template: the day is known only at run time, so it cannot be replayed as such.
    purge_day = DatabricksSqlOperator(
        task_id="purge_day", databricks_conn_id=CONN, sql_warehouse_name=WAREHOUSE,
        sql="DELETE FROM demo.update_repos_sample.orders_daily WHERE order_date = '{{ ds }}'")

    # Code from a hand-made Git folder, not from the bundle: outside the project's folder.
    report = DatabricksNotebookOperator(task_id="customer_report", databricks_conn_id=CONN,
                                        notebook_path=f"{REPO}/src/reports/customer_report",
                                        source="WORKSPACE", notebook_params={"country": "FR"})

    # Path from an Airflow variable: known only at run time.
    export = DatabricksSubmitRunOperator(
        task_id="export_partner", databricks_conn_id=CONN,
        json={"notebook_task": {"notebook_path": Variable.get("sample_files") + "/src/partners/export_partner"}})

    # The dbt project of the repository, built on a SQL warehouse from the Git repository: listed, not
    # replayed (the integration test does not run dbt tasks yet).
    dbt_build = DatabricksSubmitRunOperator(
        task_id="dbt_build", databricks_conn_id=CONN,
        json={"git_source": {"git_url": "https://github.com/O-Faraday/update_repos_sample",
                             "git_provider": "gitHub", "git_branch": "main"},
              "dbt_task": {"project_directory": "transform", "commands": ["dbt deps", "dbt build"],
                           "warehouse_id": "{{ var.value.sample_warehouse_id }}"}})

    fetch_feed >> check_feed >> ingest >> [kpis, purge_day, dbt_build]
    kpis >> report >> export
