#Bir üçgenin açıları
#Bu program üçgenin ilk iki açısını girdiğinizde
#size üçüncü açıyı verir
#ilk iki açıyı almak için input() değişkenini kullanır

açı1 = input("Üçgenin ilk açısı lütfen\t:")

if int(açı1) < 0 :
 print("Hata açı '-' değerinde olamaz")
 exit()
#program hata verdiği için çıkış komutu veriyoruz
if int(açı1) > 180 :
 print("Hata açı 180 değerinden büyük olamaz")
 exit()
if int(açı1) == 180 :
 print("Hata açı 180 değerinde olamaz")
 exit()

açı2 = input("Üçgenin ikinci açısı lütfen\t:")

if int(açı2) < 0 :
 print("Hata açı '-' değerinde olamaz")
 exit()
açılartoplamı = 180
if int(açı2) > 180 :
 print("Hata açı 180 değerinden büyük olamaz")
 exit()
if int(açı2) == 180 :
 print("Hata açı 180 değerinde olamaz")
 exit()
açı3=açılartoplamı-int(açı1)-int(açı2)

print("Üçgenin birinci açısı\t:",açı1,"derece değerinde")
print("Üçgenin ikinci açısı\t:",açı2,"derece değerinde ise")
print("Bu üçgenin üçüncü açısı\t:",açı3,"derece değerindedir",sep=" ")