_auther_='Tarık Ünal'
faktoriyel=1

while True:
    sayi=input("Pozitif bir sayı giriniz....")
    if (int(sayi) < 0):
        print("Yanlış bilgi girişi yaptınız....")
    else:
        for i in range(1,int(sayi)+1):
            faktoriyel=faktoriyel*i

        print("Faktröiyel sonucu =",faktoriyel)
        break

