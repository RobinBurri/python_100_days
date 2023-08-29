import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

for key, value in student_dict.items():
    pass


student_data_frame = pandas.DataFrame(student_dict)

for index, row in student_data_frame.iterrows():
    pass


data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Eneter a word: ").upper()
    try:
        new_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_word)


generate_phonetic()
