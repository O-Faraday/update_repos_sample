from common.frames import is_text_column, orders_frame


def test_orders_frame_cleans_the_country():
    frame = orders_frame([{"order_id": 1, "country": " fr", "amount": 10.0}])
    assert frame["country"].tolist() == ["FR"]


def test_country_is_text():
    # Passes with pandas 2. pandas 3 stores text as the str dtype, so this test fails when step 6
    # upgrades pandas from 2 to 3 without adapting is_text_column. The code model adapts it (6b);
    # the test stays as it is, and step 6c checks it still passes.
    frame = orders_frame([{"order_id": 1, "country": "fr", "amount": 10.0}])
    assert is_text_column(frame, "country")
