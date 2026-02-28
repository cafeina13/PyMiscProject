from functools import reduce
from math import gcd
import random

liste = [2,4,6,9,10]
#
# def toplama(x,y):
#     return x+y
#
# sonuc1 = reduce(toplama, liste)
# sonuc2 = reduce(lambda x,y: x + y, liste)
#
# print(sonuc2)
#
# ekok_al = lambda x,y: int((x*y)/gcd(x,y))
#
# ekok_ = reduce(ekok_al,liste)
# print(ekok_)
#
tas = "Taş"
makas = "Makas"
kagit = "Kağıt"
def tas_maks(x,y):
    kume = {x,y}
    if x == y:
        return x
    elif kume == {tas,makas}:
        return tas
    elif kume == {tas,kagit}:
        return kagit
    elif kume == {kagit,makas}:
        return makas
    else:
        return "wrong input !!"

tkm = [tas,kagit,makas]
def tkm_rnd():
    return tkm[random.randrange(3)]

tas_kagit_makas = [tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),tkm_rnd(),]

oyna = reduce(tas_maks,tas_kagit_makas)
print(oyna)