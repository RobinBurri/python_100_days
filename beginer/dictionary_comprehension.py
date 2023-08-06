import random

names = ["John", "Jane", "Jo", "Jack", "Jill", "Mary", "Mike"]

# students_scores = {new_key:new_value for item in list}

students_scores = {student: random.randint(1, 100) for student in names}

print(students_scores.items())

passed_students = {
    student: score for (student, score) in students_scores.items() if score >= 60
}


print(passed_students)
