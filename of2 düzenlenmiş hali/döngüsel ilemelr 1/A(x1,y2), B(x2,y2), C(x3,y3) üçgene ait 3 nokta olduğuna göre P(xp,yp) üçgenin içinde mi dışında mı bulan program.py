print("Üçgen")

x1 = float(input("Birinci apsis = "))
x2 = float(input("İkinci apsis = "))
x3 = float(input("Üçüncü apsis = "))
x4 = float(input("Dördüncü apsis = "))

if x1+x2>x4:
    print("Apsis üçgen içinde.")
elif x1+x3>x4:
    print("Apsis üçgen içinde.")
elif x2+x3>x4:
    print("Apsis üçgen içinde.")
else:
    print("Apsis üçgen içinde değil!")

y1=float(input("Birinci ordinat = "))
y2=float(input("İkinci ordinat = "))
y3=float(input("Üçüncü ordinat = "))
y4=float(input("Dördüncü ordinat = "))

if y1+y2>y3:
    print("Ordinat üçgen içinde.")
elif y1+y3>y4:
    print("Ordinat üçgen içinde.")
elif y2+y3>y4:
    print("Ordinat üçgen içinde.")
else:
    print("Ordinat üçgen içinde değil!")

print("İki sistemden biri üçgen dışındaysa (x,4y4) noktası üçgen dışındadır.")