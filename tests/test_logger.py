def test_setup_logger_creates_file_and_no_duplicates(tmp_path, monkeypatch):
    from src import log_conf

    monkeypatch.chdir(tmp_path)
    log_conf.setup_logger()
    log_conf.setup_logger()

    p = tmp_path / "logs" / "app.log"
    assert p.exists()

    import logging

    root = logging.getLogger()
    assert len(root.handlers) == 2
