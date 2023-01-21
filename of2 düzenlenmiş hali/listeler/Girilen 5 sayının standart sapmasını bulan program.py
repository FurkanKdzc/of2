a = 0
toplam = 0
liste = list()

while a<5:
    sayi=int(input("Sayı giriniz = "))
    liste.append(sayi)
    toplam+=sayi
    a+=1

karetoplam = 0
ort = toplam//5

for i in liste:
    result = ort-i
    karet = result**2
    karetoplam+=karet

sonuc = (karetoplam/4)**0.5

print(sonuc)