# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest order files (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")
BASE = f"/Volumes/{CATALOG}/{SCHEMA}/raw"

# COMMAND ----------

orders_schema = "order_id BIGINT, customer_id BIGINT, amount DECIMAL(10,2), country STRING, order_ts TIMESTAMP"

stream = (spark.readStream.format("cloudFiles")
          .option("cloudFiles.format", "csv")
          .option("header", "true")
          .option("cloudFiles.schemaLocation", f"{BASE}/_schemas/orders")
          .schema(orders_schema)
          .load(f"{BASE}/orders"))

query = (stream.writeStream
         .option("checkpointLocation", f"{BASE}/_checkpoints/orders_bronze")
         .trigger(availableNow=True)
         .toTable(f"{CATALOG}.{SCHEMA}.orders_bronze_clean"))
query.awaitTermination()
