_auther_='Tarık Ünal'
s = input('Lütfen bir tam sayı giriniz..:')
try:
    if int(s)>=0:
        print("Yazdığınız sayıya kadar olan tek sayılar:")
        for i in range(int(s),0,-1):
            if i%2 != 0:
                print(i)
        print("__________")
except:
    print("Lütfen bir sayı giriniz...:")
