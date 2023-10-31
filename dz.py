# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!

credit by karpblch
# 10 задание 
# 1 часть(Вторая часть скоро будет)
from tkinter import *
import random

definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных."
}

def show_random_definition():
    global definitions
    a = random.choice(list(definitions.keys()))
    definition_text['text'] = definitions.get(a)
     
win = Tk()
win.geometry('600x600')
win.title('Определения Python')
definition_text = Label(win,text="Вывод")
definition_text.pack()
baton = Button(win,text="Показать определение",command=show_random_definition)
baton.pack()

win.mainloop() # удержание окна

credit by karpblch

# 9 задание
# 1 часть
from tkinter import *

def massage():
    lb["text"] = pole.get()
    winn = Tk()
    winn.geometry('500x500')
    winn.title('Задание 9.1')
    lb1 = Label(winn,text=pole.get())
    lb1.grid(column=1,row=1)


win = Tk()
win.geometry('500x500')
win.title('Задание 9')

pole = Entry(win)
pole.grid(column=1,row=1)

lb = Label(win,text="Вывод")
lb.grid(column=1,row=2)

baton = Button(win,text="Нажми",command=massage)
baton.grid(column=1,row=3)

win.mainloop() # удержание окна

credit by karpblch

# 2 часть
from tkinter import *

def massage():
    winn = Tk()
    winn.geometry('500x500')
    winn.title('Задание 9.1')
    lb1 = Label(winn,text=pole.get())
    lb1.grid(column=1,row=1)

def clear_lb():
    pole.delete(0,END)
    

win = Tk()
win.geometry('500x500')
win.title('Задание 9')

pole = Entry(win)
pole.grid(column=1,row=1)

# lb = Label(win,text="Вывод")
# lb.grid(column=1,row=2)

baton = Button(win,text="Нажми",command=massage)
baton.grid(column=1,row=3)

сlear = Button(win,text="Удаление",command=clear_lb)
сlear.grid(column=2,row=1)



win.mainloop() # удержание окна


credit by karpblch

# задание 8
dict = dict(
    name = 'Ilya',
    age = 18,
    city = "Moscow"
) # Словарь
dict["age"] = 10 # Измение в ключе age значение (18 -> 10)
dict.update({"email":"ilya@example.ru"}) # Добавление в словаря ключа email с его значение ilya@example.ru
dict.pop('city') # Удаление из словаря ключа city и его значения Moscow
for key, velua in dict.items(): # Цикл на вывод словаря
    print(f"Ключ: {key}, Значение: {velua}")# Вывод словаря
credit by karpblch


# задание 7
list = (4,5,6)
print(list)
print(f'Первое число: {list[0]}')
print(f'Второе число: {list[1]}')
print(f'третье число: {list[2]}')
print(f'Сумма: {sum(list)}')


credit by karpblch

# задание 6
# часть 1
n = int(input("Введите целое число: "))
for i in range(n+1):
    print(i)
    i += 1
credit by karpblch
# часть 2
n = int(input("Введите целое число: "))
i = 0
while i <= n:
    print(i)
    i += 1

credit by karpblch


 # задание 5
klava = int(input("Введи чисто от 1 до 10: "))
if klava % 3 == 0 and klava <= 10:
    print(f"Число делится на 3")
elif enter % 3 != 0 and enter <= 10:
    print(f"Число не делится на 3")
elif klava > 10:
    print("Число больше 10")
else:
    print("Число не соответствует условиям")

credit by karpblch

list = [1,2,"еей",'еее', True, False,5,"tt",7,9]
print(list[1:10:2])
print(list[0:5])
list[0] = True # Изменяет  0 объект списка 
list[7] = 99 # Изменяет  7 объект списка  
list[1] = False # Изменяет  1 объект списка  
print(list) # Вывод измененного списка
credit by karpblch
