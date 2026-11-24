from common.pricing import amount_band, discount, normalize_country, with_vat


def test_with_vat():
    assert with_vat(10) == 12.0


def test_discount():
    assert discount(100) == 90.0
    assert discount(100, rate=0.25) == 75.0


def test_amount_band():
    assert [amount_band(a) for a in (10, 120, 500)] == ["small", "medium", "large"]


def test_normalize_country_trims_spaces():
    # Fails on purpose: the known bug of normalize_country (spaces kept). The rewrite does not fix it,
    # so the evaluation must class it "failing before and after", not as a regression.
    assert normalize_country(" fr ") == "FR"
