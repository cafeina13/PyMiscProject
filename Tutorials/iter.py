# class Rover:
#     def __init__(self,start:int,end:int,step=1):
#         self.yazilacak = start
#         self.end = end
#         self.step = step
#         self.artar = start < end
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.yazilacak == self.end or (self.artar and self.yazilacak > self.end) or (not self.artar and self.yazilacak < self.end):
#             raise StopIteration
#         yazdir = self.yazilacak
#         if self.artar:
#             self.yazilacak += self.step
#         else:
#             self.yazilacak -= self.step
#         return yazdir
#
#
# for i in Rover(10,78):
#     print(i)

from string import punctuation
class Cumle():
    def __init__(self,cumle:str):
        self.cumle = str(cumle)

    def __iter__(self):
        self.kelimeler = self.cumle.split(" ")
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.kelimeler):
            raise StopIteration
        kelime = self.kelimeler[self.index]
        self.index += 1
        return kelime.capitalize()#.strip(punctuation)

cumlem = "Sevdim seni bir kere başkasını sevemem, deli diyorlar bana desinler değişemem, desinler değişemem"

for i in Cumle(cumlem):
    print(i)