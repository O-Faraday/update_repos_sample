# Databricks notebook source
# MAGIC %md
# MAGIC # Customers of a country (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
dbutils.widgets.text("country", "FR")
country = dbutils.widgets.get("country")

# Parameter markers: the value is never pasted into the SQL text.
customers = spark.sql(
    "SELECT customer_id, country FROM demo.update_repos_sample.customers WHERE country = :country",
    args={"country": country},
)
customers.write.mode("overwrite").saveAsTable("demo.update_repos_sample.customers_by_country_clean")
