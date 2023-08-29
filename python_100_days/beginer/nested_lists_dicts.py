# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

# Nesting Dictionary in a List
travel_log1 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]


def add_new_country(country_visited: str, city_visited: list, total_visits: int):
    """Add a new country to the travel_log."""
    travel_log1.append(
        {
            "country": country_visited,
            "cities_visited": city_visited,
            "total_visits": total_visits,
        }
    )


add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)

print(travel_log1)
