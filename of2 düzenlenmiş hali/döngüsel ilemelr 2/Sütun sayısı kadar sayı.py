sutun = int(input("Sütun sayını giriniz = "))

for k in range(sutun,0-1,-1):
    print()
    for j in range(k):
        print(k,end="")
    continue

for k in range(1,sutun+1,+1):
    for satir in range(k):
        print(k, end="")
    print()