#03.03.18
_author_='Tarık Ünal'
s = input('Lütfen bir tam sayı yazınız..:\n')
try:
    if int(s)>=0:
        print("Yazdığınız sayıya kadar olan çift sayılar:")
        for i in range(int(s)):
            if i % 2 == 0:
                print(i)
        print("__________")
except:
        print("LÜtfen bir tam sayı yazınız")
