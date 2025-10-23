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

def save_csv_files(path: Path, rows: list[tuple], headers: list[str], encoding="utf-8"):
    path.parent.mkdir(parents=True, exist_ok=True)
    print(rows, headers)
    with path.open("w", encoding=encoding, newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Файл сохранён: {path.resolve()}")