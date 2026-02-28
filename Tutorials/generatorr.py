from itertools import count
import sys

infinite_list = (x for x in count())

k = 0
for i in infinite_list:
    k += 1
    print( i)
    if k == 50:
        break