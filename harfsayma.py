_AUTHOR_='Tarık Ünal'
#Harf/Kelime sayma
metin = input("Metni giriniz...:")

aranan_harf = input("Sayılacak harfi/kelimeyi giriniz: ")

sonuc = 0

for harf in metin:
	if aranan_harf == harf:
		sonuc += 1
print(aranan_harf + " harfinden/kelimesinden metinde "  + str(sonuc) + " tane vardır")
