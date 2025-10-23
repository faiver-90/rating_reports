from src.script.type_reports import average_rating


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
