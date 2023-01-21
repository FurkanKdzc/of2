vize = int(input("Vize notunuzu giriniz = "))
final = int(input("Final notunuzu giriniz ="))

sonuc = (vize*40//100) + (final*60//100)

if sonuc<60:
    print("Kaldınız.")
else:
    print("Geçtiniz.")

print("Sonucunuz = ", sonuc)