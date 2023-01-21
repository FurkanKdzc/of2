m = [[1,2,3],[4,5,6],[7,8,9]]
n = [[0,1,2],[3,4,-6],[5,6,7]]

k = list()

m_satirsayisi = len(m)
m_sutunsayisi = len(n)

for satir in range(m_satirsayisi):
    k_satir = list()
    for sutun in range(m_sutunsayisi):
        m_sayi = m[satir][sutun]
        n_sayi = n[satir][sutun]

        toplam = m_sayi+n_sayi

        k_satir.append(toplam)

    k.append(k_satir)

print(k)