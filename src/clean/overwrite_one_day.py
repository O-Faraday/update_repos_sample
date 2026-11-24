# Databricks notebook source
# MAGIC %md
# MAGIC # Reload one day of orders (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
dbutils.widgets.text("day", "2026-10-01")
day = dbutils.widgets.get("day")
daily = spark.table("demo.update_repos_sample.orders_raw").where(f"to_date(order_ts) = '{day}'")

# Replaces this day only.
(daily.write.mode("overwrite")
    .option("replaceWhere", f"to_date(order_ts) = '{day}'")
    .saveAsTable("demo.update_repos_sample.orders_daily_clean"))
