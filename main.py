import argparse
import sys

import tabulate

from src.script.io import read_csv_files
from src.script.register_reports import register


def parse_args(argv: list[str]) -> argparse.Namespace:
    reports_list = "\n".join(f"  {name}" for name in register.items())

    p = argparse.ArgumentParser(
        prog="ratings",
        description=(
            "Агрегация рейтингов и формирование отчётов из CSV.\n"
            "Доступные отчеты:\n"
            f"{reports_list}"
        ),
    )
    p.add_argument("--files", nargs="+", required=True, help="Пути к CSV-файлам.")
    p.add_argument(
        "--report",
        required=True,
        choices=list(register.keys()),
        help="Название отчёта.",
    )

    return p.parse_args(argv)


def main(argv: list[str] | None = None):
    ns = parse_args(argv or sys.argv[1:])
    report_worker = register.get(ns.report)["func"]
    report_headers = register.get(ns.report)["headers"]
    rows = read_csv_files(ns.files)
    final_rows = report_worker(rows)

    if final_rows:
        print(tabulate.tabulate(final_rows, headers=report_headers, tablefmt="github"))


if __name__ == "__main__":
    raise SystemExit(main())
