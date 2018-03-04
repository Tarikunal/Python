#04.03.18
_auther_='Tarık Ünal'


kaynak="şçöğüıŞÇÖĞÜİ"
hedef="scoguiSCOGUI"

çeviri_tablosu=str.maketrans(kaynak,hedef)

metin=input("Bir metin girin: ")

print(metin.translate(çeviri_tablosu))
