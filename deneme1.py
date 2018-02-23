_author_='Tarik Unal'

while True:
    print("Kitap Okumak (1)")
    print("Müzik Dinlemek (2)")
    print("Film İzlemek (3)")
    print("Bilgisayar Oyunu (4)")
    print("Gitar Çalmak (5)")
    print("Yemek Yemek (6)")
    print("Ders Çalışmak (7)")
    print("---------")
    print
    secim=input("Yapmak istediğiniz aktivite numarasını giriniz...:")
    isim=input("Isminiz :")

    if secim =="1":
        print("Kitap okumak isteyen", isim ,"101 numaralı kitap odasına gidebilir.")
        print
    elif secim =="2":
        print("Müzik dinlemek isteyen", isim ,"102 numaralı müzik odasına gidebilir.")
        print
    elif secim =="3":
        print("Film izlemek isteyen", isim ,"103 numaralı film odasına gidebilir.")
        print
    elif secim =="4":
        print("Bilgisayar oyunu oynamak isteyen", isim ,"104 numaralı bilgisayar odasına gidebilir.")
        print
    elif secim =="5" :
        print("Gitar çalmak isteyen", isim ,"105 numaralı müzik odasına gidebilir.")
        print
    elif secim =="6" :
        print("Yemek yemek isteyen",isim ,"106 numaralı yemek odasına gidebilir.")
        print
    elif secim =="7" :
        print("Ders çalışmak isteyen", isim ,"107 numaralı çalışma odasına gidebilir.")
        print
    else:
        print("Aktivite numarası geçersizdir. Program sonlandırılıyor...")
        break


