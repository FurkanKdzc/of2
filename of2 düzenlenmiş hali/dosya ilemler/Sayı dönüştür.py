liste1 = []
n=int(input("Sayı adedini giriniz = "))

for i in range(n):
    a = int(input("Sayı = "))
    liste1.append(a)

def teksayıdonustur(n):
    cift=0
    tek=0

    for i in range(len(n)):
        if liste1[i]%2==0:
            cift+=1
            b=liste1[i]
            b+=1
            liste1[i]=b

        else:
            liste1[i]
            tek+=1
        print(liste1[i], end=" ")
    if cift==0:
        print("Çift sayı bulunamadı.")

sonuc=teksayıdonustur(liste1)