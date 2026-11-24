"""Dates of the business day, in an explicit time zone."""

from datetime import date, datetime
from zoneinfo import ZoneInfo

BUSINESS_TZ = ZoneInfo("Europe/Paris")


def business_day(at: datetime | None = None) -> date:
    """The business day of a moment, in the business time zone."""
    moment = at.astimezone(BUSINESS_TZ) if at else datetime.now(BUSINESS_TZ)
    return moment.date()
