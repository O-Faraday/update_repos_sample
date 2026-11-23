"""The policy agent, logged as an MLflow model from code by agent_driver (synthetic)."""

import mlflow
from databricks_langchain import ChatDatabricks

# The endpoint is in the YAML configuration, read when the model loads: the
# agent cannot know it statically.
config = mlflow.models.ModelConfig(development_config="agent_config.yaml")
llm = ChatDatabricks(endpoint=config.get("llm_endpoint"), temperature=0)


def answer(question: str) -> str:
    # Model call without timeout or error handling (IO-002).
    return llm.invoke(question).content


mlflow.models.set_model(answer)
