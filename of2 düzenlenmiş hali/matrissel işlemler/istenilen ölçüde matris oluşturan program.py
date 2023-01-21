m = int(input("Sütun sayısını giriniz = "))
n = int(input("Satır sayısını giriniz = "))

matris = [[0 for i in range(n)] for i in range(m)]

print(m, "x", "'lik matris değeri gireceksiniz = ")

for i in range(m):
    for j in range(n):
        matris[i][j] = int(input("Matris [" + str(i) + "][" + str(j) + "] = "))

print("Matris = ", matris)