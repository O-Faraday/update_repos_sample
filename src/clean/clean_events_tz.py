# Databricks notebook source
# MAGIC %md
# MAGIC # Clean raw events (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
from pyspark.sql import functions as F

raw = spark.table("demo.update_repos_sample.events_raw")
events = (raw
          .withColumn("event_utc", F.to_utc_timestamp(F.col("event_ts"), "Europe/Paris"))
          .dropDuplicates(["event_id"])
          .withColumn("customer_key", F.expr("try_cast(customer_id AS INT)")))
events.write.mode("overwrite").saveAsTable("demo.update_repos_sample.events_clean_tz")
