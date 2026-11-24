# Databricks notebook source
# MAGIC %md
# MAGIC # Train the basket model (synthetic)

# COMMAND ----------

import mlflow
from sklearn.linear_model import LinearRegression

# The workspace model registry, not Unity Catalog.
mlflow.set_registry_uri("databricks")

df = spark.table("demo.update_repos_sample.orders_raw").toPandas()
model = LinearRegression().fit(df[["customer_id"]], df["amount"])
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "basket_model", registered_model_name="basket_model")
