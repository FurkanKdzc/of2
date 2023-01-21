tarlalarm2=[]
tarlaisimleri=[]

for i in range(6):
    isim=(input("tarla isimleri : "))
    tarlaisimleri.append(isim)
print(tarlaisimleri)
k = int(input("K tarlasının alanı = "))
l = int(input("L tarlasının alanı = "))
n = int(input("N tarlasının alanı = "))
p = int(input("P tarlasının alanı = "))
r = int(input("R tarlasının alanı = "))
s = int(input("S tarlasının alanı = "))

tarlalarm2+=[k, l, n, p, r, s]
print(tarlalarm2)

deponunhacmi = int(input("Deponun hacmi = "))
m2kontrol=2500
tarlaindex = 0

if deponunhacmi>=2500:
    for i in tarlalarm2:
        m2kontrol-=i
        tarlaindex+=1
        if m2kontrol<=0:
            break
print("Tarlanın sırası = ", tarlaindex)
print("Tarlanın ismi = ", tarlaisimleri[tarlaindex-1])