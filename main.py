import argparse
import sys

from script.build_final_table import build_final_table
from script.io import read_csv_files
from script.register_reports import register


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
        build_final_table(final_rows, report_headers)


if __name__ == "__main__":
    raise SystemExit(main())
