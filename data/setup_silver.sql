-- A silver table kept as an external table on a cloud path.
CREATE TABLE IF NOT EXISTS demo.update_repos_sample.orders_silver_ext (
  order_id BIGINT, customer_id BIGINT, amount DECIMAL(10, 2), country STRING
)
LOCATION 's3://sample-bucket.invalid/silver/orders';

-- A small table partitioned on a high-cardinality column.
CREATE TABLE IF NOT EXISTS demo.update_repos_sample.orders_by_id (
  order_id BIGINT, amount DECIMAL(10, 2)
)
PARTITIONED BY (order_id);
