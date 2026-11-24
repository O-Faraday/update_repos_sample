# Databricks notebook source
# MAGIC %md
# MAGIC # Register the basket model in Unity Catalog (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
import mlflow
from mlflow import MlflowClient
from sklearn.linear_model import LinearRegression

mlflow.set_registry_uri("databricks-uc")
MODEL = "demo.update_repos_sample.basket_model_clean"

data = (spark.table("demo.update_repos_sample.orders_raw").select("customer_id", "amount")
        .limit(10_000).toPandas())
model = LinearRegression().fit(data[["customer_id"]], data["amount"])
with mlflow.start_run():
    info = mlflow.sklearn.log_model(model, name="basket_model", registered_model_name=MODEL,
                                    input_example=data[["customer_id"]].head(5))
MlflowClient().set_registered_model_alias(MODEL, "champion", info.registered_model_version)
