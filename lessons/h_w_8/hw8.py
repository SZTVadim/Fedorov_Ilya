temps = [18, 22, -3, 25, 19, -1, 21]

fahrenheit_temps = [temp * 9 / 5 + 32 for temp in temps]

print(fahrenheit_temps)

users = {
    "ivan": "qwerty",
    "maria": "12345",
    "petr": "admin",
    "anna": "pass",
    "guest": "guest"
}
password_lengths = {
    login: len(password) for login, password in users.items()
}
print(password_lengths)

scores = (10, 7, 0, 9, 8, 5)
increased_scores = tuple(score * 1.1 for score in scores)
print(increased_scores)
