# Databricks notebook source
# MAGIC %md
# MAGIC # Answer policy questions (synthetic)

# COMMAND ----------

# Versions that cannot be installed together: langchain-core 0.3 needs pydantic 2 (LIB-002).
# MAGIC %pip install langchain-core==0.3.0 pydantic==1.10.13 databricks-langchain databricks-vectorsearch

# COMMAND ----------

import sys

sys.path.append("../common")
from llm import get_llm  # noqa: E402
from databricks.vector_search.client import VectorSearchClient  # noqa: E402

llm = get_llm()
vsc = VectorSearchClient()
index = vsc.get_index(endpoint_name="sample-vs-endpoint", index_name="main.update_repos_sample.policy_index")

# Vector search and model call without error handling (IO-002). The index and
# its endpoint do not exist in the workspace (REF-001).
docs = index.similarity_search(query_text="refund policy", columns=["text"], num_results=3)
answer = llm.invoke(f"Answer from these extracts: {docs}")

# COMMAND ----------

import mlflow.deployments  # noqa: E402

client = mlflow.deployments.get_deploy_client("databricks")
ENDPOINT = "sample-shipping-endpoint"  # not served in the workspace (REF-001)
reply = client.predict(endpoint=ENDPOINT, inputs={"messages": [{"role": "user", "content": "hello"}]})

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ai_query('databricks-meta-llama-3-3-70b-instruct', concat('Summarize: ', text)) AS summary
# MAGIC FROM main.update_repos_sample.policies
