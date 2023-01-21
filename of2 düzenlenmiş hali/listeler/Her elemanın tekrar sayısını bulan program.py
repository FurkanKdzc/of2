harfler = {}
cumle = str(input("Cümle giriniz : "))

for i in cumle:
    if i in harfler:
        harfler[i]+=1
    else:
        harfler[i]=1

print(harfler)