# update_repos_sample

A small synthetic shop on Databricks, to show what the
[dbx_modernizer](https://github.com/O-Faraday/databricks-uptodate-agent) agent does. It runs end to
end on its own data, with a few problems planted on purpose: [EXPECTED.md](EXPECTED.md) lists what
the agent should find, and why. Every name, value and credential is fake.

## The flow

```
data/*.csv ──(copied once)──> volume raw/          Airflow: airflow/dags/nightly.py
                                  │                    fetch_partner_rates (in Airflow)
               job ingest (resources/jobs.yml)  <──── ingest (runs the job by name)
                 load_orders     -> orders_raw
                 load_customers  -> customers
                 clean_orders    -> orders_clean    (pandas helpers: src/common/frames.py, tests/)
                                  │
               dbt (transform/)  <──────────────────── dbt_build
                 staging: stg_orders, stg_customers (views)
                 marts:   daily_revenue, customer_orders (<schema>_marts)

src/ops/export_partner.py: a notebook someone runs by hand, in no job
```

## Layout

```
databricks.yml        bundle, variables catalog and schema, targets dev (default) and prod
resources/jobs.yml    the ingest job
data/                 the raw files (orders, customers)
src/ingest/           loads of the raw files
src/prepare/          the cleaning, with the shared pandas helpers of src/common/
src/ops/              a notebook run by hand
tests/                unit tests of src/common/ (step 6 checks them before and after its changes)
transform/            the dbt project
airflow/dags/         the DAG that runs the job, then dbt (read by the agent, never run by it)
expected.yaml         what the agent should find (EXPECTED.md is generated from it)
```

## Set it up

Replace `demo` with a catalog of your workspace (and in `transform/profiles.yml` for a local dbt run).

```bash
databricks schemas create update_repos_sample demo --profile <profile>
databricks volumes create demo update_repos_sample raw MANAGED --profile <profile>
databricks fs cp data/orders.csv dbfs:/Volumes/demo/update_repos_sample/raw/orders/orders.csv --profile <profile>
databricks fs cp data/customers.csv dbfs:/Volumes/demo/update_repos_sample/raw/customers/customers.csv --profile <profile>
databricks bundle deploy -t dev --var catalog=demo --profile <profile>
databricks bundle run ingest -t dev --var catalog=demo --profile <profile>
```

The run creates the tables. Without the raw files, the agent reports the missing input (rule
IO-007) and does not test its changes (step 6c needs the project to run on its own data).

## Evaluation

`expected.yaml` is the agent's evaluation set for this example. The larger set of earlier versions
(116 planted situations) is kept at the tag `eval-v1`.
