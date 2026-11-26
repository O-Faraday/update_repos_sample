# Runbook: job `sample_ingest`

Deployed by the bundle `update_repos_sample`.

## What it runs

| Task | Runs | After | Reads | Writes |
|---|---|---|---|---|
| `load_orders` | `src/ingest/load_orders` (notebook) | - | `demo.update_repos_sample.raw`, `orders` | `demo.update_repos_sample.orders_raw` |
| `load_customers` | `src/ingest/load_customers` (notebook) | - | `customers`, `demo.update_repos_sample.raw` | `demo.update_repos_sample.customers` |
| `clean_orders` | `src/prepare/clean_orders` (notebook) | `load_orders`, `load_customers` | `demo.update_repos_sample.orders_raw` | `demo.update_repos_sample.orders_clean` |

## How it starts

- triggered by the Airflow DAG `shop_nightly` (see [its runbook](dag_shop_nightly.md))

## Data

Reads:
- `customers`
- `demo.update_repos_sample.orders_raw`
- `demo.update_repos_sample.raw`
- `orders`

Writes:
- `demo.update_repos_sample.customers`
- `demo.update_repos_sample.orders_clean`
- `demo.update_repos_sample.orders_raw`

## Safeguards

- retries: none on `clean_orders`, `load_customers`, `load_orders`
- timeout: none on `clean_orders`, `load_customers`, `load_orders`
- health rules: none
- recent runs: 1, of which 0 failed (window of the inventory)

## If it fails

These depend on what it writes, and get stale or wrong data:
- `transform/models/staging/stg_customers.sql` (reads `demo.update_repos_sample.customers`), run by `shop_nightly`
- `src/ops/export_partner` (reads `demo.update_repos_sample.orders_clean`)
- `transform/models/staging/stg_orders.sql` (reads `demo.update_repos_sample.orders_raw`), run by `shop_nightly`
- `transform/models/marts/customer_orders.sql` (reads `demo.update_repos_sample.stg_customers`), run by `shop_nightly`
- `transform/models/marts/daily_revenue.sql` (reads `demo.update_repos_sample.stg_orders`), run by `shop_nightly`

Who is told: no mail on failure.

To rerun after a failure: repair the run (only the failed tasks and those after them run again), once the cause is fixed.
