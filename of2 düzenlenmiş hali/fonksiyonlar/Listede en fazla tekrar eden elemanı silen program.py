a=[2,3,4,3,3,2,3]
tekrarsayisi=[0,0,0,0,0,0,0]

#TEKRAR SAYISINI BULMA !
for i in range(len(a)):
    eleman=a[i]
    c=0

    for j in range(len(a)):
        if eleman==a[j]:
            c+=1
        tekrarsayisi[i]=c

#MAKSİMUM SAYIYI BULMA !
mak=a[0]
for i in range(1,len(a)):
    if mak<a[i]:
        mak=a[i]
print(mak)

#DİZİDEN ELEMAN SİLME !
print("Dizinin ilk hali = ", a)

for i in range(len(a)-1,-1,-1):
    if tekrarsayisi[i]==mak:
        del a[i]

print("Dizinin son hali = ", a)