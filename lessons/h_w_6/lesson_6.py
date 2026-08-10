"""
Домашнее задание
"""

# ЗАДАНИЕ 1

student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва"
}

print(student.keys())
print(student.values())

for key, value in student.items():
    print(f"{key}: {value}")

for value in student.values():
    print(value)


# ЗАДАНИЕ 2

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

student3 = student1.copy()
student3.update(student2)

student1.update(student2)

print(student1)
print(student2)
print(student3)
