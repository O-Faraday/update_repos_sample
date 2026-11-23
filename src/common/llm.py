"""The chat model of the sample, built here and used in other files."""

from databricks_langchain import ChatDatabricks

from config import CHAT_ENDPOINT


def get_llm():
    # The endpoint is named in another file: reading one file at a time, the
    # agent cannot tell which model a caller of get_llm() reaches.
    return ChatDatabricks(endpoint=CHAT_ENDPOINT, temperature=0)
