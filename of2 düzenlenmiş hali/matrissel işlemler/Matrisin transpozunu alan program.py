import random

satir = int(input("Satır sayısını giriniz = "))
sutun = int(input("Sütun sayısını giriniz = "))

m = [[0 for x in range(sutun)] for y in range(satir)]
mt = [[0 for x in range(satir)] for y in range(sutun)]

for i in range(satir):
    for j in range(sutun):
        m[i][j] = int(input("Matris = "))
        mt[j][i] = m[i][j]

print("Matris = ", m)
print("Matrisin transpozu = ", mt)