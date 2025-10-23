import sys
from collections import defaultdict


def average_rating(rows):
    if rows is None:
        return None

    sums = defaultdict(float)
    counts = defaultdict(int)


    for idx, row in enumerate(rows, 1):
        try:
            brand = row["brand"]
            rating = float(row["rating"])
        except KeyError as e:
            print(f"[WARN] missing key {e} at row {idx}", file=sys.stderr)
            continue
        except (TypeError, ValueError):
            print(f"[WARN] bad rating at row {idx}: {row.get('rating')!r}", file=sys.stderr)
            continue

        sums[brand] += rating
        counts[brand] += 1

    result = [(brand, round(sums[brand] / counts[brand], 3)) for brand in sums]
    result.sort(key=lambda x: x[1], reverse=True)

    return result
