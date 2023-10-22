# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!
# 9 - 10 задание в работе 
# если код , то этот код еще находится в работе 
credit by karpblch

# from tkinter import *
# from tkinter.ttk import Combobox
credit by karpblch

# def clicked():
#     res = "Привет {}".format(txt.get())
#     lbl.configure(text=res)
credit by karpblch

# window = Tk()
# window.title("Добро пожаловать в приложение PythonRu")
# window.geometry('400x250')
# lbl = Label(window, text="Привет")
# lbl.grid(column=0, row=0)
# txt = Entry(window, width=10)
# txt.grid(column=1, row=0)
# btn = Button(window, text="Клик!", command=clicked)
# btn.grid(column=2, row=0)
# combo = Combobox(window)
# combo['values'] = (1, 2, 3, 4, 5, "Текст")
# combo.current(1)  # установите вариант по умолчанию
# combo.grid(column=0, row=1)
# window.mainloop()
# window.mainloop()
credit by karpblch



# задание 8
my_dict = dict(name = '',age = 0, city = "")
my_dict["name"] = input("Как тебя зовут?")
my_dict["age"] = input("Сколько тебе лет?")
my_dict["city"] = input("Откуда ты?")
print(my_dict)

credit by karpblch


# задание 7
list = (4,5,6)
print(list)
print(f'Первое число: {list[0]}')
print(f'Второе число: {list[1]}')
print(f'третье число: {list[2]}')
for i in list:
    print(f'{list}')
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
