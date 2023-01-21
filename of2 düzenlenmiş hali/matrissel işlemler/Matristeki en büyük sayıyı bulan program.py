def matrismax(m):
    maxdeger = None

    for satir in m:
        for deger in satir:
            if maxdeger is None:
                maxdeger = deger
            elif maxdeger<deger:
                maxdeger = deger
    return maxdeger

m1 = [[2,3,4,5],
      [-2,-9,3,1],
      [2,8,75,3],
      [1,2,3,4]]

print(matrismax(m1))