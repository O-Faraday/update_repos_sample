# Silver orders, with the legacy dlt module.
import dlt
from pyspark.sql import functions as F


@dlt.table(comment="Orders with a normalised country")
def silver_orders():
    return dlt.read_stream("orders_bronze").withColumn("country", F.upper(F.trim("country")))
