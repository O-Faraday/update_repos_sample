# Databricks notebook source
# MAGIC %md
# MAGIC # Load customers (synthetic)

# COMMAND ----------

import requests

API = "https://api.example.invalid/customers"
# A fake password written in the code (SEC-001): it should come from a secret scope.
password = "not-a-real-password-123"

# HTTP call without timeout or error handling (IO-002, IO-003).
response = requests.get(API, auth=("sample", password))
customers = spark.createDataFrame(response.json())

# COMMAND ----------

spark.sql("USE CATALOG main")
spark.sql("USE SCHEMA update_repos_sample")
# A one-level name, completed by the USE statements above.
customers.write.mode("overwrite").saveAsTable("customers")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE main.update_repos_sample.customer_contacts AS
# MAGIC SELECT customer_id, email, phone FROM main.update_repos_sample.customers
