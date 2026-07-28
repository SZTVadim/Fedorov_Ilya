text = "Привет"
number = 42
float_number = 3.14
numbers = [1, 2, 3]

print(type(text))
print(type(number))
print(type(float_number))
print(type(numbers))

text = "python PROGRAMMING"

print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

text = "  Hello World  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

text = "яблоко,банан,апельсин,груша"
fruits = text.split(",")

print(fruits)
print(" | ".join(fruits))

text = "Я изучаю Python. Python - это круто!"

print(text.replace("Python", "Java"))

text = "Python программирование на Python"

print(text.find("Python"))
print(text.count("Python"))
print(text.find("Java"))

print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

text = "Python very good"

print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])

print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
