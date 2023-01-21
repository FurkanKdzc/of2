m = int(input("Sütun sayısını giriniz = "))
n = int(input("Satır sayısını giriniz = "))

matris = [[0 for i in range(n)] for j in range(m)]

print(m, "x", n, "'lik matris değeri gireceksiniz = ")

sutuntop = []

for i in range(m):
    top = 0
    for j in range(n):
        matris[i][j] = int(input("Matris[" + str(i) + "][" + str(j) + "]"))
        top+=matris[i][j]
    sutuntop.append(top)

print("Matris = ", matris)
print("Sütun toplamı = ", sutuntop)

satirtop = []

for j in range(n):
    top1 = 0
    for i in range(m):
        top1+=matris[i][j]
    satirtop.append(top1)

print("Matris = ", matris)
print("Satır toplamı = ", satirtop)