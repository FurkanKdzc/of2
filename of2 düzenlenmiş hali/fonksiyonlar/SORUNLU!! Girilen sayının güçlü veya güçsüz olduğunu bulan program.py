top = 0
n = int(input("n = "))
yedek = n

while n>0:
    sonbasamak = n%10
    top+=fak(sonbasamak)
    n=n//10

if top==yedek:
    print("Güçlü.")
else:
    print("Güçlü değil.")