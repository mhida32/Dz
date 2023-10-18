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
        print("error")
else:
	print("error")
