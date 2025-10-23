import csv
import sys
from collections.abc import Iterable
from pathlib import Path


def _open_text(p: Path, mode: str = "r", encoding="utf-8"):
    return p.open(mode, encoding=encoding, newline="")


def read_csv_files(files: Iterable[str], delimiter: str = ","):
    value = []
    for f_name in files:
        path = Path(f_name)
        if not path.exists():
            print(f"[WARN] file not found: {path}", file=sys.stderr)
            continue
        with _open_text(path, "r", "utf-8") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row in reader:
                value.append(row)
    return value
