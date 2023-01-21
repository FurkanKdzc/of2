a = int(input("A sayısını giriniz = "))
b = int(input("B sayısını giriniz = "))
c = int(input("C sayısını giriniz = "))

if a>b and a>c:
    print("A sayısı en büyüktür.")
elif b>a and b>c:
    print("B sayısı en büyüktür.")
else:
    print("C sayısı en büyüktür.")