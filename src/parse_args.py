import argparse

from src.reports.register_reports import register


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
    known, unknown = p.parse_known_args(argv)

    if unknown:
        print(f"[WARN] Ignoring unknown args: {' '.join(unknown)}")

    return known
