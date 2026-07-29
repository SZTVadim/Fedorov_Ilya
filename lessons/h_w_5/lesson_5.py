fruits = ["яблоко"]

fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

print(fruits)

fruits = ["яблоко", "банан", "апельсин", "банан"]

fruits.remove("банан")
deleted_fruit = fruits.pop()

print(fruits)
print(deleted_fruit)

fruits = ["яблоко", "банан", "апельсин", "банан"]

print(fruits.index("банан"))
print(fruits.count("банан"))

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers.sort()
numbers.reverse()

print(numbers)
