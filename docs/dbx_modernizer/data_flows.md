# Data flows

What the code reads and writes, from the code and from Unity Catalog lineage.

```mermaid
flowchart LR
  n1["customers"]
  n2[("demo.update_repos_sample.customers")]
  n3[("demo.update_repos_sample.orders_clean")]
  n4[("demo.update_repos_sample.orders_raw")]
  n5[("demo.update_repos_sample.raw")]
  n6[("demo.update_repos_sample.stg_customers")]
  n7[("demo.update_repos_sample.stg_orders")]
  n8[("demo.update_repos_sample_marts.customer_orders")]
  n9[("demo.update_repos_sample_marts.daily_revenue")]
  n10["orders"]
  n11["orders"]
  n12["src/ingest/load_customers"]
  n13["src/ingest/load_orders"]
  n14["src/ops/export_partner"]
  n15["src/prepare/clean_orders"]
  n16["transform/models/marts/customer_orders.sql"]
  n17["transform/models/marts/daily_revenue.sql"]
  n18["transform/models/staging/stg_customers.sql"]
  n19["transform/models/staging/stg_orders.sql"]
  n1 --> n12
  n5 --> n12
  n12 --> n2
  n5 --> n13
  n11 --> n13
  n13 --> n4
  n3 --> n14
  n14 --> n5
  n14 --> n10
  n4 --> n15
  n15 --> n3
  n6 --> n16
  n7 --> n16
  n16 --> n8
  n7 --> n17
  n17 --> n9
  n2 --> n18
  n18 --> n6
  n4 --> n19
  n19 --> n7
```

| Data | Written by | Read by |
|---|---|---|
| `customers` | - | `src/ingest/load_customers` |
| `demo.update_repos_sample.customers` | `src/ingest/load_customers` | `transform/models/staging/stg_customers.sql` |
| `demo.update_repos_sample.orders_clean` | `src/prepare/clean_orders` | `src/ops/export_partner` |
| `demo.update_repos_sample.orders_raw` | `src/ingest/load_orders` | `src/prepare/clean_orders`, `transform/models/staging/stg_orders.sql` |
| `demo.update_repos_sample.raw` | `src/ops/export_partner` | `src/ingest/load_customers`, `src/ingest/load_orders` |
| `demo.update_repos_sample.stg_customers` (created by the code; not in the workspace yet) | `transform/models/staging/stg_customers.sql` | `transform/models/marts/customer_orders.sql` |
| `demo.update_repos_sample.stg_orders` (created by the code; not in the workspace yet) | `transform/models/staging/stg_orders.sql` | `transform/models/marts/customer_orders.sql`, `transform/models/marts/daily_revenue.sql` |
| `demo.update_repos_sample_marts.customer_orders` (created by the code; not in the workspace yet) | `transform/models/marts/customer_orders.sql` | - |
| `demo.update_repos_sample_marts.daily_revenue` (created by the code; not in the workspace yet) | `transform/models/marts/daily_revenue.sql` | - |
| `orders` | - | `src/ingest/load_orders` |
| `orders` | `src/ops/export_partner` | - |
