class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book1 = Book("Дюна", "Фрэнк Герберт", 700)
book2 = Book("Пикник на обочине", "Стругацкие", 200)
book3 = Book("Метро 2033", "Дмитрий Глуховский", 500)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Илья")

account.deposit(1000)
account.withdraw(500)
account.withdraw(1000)

print(account.get_balance())
