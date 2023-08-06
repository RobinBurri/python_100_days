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


# names = []
# letter_content = ""

# with open("../Names/names_list.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for name in lines:
#         names.append(name.strip())

# with open("../Letter/starting_letter.txt", "r", encoding="utf-8") as f:
#     letter_content = f.read()

# for name in names:
#     with open(f"../readyToSend/letter_{name}.txt", "w", encoding="utf-8") as f:
#         f.write(letter_content.replace("[name]", name))