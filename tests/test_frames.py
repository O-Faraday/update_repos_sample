from common.frames import is_text_column, orders_frame


def test_orders_frame_upper_cases_the_country():
    frame = orders_frame([{"order_id": 1, "country": "fr", "amount": 10.0}])
    assert frame["country"].tolist() == ["FR"]


def test_country_is_text():
    # Passes with pandas 2; pandas 3 stores text as the str dtype, so this test regresses when step 6b
    # upgrades pandas from 2 to 3 without adapting is_text_column (the code model adapts it; the test
    # stays as it is).
    frame = orders_frame([{"order_id": 1, "country": "fr", "amount": 10.0}])
    assert is_text_column(frame, "country")
