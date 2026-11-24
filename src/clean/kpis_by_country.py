# Databricks notebook source
# MAGIC %md
# MAGIC # KPIs by country (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
from pyspark.sql import functions as F

dbutils.widgets.text("day", "2026-10-01")
day = dbutils.widgets.get("day")
orders = spark.table("demo.update_repos_sample.orders_raw").where(F.to_date("order_ts") == F.lit(day))

# One aggregation for every country, in Spark.
counts = orders.groupBy(F.upper(F.trim("country")).alias("country")).count()
counts.write.mode("overwrite").saveAsTable("demo.update_repos_sample.orders_count_by_country_clean")
