def fak(n):
    if n==0:
        return 1
    return n*fak(n-1)

n = int(input("n = "))

sonuc = fak(n)

print(sonuc)