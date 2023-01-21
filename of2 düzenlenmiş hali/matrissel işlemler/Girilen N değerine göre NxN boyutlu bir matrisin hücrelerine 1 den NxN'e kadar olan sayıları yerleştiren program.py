n = int(input("Matris boyu = "))

a = [[0 for i in range(n)] for i in range(n)]

b = 0

for i in range(len(a)):
    for j in range(len(a)):
        b = b+1
        a[i][j] = b

for i in a:
    print(i)