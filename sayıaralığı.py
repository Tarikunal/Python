#06.03.2018
_author_='Tarık Ünal'
#Girilen iki sayı arasındaki sayıları yazdıran fonksiyon

num1=int(input("Başlangıç sayısını girin: "))
num2=int(input("Bitiş sayısını girin: "))
num3=int(input("Artışı girin: "))

liste=[x for x in range(num1,num2) if x % num3 == 0]

print(liste)
