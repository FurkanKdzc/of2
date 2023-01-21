def alan(x,n):
    m=0
    uzunkenar=x+2

    for i in range(n):
        alan=x*uzunkenar
        m+=alan
        uzunkenar+=2
    return m

n = int(input("N sayısını giriniz = "))
x = int(input("X sayısını giriniz = "))
hesapla=alan(x,n)

print("Alan = ", hesapla)