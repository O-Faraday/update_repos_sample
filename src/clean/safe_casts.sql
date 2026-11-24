-- Written to Databricks guidance: nothing here should be reported.
-- try_cast returns NULL for a value that is not a number, under ANSI mode too.
CREATE OR REPLACE VIEW demo.update_repos_sample.orders_amounts_clean
COMMENT 'Order amounts, NULL when the source value is not a number.'
AS SELECT order_id, try_cast(amount AS DECIMAL(10, 2)) AS amount
FROM demo.update_repos_sample.orders_raw;
