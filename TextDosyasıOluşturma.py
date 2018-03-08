fileName = "TextDos."

girdi = input("Yazmak istediğiniz mesaj ..:")

try:
    file = open(fileName, "w")
    file.write(girdi)
    file.close()
    print("[+] Dosya basarili bir sekilde olusturuldu...!")
except:
    print
    ("[!] Hata!")