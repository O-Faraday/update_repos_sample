# Databricks notebook source
# MAGIC %md
# MAGIC # Stream events (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
events = spark.readStream.table("demo.update_repos_sample.events_raw")

query = (events.writeStream
         .option("checkpointLocation", "/Volumes/demo/update_repos_sample/raw/_checkpoints/events_clean_ok")
         .trigger(availableNow=True)
         .toTable("demo.update_repos_sample.events_clean_ok"))
query.awaitTermination()
