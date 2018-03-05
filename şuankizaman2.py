_auther_='Tarık Ünal'

"""
    Zaman göstereç
"""

import time

zaman = time.localtime()
yil = zaman[0]
ay = zaman[1]
gun = zaman[2]
saat = zaman[3]
dakika = zaman[4]
saniye = zaman[5]

print("""
    Tarih: {}/{}/{}
    Saat : {}:{}:{}
    """.format(gun, ay, yil, saat, dakika, saniye))