def faktoriyel(x):
    f=1

    for i in range(1,x+1):
        f*=i
    return f

n = int(input("Bir sayı giriniz = "))

for i in range(n+1):
    print(i,"!=", faktoriyel(i))