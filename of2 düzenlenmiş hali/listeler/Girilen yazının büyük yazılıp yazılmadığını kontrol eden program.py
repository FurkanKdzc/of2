cumle = input("Cümle giriniz = ")
buyuk = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]

for i in (cumle):
    if i in (buyuk):
        print("Cümle büyük yazılmıştır.")
        break
    else:
        print("Cümle küçük yazılmıştır.")
        break