#1 ocak 1901 - 31 aralık 2000 kaç kez ayın ilk günü pazar olur

from datetime import date

baslangic = date(1901,1,1)
son = date(2000,12,31)

dTarih = date(baslangic.year,baslangic.month,baslangic.day)
sTarih = date(son.year,son.month,1)

sayac = 0
while dTarih <= sTarih:
    if dTarih.weekday() == 6:
        sayac += 1
    if dTarih.month == 12:
        dTarih = date(dTarih.year + 1, 1, 1)
    else:
        dTarih = date(dTarih.year,dTarih.month + 1,1)
print(sayac)