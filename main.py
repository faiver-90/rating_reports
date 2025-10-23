import sys

import tabulate

from src.parse_args import parse_args
from src.reports.io import read_csv_files
from src.reports.register_reports import register


def main(argv: list[str] | None = None) -> int:
    try:
        ns = parse_args(argv or sys.argv[1:])
        if not ns.files:
            print("[ERROR] no input files", file=sys.stderr)
            return 2

        meta = register.get(ns.report)
        if not meta or "func" not in meta or "headers" not in meta:
            print(f"[ERROR] report '{ns.report}' is misconfigured", file=sys.stderr)
            return 2

        rows = read_csv_files(ns.files)
        if not rows:
            print("[WARN] no data rows after reading CSVs", file=sys.stderr)

        try:
            final_rows = meta["func"](rows)
        except KeyboardInterrupt:
            print("[ERROR] interrupted", file=sys.stderr)
            return 130
        except Exception as e:
            print(f"[ERROR] report '{ns.report}' failed: {e}", file=sys.stderr)
            return 1

        if final_rows:
            print(
                tabulate.tabulate(
                    final_rows, headers=meta["headers"], tablefmt="github"
                )
            )
        else:
            print("[INFO] nothing to print", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"[ERROR] unexpected: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
