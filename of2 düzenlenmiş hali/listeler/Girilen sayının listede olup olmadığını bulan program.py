x = []
eleman = int(input("Listede kaç eleman olsun = "))
a = int(input("Aradığınız değeri girinzi = "))

for i in range(eleman):
    x.append(int(input("Sayıları yazınız = ")))
    x+=[i]

for i in x:
    if i==a:
        print(a,"Listede")
        break
    else:
        print(a,"Listede değil")