# Databricks notebook source
# MAGIC %md
# MAGIC # Send the daily summary to a partner (clean)

# COMMAND ----------

# Written to Databricks guidance: nothing here should be reported.
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

PARTNER_URL = "https://partner.example.invalid/api/summary"
token = dbutils.secrets.get(scope="partners", key="summary-api-token")

session = requests.Session()
session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=2,
                                                        status_forcelist=[429, 500, 502, 503, 504])))

# COMMAND ----------

summary = {"day": "2026-10-01", "orders": 8}
try:
    response = session.post(PARTNER_URL, json=summary, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    response.raise_for_status()
except requests.RequestException as exc:
    raise RuntimeError(f"partner summary not sent: {exc}") from exc
