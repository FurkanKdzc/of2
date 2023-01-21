x=[]
sayi = int(input("Kaç sayı gireceksiniz = "))

for i in range(sayi):
    eleman = int(input("Sayıları giriniz ="))
    x+=[eleman]
    print("Sıralı değil : ", x)

for i in range(0,(sayi)-1):
    if x[i+1]>x[i]:
        a=x[i+1]
        x[i] = x[i+1]
        x[i] = a

print("Sıralı : ", x)