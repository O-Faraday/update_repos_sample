# Demo data

Synthetic tables, functions and files for the sample, in the Unity Catalog
catalog `demo`, schema `update_repos_sample`. Every row is invented.

| Object | Kind | Why it is there |
|---|---|---|
| `orders_raw` | table | read and appended by `src/ingest/load_orders.py`; no comment (GOV-001) |
| `customers` | table | personal columns: `email` masked by `mask_email`, `phone` not (PII-001) |
| `events_raw` | table | source of the stream in `src/ingest/stream_events.py` |
| `policies` | table | documented (no GOV-001); read by `ai_query` in `src/genai/ask_policy.py` |
| `mask_email` | SQL function | the column mask of `customers.email` |
| `amount_band` | SQL function | documented |
| `normalize_country` | Python function | no comment |
| `raw` | volume | `raw/orders/orders.csv`, read without a schema by `load_orders.py` (IO-006) |
| `orders_gold_clean` (setup_clean.sql) | table | written to guidance: commented, clustered (must not be reported) |
| `country_code` (setup_clean.sql) | SQL function | written to guidance: commented |
| `grants.sql`, `setup_silver.sql` | SQL | never run: read by the code review only (grants to every user, external silver table, small partitioned table) |

Left missing on purpose (REF-001): the vector index `policy_index`, the
serving endpoint `sample-shipping-endpoint`, and the tables the notebooks
create themselves (`customer_contacts`, `events_clean`).

## Load

`setup.sql`, then `setup_clean.sql`, run statement by statement on a SQL warehouse (the SQL editor,
or the Statement Execution API). Then copy the raw file to the volume:

```bash
databricks fs cp data/raw/orders.csv dbfs:/Volumes/demo/update_repos_sample/raw/orders/orders.csv --profile <profile>
```

The catalog `demo` must exist, and the user needs `CREATE SCHEMA` on it.
