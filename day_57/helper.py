import requests


def find_genders(name: str):
    base_url = f"https://api.genderize.io?name={name}"
    r = requests.get(base_url, timeout=5)
    r.raise_for_status()
    data = r.json()
    return data.get("gender")


def find_ages(name: str):
    base_url = f"https://api.agify.io?name={name}"
    r = requests.get(base_url, timeout=5)
    r.raise_for_status()
    data = r.json()
    return data.get("age")
