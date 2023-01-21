def fak(a):
    f=1
    
    for i in range(1,a+1,1):
        f*=i
        return f

x = int(input("x = "))
k = int(input("k = "))
top = 1

for i in range(1,k+1,+1):
    top+=x**i/fak(i)

print(top)