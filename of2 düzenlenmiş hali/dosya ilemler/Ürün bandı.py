def yaz(saniye):
    saat = saniye//3600
    kalansaniye = saniye-saat*3600
    dakika = kalansaniye//60
    kalansaniye = kalansaniye-dakika*60

    print(saat, ":", dakika, ":", kalansaniye)

t= int(input("Paket sayısını giriniz = "))
k = 12
l = 15
saniye = 0
paket = 0

while paket<t:
    c=0

    if saniye%k==0:
        paket+=1
        c+=1
    if saniye%l==0:
        paket+=1
        c+=1
    if c==2:
        yaz(saniye)
    saniye+=1