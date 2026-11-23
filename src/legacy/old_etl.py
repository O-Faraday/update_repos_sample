# Databricks notebook source
# MAGIC %md
# MAGIC # Old ETL (synthetic)

# COMMAND ----------

# MAGIC %pip install pandas==2.2.2

# COMMAND ----------

# DBFS mount and /mnt paths instead of Unity Catalog volumes (CODE-001).
dbutils.fs.mount(source="s3a://sample-bucket.invalid/raw", mount_point="/mnt/sample_raw")
orders = spark.read.parquet("/mnt/sample_raw/orders")

# Hive metastore table (CODE-001).
legacy = spark.table("hive_metastore.default.orders_legacy")

# Hard-coded executor memory (CODE-003) and Spark cache on Delta data (CODE-003).
spark.conf.set("spark.executor.memory", "8g")
orders.cache()

# RDD API, not available on serverless or standard access mode (CODE-001).
counts = orders.rdd.map(lambda r: (r[0], 1)).reduceByKey(lambda a, b: a + b).collect()

# COMMAND ----------

from pyspark.sql.functions import udf  # noqa: E402


# Python UDF where a native function would do (CODE-003).
@udf("string")
def clean(value):
    return value.strip().lower() if value else value


cleaned = orders.withColumn("customer_key", clean("customer_id"))
cleaned.write.mode("overwrite").parquet("/mnt/sample_raw/clean")
for row in counts[:10]:
    print(row)
