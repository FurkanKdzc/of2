cumle = input("Cümlenizi giriniz = ")
k = int(input("Birinci değer giriniz = "))
r = int(input("İkinci değeri giriniz = "))
a = abs(k-r)
kontrol = 0

for i in range(a):
    print(cumle[k])
    k+=1
    if kontrol==a:
        break