ikiliksayi = " "
sayi = int(input("Bir sayı giriniz = "))

while sayi!=0:
    ikiliksayi = str(sayi%2)+ikiliksayi
    sayi=sayi//2

print(ikiliksayi)