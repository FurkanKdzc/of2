s1 = input("Birinci cümleyi giriniz = ")
s2 = input("İkinci cümleyi giriniz = ")
c = 0

for i in range(len(s1)):
    if s1[i]!=s2[i]:
        c+=1
        break

if c==0:
    print("Cümleler eşit.")
else:
    print("Cümleler eşit değil.")