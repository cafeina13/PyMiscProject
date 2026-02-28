# class Rex:
#
#     def __init__(self,end):
#         self.end = end
#
#     def __repr__(self):
#         nova = ''
#         for i in self.evoker():
#             nova += str(i) + " - "
#         return nova.strip("- ")
#
#     def evoker(self):
#         for i in range(self.end):
#             yield i
#
# holiday = Rex(6)
#
# print(holiday)
#
#
# def sayi_uret(maks:int):
#         return (i for i in range(maks,1,-1))
#
# rex = sayi_uret(8)
#
# for j in rex:
#     print(j)


from itertools import count

def infinite_castle_prime():
    yield 2
    prime_cache = [2]
    for i in count(3 , 2):
        is_prime = True
        for cp in prime_cache:
            if i % cp == 0:
                is_prime = False

        if is_prime:
            prime_cache.append(i)
            yield i


for p in infinite_castle_prime():
    print(p)
    if p >= 100:
        break