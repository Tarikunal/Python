#!/usr/bin/env python
#-*-coding:utf-8-*-
from tkinter import *
ana = Tk()
def islem():
   cek = giris.get()
   print (cek)
   yaz = Label(ana,text='Yazı : '+cek).pack()
giris = Entry()
giris.pack()
bas = Button(ana,text='Bas',command=islem).pack()
cikis =Button(ana,text='Çıkış',command=ana.destroy).pack()
ana.mainloop()
