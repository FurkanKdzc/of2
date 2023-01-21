cumle = input("Cümle giriniz = ")
bosluksayac = 0
rakam = ["0","1","2","3","4","5","6","7","8","9"]
rakamsayac = 0

for i in (cumle):
    if i == " ":
        bosluksayac+=1
    if i in rakam:
        rakamsayac+=1

print("Boşluk sayısı = ", bosluksayac)
print("Kelime sayısı = ", bosluksayac+1)
print("Harf sayısı = ", len(cumle)-(bosluksayac+rakamsayac))
print("Rakam sayısı = ", rakamsayac)