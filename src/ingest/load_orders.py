# Databricks notebook source
# MAGIC %md
# MAGIC # Load orders (synthetic)
# MAGIC Reads the raw order files of the volume and appends them to a table.

# COMMAND ----------

dbutils.widgets.text("catalog", "main")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")
RAW = f"/Volumes/{CATALOG}/{SCHEMA}/raw/orders"
TABLE = f"{CATALOG}.{SCHEMA}.orders_raw"

# COMMAND ----------

# CSV read without a schema: the types change with the files (IO-006).
orders = spark.read.format("csv").option("header", True).load(RAW)

# COMMAND ----------

# Append in a try whose except swallows the error: a failed load goes
# unnoticed (IO-001), and a rerun duplicates the rows (IO-004).
try:
    orders.write.mode("append").saveAsTable(TABLE)
except Exception as e:
    print(f"load failed: {e}")
