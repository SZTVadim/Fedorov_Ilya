from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)


def animal_sound(animal):
    # Полиморфизм: у Dog и Cat один метод make_sound, но работает он по разному
    animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")

animals = [dog1, dog2, cat1]

for animal in animals:
    zoo.add_animal(animal)

print(zoo.get_animals_count())

for animal in animals:
    animal_sound(animal)

# animal = Animal()
# Объект Animal создать нельзя, потому что make_sound является абстрактным методом
