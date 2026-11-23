# Databricks notebook source
# MAGIC %md
# MAGIC # Log and evaluate the policy agent (synthetic)

# COMMAND ----------

# MAGIC %run ../common/settings

# COMMAND ----------

# MAGIC %pip install -r ../../requirements.txt

# COMMAND ----------

import mlflow

mlflow.set_experiment(EXPERIMENT)  # from %run ../common/settings
mlflow.set_registry_uri("databricks-uc")

# The agent is a model from code: the script, its configuration and the shared code.
with mlflow.start_run():
    info = mlflow.pyfunc.log_model(
        name="policy_agent",
        python_model="agent.py",
        model_config="agent_config.yaml",
        code_paths=["../common"],
        registered_model_name=AGENT_MODEL,
    )

# COMMAND ----------

# The evaluation notebook is not in the repository (REF-001 on a missing notebook).
dbutils.notebook.run("./evaluate_agent", 600, {"model": AGENT_MODEL})

# COMMAND ----------

# Reads the policies table named in the shared settings.
policies = spark.table(POLICIES)

# COMMAND ----------

# MAGIC %sh
# MAGIC curl -s https://docs.example.invalid/policies/latest.json -o /tmp/policies.json
