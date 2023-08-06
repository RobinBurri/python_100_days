numbers = [1, 2, 3]
new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

#  => => => => =>
new_list = [n + 1 for n in numbers]
# <new_list> = [<new_item> for <each_item> in <list we are going to interate over>]
# <new_list> = [<new_item> for <each_item> in <list we are going to interate over> if <condition>]


print(new_list)

names = ["John", "Jane", "Jo", "Jack", "Jill", "Mary", "Mike"]
m_names = [n for n in names if n[0] == "M"]

print(m_names)
