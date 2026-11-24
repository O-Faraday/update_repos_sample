# Databricks notebook source
# MAGIC %md
# MAGIC # Clean raw events (synthetic)

# COMMAND ----------

from pyspark.sql import functions as F

raw = spark.table("demo.update_repos_sample.events_raw")

# Local times parsed without a time zone; the session time zone is UTC on serverless.
events = raw.withColumn("event_local", F.to_timestamp(F.col("event_ts").cast("string"), "yyyy-MM-dd HH:mm:ss"))

# Duplicates removed on every column: two events differing only by event_id both stay.
events = events.dropDuplicates()

# A text cast that fails under ANSI mode when a value is not a number.
events = events.withColumn("customer_key", F.col("customer_id").cast("string").cast("int"))
events.write.mode("overwrite").saveAsTable("demo.update_repos_sample.events_clean_batch")
