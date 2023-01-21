yazi = input("Cümleyi giriniz = ")
kelime = input("Aranan kelimeniz = ")

if kelime in yazi:
    for i in range(len(yazi)):
        if yazi[0+i:len(kelime)+i] == kelime:
            a = yazi[0:i] + yazi[i+len(kelime)::]
            print(a)
else:
    print("Kelime yazıda yok!")