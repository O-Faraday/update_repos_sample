# Databricks notebook source
# MAGIC %md
# MAGIC # Customer report (synthetic)

# COMMAND ----------

# MAGIC %pip install openpyxl xlsxwriter

# COMMAND ----------

dbutils.widgets.text("country", "FR")
country = dbutils.widgets.get("country")

# The widget value is pasted into the SQL text.
customers = spark.sql(f"SELECT * FROM demo.update_repos_sample.customers WHERE country = '{country}'")

# COMMAND ----------

for row in customers.collect():
    # Personal data written to the driver logs.
    print(f"Processing customer {row['full_name']} <{row['email']}> {row['phone']}")
