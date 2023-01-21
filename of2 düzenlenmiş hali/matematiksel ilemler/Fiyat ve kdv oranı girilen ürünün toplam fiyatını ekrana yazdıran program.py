fiyat = int(input("Ürünün fiyatını giriniz = "))
kdv = int(input("Ürünün KDV oranını giriniz = "))

sonuc = fiyat+(fiyat*kdv//100)

print("Toplam fiyat = ", sonuc)