# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!
# 9 - 10 задание в работе 
# если код , то этот код еще находится в работе 
credit by karpblch

# задание 8
dict = dict(
    name = 'Ilya',
    age = 18,
    city = "Moscow"
) # Словарь
dict["age"] = 10 # Измение в ключе age значение (18 -> 10)
dict.update({"email":"ilya@example.ru"}) # Добавление в словаря ключа email с его значение ilya@example.ru
mdict.pop('city') # Удаление из словаря ключа city и его значения Moscow
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
