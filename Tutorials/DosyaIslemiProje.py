Basliklar = []

ListMetodlar = []
for i in dir(list):
    if i[0:2] == '__':
        continue
    ListMetodlar.append(i)
Basliklar.append("List Metodları")

SetMetodlar = []
for i in dir(set):
    if i[0:2] == '__':
        continue
    SetMetodlar.append(i)
Basliklar.append("Set Metodları")

StringMetodlar = []
for i in dir(str):
    if i[0:2] == '__':
        continue
    StringMetodlar.append(i)
Basliklar.append("String Metodları")

DictMetodlari = []
for i in dir(dict):
    if i[0:2] == '__':
        continue
    DictMetodlari.append(i)
Basliklar.append("Dictionary Metodları")


with open("Listeler.txt", 'w', encoding="UTF-8") as l:
    sayac = 0
    for i in Basliklar: #Başlıkları Yazdırma
        l.write(' ' * 30) #Başlıklar sütunlar arası boşluklar
        l.seek((sayac % 5) * 31) #Sütunların olacağı konuma imleci götür
        l.write(i) #Sütun başlığını yaz
        print(i,end='')
        print(' ' * (30 - len(i)),end='')
        sayac += 1 #Kontrolü sağlamak için sayac
    l.write('\n')
    print()

    barak = 1
    satir = 0
    while barak != 0:
        barak = 0
        imlec = l.tell()
        l.write(' ' * 90)

        l.seek(imlec)

        if satir < len(ListMetodlar):
            l.write(ListMetodlar[satir])
            print(ListMetodlar[satir],end='')
            print(' ' * (30 - len(ListMetodlar[satir])),end='')
            barak += 1
        else:
            l.write("-------")
            print("-------",end='')
            print(' ' * 23,end='')


        l.seek(imlec + 30)
        if satir < len(SetMetodlar):
            l.write(SetMetodlar[satir])
            print(SetMetodlar[satir],end='')
            print(' ' * (30 - len(SetMetodlar[satir])),end='')
            barak += 1
        else:
            l.write("-------")
            print("-------",end='')
            print(' ' * 23,end='')

        l.seek(imlec + 60)
        if satir < len(StringMetodlar):
            l.write(StringMetodlar[satir])
            print(StringMetodlar[satir],end='')
            print(' ' * (30 - len(StringMetodlar[satir])),end='')
            barak += 1
        else:
            l.write("-------")
            print("-------",end='')
            print(' ' * 23,end='')

        l.seek(imlec + 90)
        if satir < len(DictMetodlari):
            l.write(DictMetodlari[satir])
            print(DictMetodlari[satir],end='')
            print(' ' * (30 - len(DictMetodlari[satir])),end='')
            barak += 1
        else:
            l.write("-------")
            print("-------",end='')
            print(' ' * 23,end='')

        satir += 1
        l.write('\n')
        print()