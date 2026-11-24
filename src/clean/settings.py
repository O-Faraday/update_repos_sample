"""Names of the clean pipeline, taken from job parameters with safe defaults."""

DEFAULT_CATALOG = "demo"
DEFAULT_SCHEMA = "update_repos_sample"


def table(catalog: str, schema: str, name: str) -> str:
    """Three-level name of a table of the project."""
    return f"{catalog}.{schema}.{name}"
