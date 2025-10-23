from src.script import register_reports


def test_register_reports_structure():
    reg = register_reports.register
    assert "average-rating" in reg
    assert callable(reg["average-rating"]["func"])
    assert reg["average-rating"]["headers"] == ["brand", "rating"]
