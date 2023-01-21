yazi = input("Yazı giriniz : ")
aranan = input("Aranan kelimeyi giriniz : ")
c = " "

for x in range(len(yazi)):
    if yazi[x:x+len(aranan)]==aranan:
        c+=yazi[0:x]
        c+=" ' "+aranan+" ' "
        c+=yazi[x+len(aranan):len(yazi)]

print(c)