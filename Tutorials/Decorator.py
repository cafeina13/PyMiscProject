import time
# def zaman_hesapla(fonk):
#     def wrapper(*args,**kwargs):
#         bas = time.time()
#         fonk(*args,**kwargs)
#         son = time.time()
#         print(f"{son-bas} saniye sürdü!")
#     return wrapper
#
# @zaman_hesapla
# def bekle(sure:int):
#     time.sleep(sure)
#
# # bekle(1)
# zaman_hesapla(bekle)(1)

# ------------------------------------------------

def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):
        basla = time.time()
        sonuc = fonk(*args,**kwargs)
        time.sleep(0.13)
        son = time.time()
        print(f"{son-basla} saniye sürdü!!")
        return sonuc
    return wrapper

@zaman_hesapla
def kare_al(liste:list):
    sonuc = []
    for i in liste:
        sonuc.append(i ** 2)
    return sonuc

@zaman_hesapla
def kup_al(liste:list):
    sonuc = []
    for i in liste:
        sonuc.append(i ** 3)
    return sonuc

@zaman_hesapla
def topla(*args):
    # return sum(args)
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

@zaman_hesapla
def bilgiler(**kwargs):
    for anahtar, deger in kwargs:
        print(f"{anahtar} : { deger}")

bilgiler(isim="Ali",yas=35, sehir="Isparta")

# print(f"{kup_al(list(range(750)))}")