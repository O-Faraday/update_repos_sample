# Databricks notebook source
# MAGIC %md
# MAGIC # Reload one day of orders (synthetic)

# COMMAND ----------

dbutils.widgets.text("day", "2026-10-01")
day = dbutils.widgets.get("day")
daily = spark.table("demo.update_repos_sample.orders_raw").where(f"to_date(order_ts) = '{day}'")

# Meant to replace one day: overwrites the whole table.
daily.write.mode("overwrite").saveAsTable("demo.update_repos_sample.orders_daily")
