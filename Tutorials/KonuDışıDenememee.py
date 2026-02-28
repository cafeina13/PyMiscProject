def rakamlar(sayi1):
    return len(set(str(sayi1))) == len(str(sayi1))

def rakamlar_2_sayi(sayi1,sayi2):
    return len(set(str(sayi1) + str(sayi2))) == len(str(sayi1) + str(sayi2))

def rakamlar_3_sayi(sayi1,sayi2,sayi3):
    return len(set(str(sayi1) + str(sayi2) + str(sayi3))) == 10


sayilar = [i for i in range(100,1000) if rakamlar(i)]
sayilar2 = []

sayac = 0
for i in sayilar:
    for j in sayilar:
        if rakamlar_2_sayi(i,j):
            sayi3 = i + j
            if rakamlar_3_sayi(i,j,sayi3):
                sayilar2.append((i,j,sayi3))
                sayac += 1
for i in sayilar2:
    print(i)
print(sayac)
