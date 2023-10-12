#готовые дз только здесь. 
# Позже везде пропишу комментарии

# дз номер 9
my_dict = dict(name = '',age = 0, city = "")
my_dict["name"] = input("Как тебя зовут?")
my_dict["age"] = input("Сколько тебе лет?")
my_dict["city"] = input("Откуда ты?")
print(my_dict)



# дз номер 8
list = (4,5,6)
print(list)
print(f'Первое число: {list[0]}')
print(f'Второе число: {list[1]}')
print(f'третье число: {list[2]}')
for i in list:
    print(f'{list}')
print(f'Сумма: {sum(list)}')


# дз номер 7
n = int(input("Введите целое число: "))
i = 0
while i <= n:
    print(i)
    i += 1
print(f"i-{i},pot-{n}")



# дз номер 6
klava = int(input("Введи чисто от 1 до 10: "))
if klava % 3 == 0:
    print(f"Число делится на 3")
elif klava > 10:
    print("Число больше 10")
else:
    print("Число не соответствует условиям")


# дз номер 5
list = [1,2,"хуй",'хуй2', True, False,5,"tt",7,9]
print(list[1:10:2])
print(list[0:5])

# дз номер 4
name = input("Как тебя зовут?")
vozrast = int(input("Сколько вам лет?:"))
if vozrast >= 18:
	print(f"Вы совершеннолетний")
else:
	print(f"Вы не совершеннолетний")
print(name.isalpha())
if name.isalpha() == True:
	print(f"Введите имя!")
else:
	print(f"Привет, {name}")


# дз номер 3
age = int(input(f"Привет,сколько тебе лет?")) #Ввод возраста
support = input("С вами есть сопровождающий?(да/нет): ") #Ввод cопровождающего
if age < 12: # Если возраст меньше 12 лет
	print(f"Билет бесплатный!") # Вывод
elif 12 <= age <= 18: # Если возраст больше или равен 12 лет и меньше или равен  18 годам просит указать сопровождающего 
	if support.lower() == 'да': # Cопровождающий есть
		print( f"Билет со скидкой!") # Вывод
	elif support.lower() == 'нет': # Сопровождающего нет
		print(f"Полная стоимость билета!") # Вывод
	else:
		print(f"Ошибка: Надо было указать да/нет, а не {support}") # Вывод ошибки если пользователь решит ввести другие значения кроме да/нет
else:
	print(f"Полная стоимость билета!")
