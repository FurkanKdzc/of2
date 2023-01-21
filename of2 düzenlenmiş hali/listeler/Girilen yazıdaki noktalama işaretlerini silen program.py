a = str(input("Bir cümle giriniz = "))
liste = [".",",","!","?","'"]
b = " "

for i in a:
    if i==liste[0] or i==liste[1] or i==liste[2] or i==liste[3] or i==liste[4]:
        continue
    else:
        b+=i

print(b)