import csv
import logging
from collections.abc import Iterable
from pathlib import Path

logger = logging.getLogger(__name__)


def _open_text(p: Path, mode: str = "r", encoding="utf-8"):
    return p.open(mode, encoding=encoding, newline="")


def read_csv_files(files: Iterable[str], delimiter: str = ","):
    rows: list[dict] = []
    for f_name in files:
        path = Path(f_name)
        if not path.exists():
            logger.error(f"File not found: {path}")
            continue
        try:
            with _open_text(path, "r", "utf-8") as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                for row in reader:
                    if not row:
                        continue
                    rows.append(row)
        except FileNotFoundError:
            logger.error(f"File not found: {path}")
        except PermissionError as e:
            logger.error(f"No permission {path}: {e}")
        except UnicodeDecodeError as e:
            logger.error(f"Bad encoding {path}: {e}")
        except csv.Error as e:
            logger.error(f"Bad CSV {path}: {e}")

    return rows
