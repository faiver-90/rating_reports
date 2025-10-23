from src.reports.io import read_csv_files

CSV_SAMPLE = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
"""


def test_read_csv_files_reads_rows(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(CSV_SAMPLE, encoding="utf-8")
    result = read_csv_files([str(csv_file)])
    assert len(result) == 2
    assert result[0]["brand"] == "apple"
    assert result[1]["rating"] == "4.8"


def test_read_csv_files_warns_on_missing(tmp_path, capsys):
    result = read_csv_files([str(tmp_path / "missing.csv")])
    captured = capsys.readouterr()
    assert "[WARN]" in captured.err
    assert result == []
