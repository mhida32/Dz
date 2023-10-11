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
