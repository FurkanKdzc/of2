def fak(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f

N=4
for n in range(N+1):
    #baştaki boşluğu bırakacak
        for t in range(N-n):
            print(end=" ")
    #değerleri yazdır

for r in range(N+1):
    pay = fak(N)
    payda = fak(N-r)*fak(r)
    c = int(pay/payda)
    print(c, end=" ")

print()