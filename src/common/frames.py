"""Small pandas helpers of the sample, unit-tested in tests/test_frames.py."""

import pandas as pd


def orders_frame(rows: list[dict]) -> pd.DataFrame:
    """Orders as a pandas frame with an upper-case country."""
    frame = pd.DataFrame(rows, columns=["order_id", "country", "amount"])
    frame["country"] = frame["country"].str.upper()
    return frame


def is_text_column(frame: pd.DataFrame, column: str) -> bool:
    """Whether a column holds text, written for pandas 2 (text columns are of dtype object there)."""
    return frame[column].dtype == object
