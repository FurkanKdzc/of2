maas = int(input("Maaşınızı giriniz = "))
cocuksayisi = int(input("Çocuk sayısını giriniz = "))

islem1 = maas+(maas*5//100)
islem2 = maas+(maas*10//100)
islem3 = maas+(maas*15//100)

if cocuksayisi==1:
    print(islem1)
elif cocuksayisi==2:
    print(islem2)
elif cocuksayisi>=3:
    print(islem3)