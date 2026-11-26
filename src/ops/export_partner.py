# Databricks notebook source
# MAGIC %md
# MAGIC # Export for a partner (run by hand)
# MAGIC Writes the day's clean orders as a CSV file in the volume, for a partner to pick up.
# MAGIC Not in any job: someone runs it when the partner asks.

# COMMAND ----------

dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")

# The partner's export account.
partner_password = "Shop-Export-2026!"

# COMMAND ----------

(spark.table(f"{CATALOG}.{SCHEMA}.orders_clean")
 .write.mode("overwrite").option("header", True)
 .csv(f"/Volumes/{CATALOG}/{SCHEMA}/raw/exports/orders"))
