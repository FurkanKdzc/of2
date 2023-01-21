import random

m = int(input("Sütun sayısını giriniz = "))
n = int(input("Satır sayısını giriniz = "))

matris = [[random.randint(0,9) for i in range(m)] for i in range(n)]

print(matris)

top = 0

for i in range(m):
    for j in range(n):
        if n==m:
            if i==j:
                top+=matris[i][j]

print(top)