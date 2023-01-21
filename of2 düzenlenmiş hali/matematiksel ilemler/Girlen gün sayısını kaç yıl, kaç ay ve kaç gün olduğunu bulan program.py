gun = int(input("Gün sayısını giriniz = "))
yil = gun//365
ay = gun//30
guns = gun%365

print("Girilen değer", yil, "yıl", ay, "ay", guns, "gündür.")