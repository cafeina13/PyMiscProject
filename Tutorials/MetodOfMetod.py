# def mat_Hesaplama(sayi:int):
#     def kare(x:int):
#         return x ** 2
#     def kok(x:int):
#         return x ** (1/2)
#     def faktoriyel(x:int):
#         tsayi = 1
#         for i in range(1,sayi+1):
#             tsayi *= i
#         return tsayi
#
#     # return f"Girilen sayı:        {sayi}\nSayının Karesi:      {kare(sayi)}\nSayının Karekökü:    {kok(sayi)}\nSayının Faktoriyeli: {faktoriyel(sayi)}"
#
#     karm = kare(sayi)
#     kokm = kok(sayi)
#     fakm = faktoriyel(sayi)
#     return f"Girilen sayı:        {sayi}\nSayının Karesi:      {karm}\nSayının Karekökü:    {kokm}\nSayının Faktoriyeli: {fakm}"
#
# print(mat_Hesaplama(6))
#
# ------------------------------------------------------------------------------
#
# def yopl_capl(*arg):
#     def topla(demet:tuple):
#         toplam = 0
#         for i in demet:
#             toplam += i
#         return toplam
#     def carp(demet:tuple):
#         carpim = 1
#         for i in demet:
#             carpim *= i
#         return carpim
#
#     return f"Girilen sayıların:\n{'-'*18}\nÇarpımı: {carp(arg)}\nToplamı: {topla(arg)}"
#
# print(yopl_capl(1,4,6,7,4,82,4,12,7,4))