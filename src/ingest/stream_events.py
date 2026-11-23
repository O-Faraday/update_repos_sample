# Databricks notebook source
# MAGIC %md
# MAGIC # Stream events (synthetic)

# COMMAND ----------

events = spark.readStream.table("main.update_repos_sample.events_raw")

# A stream without checkpointLocation restarts from scratch after a failure (IO-005).
(events.writeStream
    .outputMode("append")
    .toTable("main.update_repos_sample.events_clean"))
