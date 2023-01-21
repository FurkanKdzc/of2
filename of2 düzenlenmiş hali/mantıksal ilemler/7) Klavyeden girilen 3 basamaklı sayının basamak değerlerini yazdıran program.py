sayi = int(input("Sayıyı giriniz = "))

while sayi>0:
    sonbasamak=sayi%10
    sayi=sayi//10

    print(sonbasamak)