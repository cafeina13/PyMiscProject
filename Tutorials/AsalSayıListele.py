#ilk 10000 asal sayının kaç tanesi 3 ile başlar 7 ile biter ?


#-------------------İlk önce 10 000 asal listelenmeli-------------------------------------#
import math

asalList = list()  # asallar için liste oluşturuluyor
asalList.append(2) # 2 hatalı davrandığı için manuel ekleniyor

j = 3                        #normal taranmaya 3 den başlanıyor
while len(asalList) < 10000: #asal liste eleman sayısı 10000 oluncaya kadar devam edecek
    asal = True              #tersi kanıtlanıncaya kadar her sayı asaldır
    for k in range(3,math.isqrt(j) + 1,2): # 3 den başlayıp sayının karekökünün 1 fazlasına çift sayıları atlayarak
        if j % k == 0:   #bölen varmı
            asal = False # varsa asal değil
            break        # döngüyü kır
    if asal:               #sayının asal olmadığı kanıtlanmadıysa
        asalList.append(j) # listeye ekle
    j += 2 #sonraki tek sayıdan devam et


#-----------------------İlk 10 000 asal listelendi--------------------------------------#
#---------------Şimdi aranan asalların sayısını bulabiliriz-----------------------------#

tane = 0           #sayaç oluşturuldu
for i in asalList: #listede gez
    if str(i)[0] == '3' and str(i)[-1] == '7': #başı 3 sonu 7 olan sayı bulununca
        tane += 1                              # sayacı arttır
print(tane) #sayacı yazdır