# вариант 1
from math import sqrt, pi

print("Длины сторон треугольника:") 
a = input("a = ")
b = input("b = ")
c = input("c = ")
if  a.isdigit() == True and  b.isdigit() == True and c.isdigit()== True:
    af = float(a)
    bf = float(b)
    cf = float(c)
    if af > 0 and bf>0 and cf>0 and af + bf > cf or af+cf >bf or bf+cf>af:
        p = (af + bf + cf) / 2
        s = sqrt(p * (p - af) * (p - bf) * (p - cf))
        print("Площадь: %.2f" % s)
    else:
        print("Ошибка: Введеные числа не соответствуют условию или Введеные числа < 0")
else:
	print("Ошибка: Введите число")
# вариант 2
from math import sqrt, pi
def geon():
    if a > 0 and b>0 and c >0 and a + b > c or a + c > b or b +c > a:
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print("Площадь: %.2f" % s)
    else:
        print("Replay")
while True:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        geon()
        break
    except:
        print("Ошибка: Введите число")
