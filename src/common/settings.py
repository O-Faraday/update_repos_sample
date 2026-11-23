# Databricks notebook source
# MAGIC %md
# MAGIC # Shared settings (synthetic)
# MAGIC Included by other notebooks with `%run`: they share these names.

# COMMAND ----------

CATALOG = "demo"
SCHEMA = "update_repos_sample"
POLICIES = f"{CATALOG}.{SCHEMA}.policies"
EXPERIMENT = "/Shared/update_repos_sample_agent"
AGENT_MODEL = f"{CATALOG}.{SCHEMA}.policy_agent"
