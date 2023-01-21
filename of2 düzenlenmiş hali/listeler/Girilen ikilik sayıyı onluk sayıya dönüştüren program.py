s = 0
i = 0
basamak = 0

sayi = int(input("Lütfen ikilik sayıyı giriniz = "))

while (sayi> 0):
    basamak = int((sayi%2) * pow(10, i))
    i+= 1
    sayi = sayi//2
    s = s + basamak

print(s)