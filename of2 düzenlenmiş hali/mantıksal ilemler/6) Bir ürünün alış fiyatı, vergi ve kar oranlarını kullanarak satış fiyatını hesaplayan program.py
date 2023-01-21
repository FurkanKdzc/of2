alısfiyat = int(input("Ürünün fiyatını giriniz = "))
vergioran = int(input("Ürünün vergi oranını giriniz = "))
karoran = int(input("Ürünün kar oranını giriniz = "))

islem = alısfiyat+(alısfiyat*vergioran//100)+(alısfiyat*karoran//100)

print("Satış fiyatı = ", islem)