# Databricks notebook source
# MAGIC %md
# MAGIC # Clean orders
# MAGIC Cleans the country codes of the orders with the shared pandas helpers and writes `orders_clean`.
# MAGIC pandas is pinned below to another version than in requirements.txt (LIB-001).

# COMMAND ----------

# MAGIC %pip install pandas==2.2.2

# COMMAND ----------

import sys

sys.path.append("..")  # src/, for the shared helpers
from common.frames import is_text_column, orders_frame

dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")

# COMMAND ----------

# The whole table collected to the driver to use pandas (CODE-003): fine for the sample, not for a real
# volume of orders.
rows = spark.table(f"{CATALOG}.{SCHEMA}.orders_raw").select("order_id", "country", "amount").toPandas()
frame = orders_frame(rows.to_dict("records"))
if not is_text_column(frame, "country"):
    raise ValueError("country should be text")

spark.createDataFrame(frame).write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.orders_clean")
