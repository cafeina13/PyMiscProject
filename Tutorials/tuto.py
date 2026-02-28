metodlar = []
for i in dir(list):
    if i[0:2] == '__':
        continue
    metodlar.append(i)