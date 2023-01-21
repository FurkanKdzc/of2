print("A(m,n) Boyutlarını giriniz = ")

m = int(input("Satır sayısı = "))
n = int(input("Sütun sayısı = "))

print("B(f,p) Boturlarını giriniz = ")

f = int(input("Satır sayısı = "))
p = int(input("Sütun sayısı = "))

if n!=f:
    print("Matrisler çarpılamaz.")
else: 
    A = [[0 for i in range(n)] for i in range(m)]
    B = [[0 for i in range(p)] for i in range(f)]
    C = [[0 for i in range(p)] for i in range(m)]

    print("A matrisini giriniz = ")

    for i in range(m):
        for j in range(n):
            print('A[{}][{}]'.format(i+1, j+1))
            A[i][j] = int(input("Sayı = "))

    print("B matrisini giriniz = ")

    for i in range(f):
        for j in range(p):
            print('B[{}][{}]'.format(i+1, j+1))
            B[i][j] = int(input("Sayı = "))
        
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]

print(C)