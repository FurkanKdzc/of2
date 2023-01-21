def sayiAsalmi(p):
    k=1

    for i in range(2,p):
        if p%i==0:
            k=0
            break
    return k

print(sayiAsalmi(10))

n = int(input("N = "))
c = 0
sayi = 1

while n>c:
    if sayiAsalmi(sayi)==1:
        c+=1
        print(sayi)
    sayi=sayi+1