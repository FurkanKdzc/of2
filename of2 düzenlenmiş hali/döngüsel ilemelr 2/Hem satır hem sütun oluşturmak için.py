sayi = int(input("Lütfen tablo ölçülerini giriniz = "))

for satir in range(1,sayi+1):
    for sutun in range(1,sayi+1):
        deger = satir*sutun
        print(deger, end=" ")

    print()