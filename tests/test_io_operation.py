from src.reports.io_operation import read_csv_files

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


def test_read_csv_files_warns_on_missing(tmp_path):
    result = read_csv_files([str(tmp_path / "missing.csv")])
    assert result == []


def test_read_csv_bad_encoding(tmp_path, caplog):
    from src.reports.io_operation import read_csv_files

    p = tmp_path / "bad.csv"
    p.write_bytes(b"\xff\xfe\x00\x00")  # ломаем UTF-8
    caplog.set_level("ERROR")
    rows = read_csv_files([str(p)])
    assert rows == []
    assert "Bad encoding" in caplog.text


def test_read_csv_bad_format(tmp_path, caplog):
    from src.reports.io_operation import read_csv_files

    p = tmp_path / "bad.csv"
    p.write_text('name,brand\nval1\n"unclosed', encoding="utf-8")
    caplog.set_level("ERROR")
    rows = read_csv_files([str(p)])
    assert rows == []
    assert "Bad CSV" in caplog.text


def test_read_csv_custom_delimiter(tmp_path):
    from src.reports.io_operation import read_csv_files

    p = tmp_path / "s.csv"
    p.write_text("name;brand;rating\nx;apple;5\n", encoding="utf-8")
    rows = read_csv_files([str(p)], delimiter=";")
    assert rows[0]["brand"] == "apple"
