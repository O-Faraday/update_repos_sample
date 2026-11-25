# Databricks notebook source
# MAGIC %md
# MAGIC # Load customers
# MAGIC Reads the raw customer file of the volume and replaces `customers`.

# COMMAND ----------

from pyspark.sql.functions import udf

dbutils.widgets.text("catalog", "demo")
dbutils.widgets.text("schema", "update_repos_sample")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")

# COMMAND ----------

customers = (spark.read.format("csv").option("header", True)
             .schema("customer_id INT, name STRING, email STRING, phone STRING, country STRING")
             .load(f"/Volumes/{CATALOG}/{SCHEMA}/raw/customers"))


# A Python UDF where a native function does the same (upper(trim(country))): slower (CODE-003).
@udf("string")
def country_code(value):
    return (value or "").strip().upper()


customers = customers.withColumn("country", country_code("country"))

# COMMAND ----------

# Email and phone are written without a column mask (PII-001, once the table exists).
customers.write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.customers")
