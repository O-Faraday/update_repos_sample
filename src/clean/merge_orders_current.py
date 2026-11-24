# Databricks notebook source
# MAGIC %md
# MAGIC # Merge order updates (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
from delta.tables import DeltaTable
from pyspark.sql import functions as F
from pyspark.sql.window import Window

dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")

# COMMAND ----------

updates = spark.table(f"{CATALOG}.{SCHEMA}.orders_raw")
# One row per order: the latest update wins.
latest = Window.partitionBy("order_id").orderBy(F.col("order_ts").desc())
updates = updates.withColumn("rank", F.row_number().over(latest)).where("rank = 1").drop("rank")

target = DeltaTable.forName(spark, f"{CATALOG}.{SCHEMA}.orders_current_clean")
(target.alias("t")
    .merge(updates.alias("s"), "t.order_id = s.order_id")
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute())
