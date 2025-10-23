import main


def test_parse_args_includes_registered_reports(capsys):
    try:
        main.parse_args(["--help"])
    except SystemExit:
        out = capsys.readouterr().out
        assert "average-rating" in out


def test_main_executes_with_mocked_funcs(tmp_path, capsys):
    csv_path = tmp_path / "a.csv"
    csv_path.write_text(
        "name,brand,price,rating\niphone,apple,1000,5\n", encoding="utf-8"
    )

    rc = main.main(["--report", "average-rating", "--files", str(csv_path)])
    assert rc is None or rc == 0
    output = capsys.readouterr().out
    assert "apple" in output
