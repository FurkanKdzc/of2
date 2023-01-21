x = [[1,2,3],
     [2,3,4],
     [4,6,7],
     [2,1,5]]

indexbulma = 0
index = 9
sayi = 10

for i in range(len(x)):
    for j in range(len(x[0])):
        
        if(indexbulma==index):
            x[i][j] = sayi
            break
        else:
            indexbulma+=1

print(x)