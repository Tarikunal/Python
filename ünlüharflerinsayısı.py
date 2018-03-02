_auther_='Tarık Ünal'
#Girilen metindeki ünlü harf sayısını veren fonksiyon
s = input("Metni giriniz...:")
sesli_harf = 'aeıioöuüAEIİUÜOÖ'
sayac = 0
for i in s:
    if i in sesli_harf:
        sayac += 1
print("--%s-- metnindeki sesli harf sayisi:%d" % (s,sayac))
