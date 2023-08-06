people = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Paris"},
    {"name": "Jo", "age": 35, "city": "London"},
]

# This is the idea
# def f(person):
#     return person["name"]
# people.sort(key=f)

# short way (lambda)
people.sort(key=lambda person: person["name"])

print(people)
