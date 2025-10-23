import logging
from pathlib import Path


def setup_logger():
    Path("logs").mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    fh = logging.FileHandler("logs/app.log", mode="a", encoding="utf-8")
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
