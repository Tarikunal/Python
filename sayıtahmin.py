_author_='Tarık Ünal' #24.02.17
from random import randint

rand = randint(1, 200)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 200 arasında değer girin (0 çıkış):"))
    if (sayi == 0):
        print("Program kapatılıyor!!!")
        break
    elif sayi < rand:
        print("Yükselt.")
        continue
    elif sayi > rand:
        print("Düşür.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
