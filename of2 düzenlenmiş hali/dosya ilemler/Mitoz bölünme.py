yh1=0
yh2=0
n=int(input("n : "))
dakika=float(input("Dakikayı giriniz = "))

if dakika>=1:
    for x in range(1,dakika+1):
        yh1=(2*n)-n
        yh2=yh1-(yh1*20)/100
        n=n+yh2
    print(n)
else:
    print("Bölünme yok.")