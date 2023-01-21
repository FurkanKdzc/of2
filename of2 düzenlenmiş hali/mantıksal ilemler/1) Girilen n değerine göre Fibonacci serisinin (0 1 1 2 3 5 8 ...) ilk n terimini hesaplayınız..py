deger1 = 0
deger2 = 1
sayac = 2

n = int(input("Bir 'n' değeri giriniz = "))

print(deger1, deger2, end=" ")

while sayac<=n:
    deger3=deger1+deger2
    print(deger3, end=" ")

    deger1=deger2
    deger2=deger3
    sayac+=1