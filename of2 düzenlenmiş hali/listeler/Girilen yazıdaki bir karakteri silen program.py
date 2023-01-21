cumle = input("Cümleyi giriniz : ")
yenisi = ''
silinen = input("Silinecek karakter = ")

for i in cumle:
    if i==silinen:
        continue
    else:
        yenisi+=i

print(yenisi)