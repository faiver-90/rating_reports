import csv
import sys
from collections.abc import Iterable
from pathlib import Path


def _open_text(p: Path, mode: str = "r", encoding="utf-8"):
    return p.open(mode, encoding=encoding, newline="")


def read_csv_files(files: Iterable[str], delimiter: str = ","):
    rows: list[dict] = []

    for f_name in files:
        path = Path(f_name)
        if not path.exists():
            print(f"[WARN] file not found: {path}", file=sys.stderr)
            continue
        try:
            with _open_text(path, "r", "utf-8") as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                for row in reader:
                    if not row:
                        continue
                    rows.append(row)
        except FileNotFoundError:
            print(f"[WARN] file not found: {path}", file=sys.stderr)
        except PermissionError as e:
            print(f"[WARN] no permission {path}: {e}", file=sys.stderr)
        except UnicodeDecodeError as e:
            print(f"[WARN] bad encoding {path}: {e}", file=sys.stderr)
        except csv.Error as e:
            print(f"[WARN] bad CSV {path}: {e}", file=sys.stderr)

    return rows
