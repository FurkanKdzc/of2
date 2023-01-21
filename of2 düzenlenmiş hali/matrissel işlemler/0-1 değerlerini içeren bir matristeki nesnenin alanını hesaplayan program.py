x = [[0,1,1,0,1],
     [0,0,1,0,1],
     [1,0,1,1,0],
     [0,1,0,1,1],
     [1,0,1,1,0]]

kontrol = 1
ilkkenar = 0

for i in range(len(x)):
    if kontrol==i:
        break
    for j in range(len(x[0])):
        ilkkenar+=x[i][j]

print(ilkkenar)

kontrol = 1
solkenar = 0

for i in range(len(x[0])):
    if kontrol==i:
        break
    for j in range(len(x)):
        solkenar+=(x[j][i])

print(solkenar)

kontrol = 0
altkenar = 0

for i in range(len(x)):
    kontrol+=1

    for j in range(len(x[0])):
        if kontrol==len(x):
            altkenar+=x[i][j]

print(altkenar)

kontrol = 0
sagkenar = 0

for i in range(len(x)):
    kontrol+=1
    
    for j in range(len(x[0])):
        if kontrol==1:
            sagkenar+=x[j][len(x)-1]

        break

print(sagkenar)