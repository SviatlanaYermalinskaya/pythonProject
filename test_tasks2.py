# test tasks 2
#task1
#Создать папку, перейти в нее, создать там пайтон-файл, который будет выводить в консоль ваше имя.
from abc import ABC, abstractmethod
import os
import random

my_folder = "Folder"+str(random.randint(100,999))
os.mkdir(my_folder)
os.chdir(my_folder)
with open("sv.py", "w+", encoding="utf-8") as f:
    f.write("print('Sviatlana')")

#task2
#Напишите декоратор и примените его один раз к функции с вашим именем
# и два раза к функции с вашей фамилией. Вызвать декорируемые функции.

def decor(fn):
    def wrapper():
        print("Start decor")
        fn()
        print("End decor")
    return wrapper

@decor
def sveta():
    print("Sveta")

@decor
@decor
def yermalinskaya():
    print("Yermalinskaya")

sveta()
yermalinskaya()

#task3
#Напишите абстрактный класс с двумя методами. Напишите второй класс,
# сделайте его наследником от первого, реализуйте все методы класса-родителя
# и добавьте еще статический метод.
# Создайте экземпляр второго класса и запустите все созданные методы.

class AClass(ABC):

    @abstractmethod
    def print_name(self):
        pass

    @abstractmethod
    def print_surname(self):
        pass

class MyName(AClass):

    def print_name(self):
        print("Sviatlana")

    def print_surname(self):
        print("Yermalinskaya")

    @staticmethod
    def print_class():
        print(MyName.__name__)

my_class = MyName()
my_class.print_name()
my_class.print_surname()
my_class.print_class()
MyName.print_class()


#task4
class OddIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 2
            return self.counter - 1
        else:
            raise StopIteration

for i in OddIterator(5):
    print(i)
