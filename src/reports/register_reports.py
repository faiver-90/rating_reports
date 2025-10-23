from src.reports.type_reports.average_rating import average_rating

register = {"average-rating": {"func": average_rating, "headers": ["brand", "rating"]}}
