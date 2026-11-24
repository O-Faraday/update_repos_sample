# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest return files with Auto Loader (synthetic)

# COMMAND ----------

returns = (spark.readStream.format("cloudFiles")
           .option("cloudFiles.format", "json")
           .load("/Volumes/demo/update_repos_sample/raw/returns"))

(returns.writeStream
    .trigger(processingTime="10 seconds")
    .toTable("demo.update_repos_sample.returns_bronze"))
