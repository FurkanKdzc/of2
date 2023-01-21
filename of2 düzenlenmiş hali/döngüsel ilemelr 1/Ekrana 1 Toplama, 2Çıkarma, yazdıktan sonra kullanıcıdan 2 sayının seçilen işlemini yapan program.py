print("1 = Toplama")
print("2 = Çıkarma")
print("3 = Çarpma")
print("4 = Bölme")

sayi1 = int(input("1. Sayıyı giriniz ="))
sayi2 = int(input("2. Sayıyı giriniz ="))
islem = int(input("İşlem seçiniz = "))

if islem == 1:
    print("Cevap = ", sayi1+sayi2)
elif islem == 2:
    print("Cevap = ", sayi1-sayi2)
elif islem == 3:
    print("Cevap = ", sayi1*sayi2)
elif islem == 4:
    print("Cevap = ", sayi1/sayi2)