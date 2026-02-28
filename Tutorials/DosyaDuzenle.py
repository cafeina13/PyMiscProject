from os import chdir,listdir,path as tpath,mkdir,rename,getcwd, rmdir, stat
import time as t

def hSDznl(yol:str,klasorKlasoru:str = "MainFolder",dosyaKlasoru:str="FileFolder"): #Klasör ve dosya düzenleme fonksiyonlarını çağırır
    sayacK = kDnl(yol,klasorKlasoru)
    sayacD = dDnl(yol,dosyaKlasoru)
    return sayacD,sayacK

def kDnl(yol:str,anaKlasorAdi:str= "MainFolder"): #Klasör düzenler
    cwd = getcwd()                                #Düzenlenecek yolu alır, default haricinde ana klasör adı alır
    chdir(yol)                                    #Kaç klasör yer değiştirildi bilgisini döndürür
    sayac = 0
    for i in listdir():
        if tpath.isdir(i):
            dirKlasor = anaKlasorAdi
            if not tpath.exists(dirKlasor):
                mkdir(dirKlasor)
            rename(i, tpath.join(dirKlasor, i))
            sayac += 1
    chdir(cwd)
    return sayac

def dDnl(yol:str,anaKlasorAdi:str="FileFolder"): #Dosyaları Düzenler
    cwd = getcwd()                               #Düzenlenecek yolu alır, default haricinde Dosya klasörü adını alır
    chdir(yol)                                   #Kaç dosya yer değiştirildi bilgisini döndürür
    sayac = 0
    for i in listdir():
        if tpath.isfile(i):
            klasor = tpath.splitext(i)[1].replace(".", "")
            if klasor == '' or i.startswith('.'):
                continue
            aKlasor = tpath.join(anaKlasorAdi, klasor)
            if not tpath.exists(anaKlasorAdi):
                mkdir(anaKlasorAdi)
            if not tpath.exists(aKlasor):
                mkdir(aKlasor)
            rename(i, tpath.join(aKlasor, i))
            sayac += 1
    chdir(cwd)
    return sayac
"""__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---"""

def tarih_sirala_klasor2(yol:str): #ana klasörün içine onun içindeki klasörlerin içindeki öğeleri tarihe göre kategorize eder
    cwd = getcwd()
    chdir(yol)
    anaKlasor = listdir(yol)
    sayac = 0
    for i in anaKlasor:
        if tpath.isdir(i):
            chdir(tpath.join(yol,i))
            gezelienKlasor = listdir()
            for j in gezelienKlasor:
                degistirmeTarihiTuple = t.localtime(stat(j)[8])
                dTarihiSTR = t.strftime("%d %B %Y %A, %H.%M", degistirmeTarihiTuple)
                klasor = tpath.join(yol,dTarihiSTR)
                yeniYol = tpath.join(klasor,j)
                if not tpath.exists(klasor):
                    mkdir(klasor)
                sayac += 1
                rename(j,yeniYol)
            chdir(yol)
    chdir(cwd)
    return sayac

def tarihSiralaDosya(yol:str):#ana klasör içindeki öğeleri tarihe göre kategorize eder
    cwd = getcwd()
    chdir(yol)
    anaKlasor = listdir(yol)
    sayac = 0
    for i in anaKlasor:
        if tpath.isfile(i):
            degistirmeTarihiTuple = t.localtime(stat(i)[8])
            dTarihiSTR = t.strftime("%d %B %Y %A, %H.%M", degistirmeTarihiTuple)
            klasor = tpath.join(yol,dTarihiSTR)
            yeniYol = tpath.join(klasor,i)
            if not tpath.exists(klasor):
                mkdir(klasor)
            sayac += 1
            rename(i, yeniYol)
    chdir(cwd)
    return sayac


def dosyaCikar(yol:str):#bir klasörün içindeki klasörlerdeki öğeleri bir üst dizine çıkarır
    cwd = getcwd()
    chdir(yol)
    anaKlasor = listdir()
    sayac = 0
    for i in anaKlasor:
        if tpath.isdir(i):
            chdir(tpath.join(yol,i))
            gezelienKlasor = listdir()
            for j in gezelienKlasor:
                yeniYol = tpath.join(yol,j)
                sayac += 1
                rename(j,yeniYol)
            chdir(yol)
    chdir(cwd)
    return sayac

def bosKlasorSil(yol:str):#bir klasördeki içi boş klasörleri siler
    cwd = getcwd()
    chdir(yol)
    sayac = 0
    for i in listdir(yol):
        if tpath.isdir(i) and len(listdir(i)) == 0:
            rmdir(i)
            sayac += 1
    chdir(cwd)
    return sayac