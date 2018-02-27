from tkinter import *

pencere = Tk()
pencere.title("Basit KDV Hesaplama Programı")
pencere.resizable(False, False)
pencere.wm_attributes("-toolwindow", 1)
pencere.geometry("350x160")
pencere.wm_attributes("-alpha", 0.9)
pencere.wm_attributes("-topmost", 1)

etiket = Label(text="""KDV Değeri;""", compound="center", fg="green")
etiket.pack()

fiyat = input("Ürün Fiyatı: ")
fiyat = int(fiyat)
deger = int(18)
deger2 = int(100)
sonuc = (fiyat * deger / deger2)
hesap = Label(text=sonuc, fg="red", bg="white")
hesap.pack()

etiket = Label(text="""Toplam Fiyat;""", compound="center", fg="green")
etiket.pack()

sonuc2 = (sonuc + fiyat)
hesap2 = Label(text=sonuc2, fg="red", bg="white")
hesap2.pack()

etiket = Label(text="""KDV Hariç Fiyat;""", compound="center", fg="green")
etiket.pack()

hesap3 = Label(text=fiyat, fg="red", bg="white")
hesap3.pack()

mainloop()