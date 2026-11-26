# Databricks notebook source
# MAGIC %md
# MAGIC # Load orders
# MAGIC Reads the raw order files of the volume and appends them to `orders_raw`.

# COMMAND ----------

dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")
RAW = f"/Volumes/{CATALOG}/{SCHEMA}/raw/orders"
TABLE = f"{CATALOG}.{SCHEMA}.orders_raw"

# COMMAND ----------

orders = spark.read.format("csv").option("header", True).option("inferSchema", True).load(RAW)

# COMMAND ----------

try:
    orders.write.mode("append").saveAsTable(TABLE)
except Exception as e:
    print(f"load failed: {e}")
