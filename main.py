import logging
import sys

import tabulate

from src.log_conf import setup_logger
from src.parse_args import parse_args
from src.reports.io import read_csv_files
from src.reports.register_reports import register

setup_logger()
logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    try:
        ns = parse_args(argv or sys.argv[1:])

        if not ns.files:
            logger.error("[ERROR] no input files")
            return 2

        meta = register.get(ns.report)
        if not meta or "func" not in meta or "headers" not in meta:
            logger.error(f"[ERROR] report '{ns.report}' is misconfigured")
            return 2

        rows = read_csv_files(ns.files)
        if not rows:
            logger.error("[WARN] no data rows after reading CSVs")

        try:
            final_rows = meta["func"](rows)
        except KeyboardInterrupt:
            logger.error("[ERROR] interrupted")
            return 130
        except Exception as e:
            logger.error(f"[ERROR] report '{ns.report}' failed: {e}")
            return 1

        if final_rows:
            print(
                tabulate.tabulate(
                    final_rows, headers=meta["headers"], tablefmt="github"
                )
            )
        else:
            logger.error("[INFO] nothing to print")
        return 0
    except Exception as e:
        logger.error(f"[ERROR] unexpected: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
