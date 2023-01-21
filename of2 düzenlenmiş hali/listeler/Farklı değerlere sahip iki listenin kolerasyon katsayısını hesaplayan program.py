x = [2,3,1,1,3]
y = [5,5,2,2,1]

xtop=ytop=xfarkkaret=yfarkkaret=pay=payda=0

for i in range(5):
    xtop+=x[i]
    ytop+=y[i]

xort = xtop/5
yort = ytop/5

xfark=yfark=carpim=xfarkkare=yfarkkare=[]

for i in range(5):
    xfark.append(x[i] - xort)
    yfark.append(y[i] - yort)
    carpim.append(xfark[i]*yfark[i])
    pay+=carpim[i]

xfarkkare.append(xfark[i]**2)
yfarkkare.append(yfark[i]**2)
xfarkkaret+=xfarkkare[i]
yfarkkaret+=yfarkkare[i]

payda = (xfarkkaret*yfarkkaret)**0.5
r = pay/payda

print(r)