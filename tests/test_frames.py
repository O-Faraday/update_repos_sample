from common.frames import is_text_column, orders_frame


def test_orders_frame_cleans_the_country():
    frame = orders_frame([{"order_id": 1, "country": " fr", "amount": 10.0}])
    assert frame["country"].tolist() == ["FR"]


def test_country_is_text():
    frame = orders_frame([{"order_id": 1, "country": "fr", "amount": 10.0}])
    assert is_text_column(frame, "country")
