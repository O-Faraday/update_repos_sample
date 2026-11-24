# Databricks notebook source
# MAGIC %md
# MAGIC # Export orders to a partner (synthetic)

# COMMAND ----------

import requests

PARTNER_URL = "https://partner.example.invalid/api/orders"
api_secret = "not-a-real-secret-value-42"

orders = spark.table("demo.update_repos_sample.orders_raw").limit(100).toPandas()

# COMMAND ----------

# Posted without timeout, retry or error handling.
response = requests.post(PARTNER_URL, json=orders.to_dict(orient="records"),
                         headers={"Authorization": f"Bearer {api_secret}"})
print(response.status_code)
