from collections import defaultdict


def average_rating(rows):
    sums = defaultdict(float)
    counts = defaultdict(int)
    for row in rows:
        brand = row["brand"]
        rating = float(row["rating"])
        sums[brand] += rating
        counts[brand] += 1

    result = [(brand, round(sums[brand] / counts[brand], 3)) for brand in sums]

    result.sort(key=lambda x: x[1], reverse=True)

    return result
