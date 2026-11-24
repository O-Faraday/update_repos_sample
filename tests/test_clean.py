from datetime import datetime, timezone

from clean.dates import business_day
from clean.settings import table


def test_table_name():
    assert table("demo", "update_repos_sample", "orders") == "demo.update_repos_sample.orders"


def test_business_day_is_in_paris_time():
    # 23:30 UTC on 1 October is already 2 October in Paris.
    assert str(business_day(datetime(2026, 10, 1, 23, 30, tzinfo=timezone.utc))) == "2026-10-02"
