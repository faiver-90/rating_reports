import logging
from collections import defaultdict

logger = logging.getLogger(__name__)


def average_rating(rows: list[dict[str, str]]) -> list[tuple] | None:
    if rows is None:
        return None

    sums: dict[str, float] = defaultdict(float)
    counts: dict[str, int] = defaultdict(int)

    for idx, row in enumerate(rows, 1):
        try:
            brand = row["brand"]
            rating = float(row["rating"])
        except KeyError as e:
            logger.warning(f"Missing key {e} at row {idx}")
            continue
        except (TypeError, ValueError):
            logger.warning(f"Bad rating at row {idx}: {row.get('rating')!r}")
            continue

        sums[brand] += rating
        counts[brand] += 1

    result = [(brand, round(sums[brand] / counts[brand], 3)) for brand in sums]
    result.sort(key=lambda x: x[1], reverse=True)

    return result
