# FileNotFoundError (the file doesn't exist)

try:
    file = open("file.txt", encoding="utf-8")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not_exist"])
except FileNotFoundError:
    file = open("file.txt", "w", encoding="utf-8")
    file.write("Hello World")
except KeyError as error_message:
    print(f"KeyError: {error_message}")

else:
    content = file.read()
    print(content)
finally:
    file.close()  # type: ignore
