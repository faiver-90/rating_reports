from src.reports.type_reports import average_rating


def test_average_rating_computes_correctly():
    rows = [
        {"brand": "apple", "rating": "4.9"},
        {"brand": "apple", "rating": "4.7"},
        {"brand": "samsung", "rating": "4.8"},
        {"brand": "xiaomi", "rating": "4.6"},
        {"brand": "xiaomi", "rating": "4.1"},
    ]
    result = average_rating.average_rating(rows)
    assert result == [
        ("apple", 4.8),
        ("samsung", 4.8),
        ("xiaomi", 4.35),
    ]


def test_average_rating_empty_input():
    assert average_rating.average_rating([]) == []


def test_average_rating_none():
    from src.reports.type_reports.average_rating import average_rating

    assert average_rating(None) is None


def test_average_rating_skips_bad_rows(caplog):
    from src.reports.type_reports.average_rating import average_rating

    caplog.set_level("ERROR")
    rows = [
        {"brand": "a", "rating": "5"},
        {"brand": "b", "rating": "x"},
        {"rating": "4.5"},
    ]
    res = average_rating(rows)
    print(caplog.records)
    assert ("a", 5.0) in res and all("WARN" in r.message for r in caplog.records)
