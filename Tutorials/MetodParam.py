import random

# def topla(sayi1:int,sayi2:int):
#   return sayi1 + sayi2
#
# def carp(sayi1:int,sayi2:int):
#   return sayi1 * sayi2
#
#
# def Hesap(method:callable,sayi1:int,sayi2:int):
#   return method(sayi1,sayi2)
#
#
# print(f"{Hesap(carp,4,8)}")

def kareal(sayi:int):
    return sayi ** 2

def cruel_angel(sayi:int):
    a = random.randrange(3)
    if a == 0:
        return sayi ** 0
    elif a == 1:
        return sayi ** 1
    else:
        return sayi * 0

def metod_sec(metod:callable,liste:list):
    sonuc = list()
    for i in liste:
        sonuc.append(metod(i))
    return sonuc

listem = [4,8,3,13,2,7,9,12,17]
print(f"Listem: {listem}\nSonuç: {metod_sec(cruel_angel,listem)}")