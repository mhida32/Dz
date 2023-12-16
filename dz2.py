# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!
credit by karpblch

# Задание 1

car = {'марка':'','модель': '','год': ''}
car.update({'цвет': ' '})
print(car.get('марка'))
fruits = (" "," ")
print(fruits[])
numbers = (" "," ")
print(numbers[])

credit by karpblch

# Задание 2
credit by karpblch

lst = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]

for row in lst:
    print(' '.join(map(str, row)))

credit by karpblch

# Задание 3 (Может изменится)
credit by karpblch

class Car:
    '''Машина'''
    def __init__(self, make:str, model:str, year:int) -> None:
        '''Информация о машине'''
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        '''Вывод информации о машине'''
        print(f"Марка машины: {self.make}\nМодель машины: {self.model}\nГод машины: {self.year}")
        

переменная = Car(Сюда написать марку машины , модель и год)
переменная.display_info()

credit by karpblch

# Задание 4
credit by karpblch
class Animal:
    def __init__(self,name, species) -> None:
        self.name = name
        self.species = species 


    def make_sound(self): 
        print("Текст")

class Dog(Animal): 
    def make_sound(self): 
        print("Текст")
    
class Cat(Animal): # подкласс Cat
    def make_sound(self):
        print("Текст")

animal = Animal("Текст","Текст")
animal.make_sound()
dog = Dog("Текст","Текст")
dog.make_sound()
cat = Cat("Текст","Текст")
cat.make_sound()
credit by karpblch

# Задание 5
credit by karpblch
with open('sample.txt','w',encoding='utf-8') as f: 
    f.write("Текст") 
with open('sample.txt','r',encoding='utf-8') as f:
    print(f.read()) 
credit by karpblch

# Задание 6
credit by karpblch
pass
credit by karpblch

# Задание 7
credit by karpblch
pass
credit by karpblch

# Задание 8
credit by karpblch
pass
credit by karpblch

# Задание 9
credit by karpblch
pass
credit by karpblch
