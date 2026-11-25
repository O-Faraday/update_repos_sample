# Databricks notebook source
# MAGIC %md
# MAGIC # Export for a partner (run by hand)
# MAGIC Writes the day's clean orders as a CSV file in the volume, for a partner to pick up.
# MAGIC Not in any job: someone runs it when the partner asks.

# COMMAND ----------

dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")

# A fake password written in the code (SEC-001): it belongs in a secret scope.
partner_password = dbutils.secrets.get(scope="<secret scope>", key="partner_password")

# COMMAND ----------

(spark.table(f"{CATALOG}.{SCHEMA}.orders_clean")
 .write.mode("overwrite").option("header", True)
 .csv(f"/Volumes/{CATALOG}/{SCHEMA}/raw/exports/orders"))
