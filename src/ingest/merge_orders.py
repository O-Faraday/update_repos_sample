# Databricks notebook source
# MAGIC %md
# MAGIC # Merge order updates (synthetic)

# COMMAND ----------

updates = spark.table("demo.update_repos_sample.orders_raw")
updates.createOrReplaceTempView("updates")

# The match key is the customer, not the order: several updates match one row.
spark.sql("""
MERGE INTO demo.update_repos_sample.orders_current t
USING updates s
ON t.customer_id = s.customer_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
""")
