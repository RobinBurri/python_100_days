import os
print("Current working directory:", os.getcwd())


# file = open("text.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

# mode="r"; mode="w"; mode="a"; default is "r"
with open("text.txt", mode="r", encoding="utf-8") as file:
    content = file.read()
    print(content)
