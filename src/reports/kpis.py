# Databricks notebook source
# MAGIC %md
# MAGIC # Daily KPIs (synthetic)

# COMMAND ----------

orders = spark.table("demo.update_repos_sample.orders_raw")
customers = spark.table("demo.update_repos_sample.customers")

# A fixed day: the notebook cannot be rerun for another date.
day = "2026-10-01"
today = orders.where(f"to_date(order_ts) = '{day}'")

# COMMAND ----------

# One Spark job per country.
for code in ["FR", "DE", "ES", "IT", "BE"]:
    n = today.where(f"upper(trim(country)) = '{code}'").count()
    print(code, n)

# COMMAND ----------

# Every order paired with every customer.
pairs = orders.crossJoin(customers)
pairs.write.mode("overwrite").saveAsTable("demo.update_repos_sample.order_customer_pairs")

# COMMAND ----------

from pyspark.sql import functions as F  # noqa: E402

revenue = orders.groupBy(F.upper(F.trim("country")).alias("country")).agg(F.sum("amount").alias("revenue"))
revenue.write.mode("overwrite").saveAsTable("demo.update_repos_sample.revenue_by_country")
