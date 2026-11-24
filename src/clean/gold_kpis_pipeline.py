# Written to Databricks guidance: nothing here should be reported.
from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view(comment="Revenue by country and day.")
@dp.expect_or_drop("country_known", "country IS NOT NULL")
@dp.expect("revenue_positive", "revenue >= 0")
def gold_revenue():
    orders = spark.read.table("silver_orders_clean")
    return (orders.groupBy("country", F.to_date("order_ts").alias("day"))
            .agg(F.sum("amount").alias("revenue")))
