from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=0)
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=1)
window.mainloop()
window.mainloop()






# my_dict = dict(name = '',age = 0, city = "")
# my_dict["name"] = input("Как тебя зовут?")
# my_dict["age"] = input("Сколько тебе лет?")
# my_dict["city"] = input("Откуда ты?")
# print(my_dict)





# list = (4,5,6)
# print(list)
# print(f'Первое число: {list[0]}')
# print(f'Второе число: {list[1]}')
# print(f'третье число: {list[2]}')
# for i in list:
#     print(f'{list}')
# print(f'Сумма: {sum(list)}')





# n = int(input("Введите целое число: "))
# i = 0
# while i <= n:
#     print(i)
#     i += 1
# print(f"i-{i},pot-{n}")










# klava = int(input("Введи чисто от 1 до 10: "))
# if klava % 3 == 0:
#     print(f"Число делится на 3")
# elif klava > 10:
#     print("Число больше 10")
# else:
#     print("Число не соответствует условиям")



# list = [1,2,"хуй",'хуй2', True, False,5,"tt",7,9]
# print(list[1:10:2])
# print(list[0:5])
