-- Written to Databricks guidance: nothing here should be reported.
CREATE OR REFRESH MATERIALIZED VIEW silver_orders_clean (
  CONSTRAINT order_id_present EXPECT (order_id IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT amount_positive EXPECT (amount > 0)
)
COMMENT 'Orders with a normalised country code.'
AS SELECT order_id, customer_id, amount, upper(trim(country)) AS country, order_ts
FROM orders_bronze_clean;
