import math

print("Çizgiye ait katsayıları giriniz = ")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("Daireye ait katsayıları giriniz = ")
x = int(input("x = "))
y = int(input("y = "))
r = int(input("r = "))

d = abs(a*x+b*y+c) /math.sqrt(a*2+b*2)
print("Nokta uzaklığı = ", d, "Yarıçap = ", r)