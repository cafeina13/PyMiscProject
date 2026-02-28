# abc + def = knmp olan sayıları bul (ortak rakamı olmayan 3 basamaklı 2 sayının toplamı yine toplananlarla ortak olmayacak)


sayilar = []
for i in range(100,1000): # 3 basamaklı sayılar arasında
    str_i = str(i)
    f,s,t = str_i
    if f != s and f != t and s != t: # rakamları birbirinden farklı
        sayilar.append(i)            # sayıları bul ve listeye ekle

aranan_sayilar = []
for sayi1 in sayilar:     # bulduğumuz rakamları farklı sayılar arasından bir sayı seçiyoruz
    for sayi2 in sayilar: # başka bir sayı daha seçiyoruz
        if sayi1 == sayi2: # eğer aynılarsa sonraki sayıya geç
            continue
        if (sayi1 + sayi2) < 1000: # eğer toplamları 4 basamaklı değilse sonraki sayıya geç
            continue
        sayi3 = sayi1 + sayi2
        continue_et = False
        for i in str(sayi1):
            for j in str(sayi2):
                if i == j: # seçilen sayılar aynı rakamları içeriyorsa devam et
                    continue_et = True
        for i in str(sayi1):
            for j in str(sayi2):
                for k in str(sayi3):
                    if i == j or i == k or j == k: # seçilen sayılarrın toplamı, toplananlarla aynı rakamı içeriyorsa devam et
                        continue_et = True
        if continue_et:
            continue
        str_sayi3 = str(sayi3)
        f,s,t,q = str_sayi3
        if f != s and f != t and f != q and s != t and s != q and t != q: # seçilen sayıların toplamı içinde rakam tekrarı yapmıyorsa listeye ekle
            aranan_sayilar.append((str(sayi1) + " + " + str(sayi2) + " = " + str(sayi3)))

sayac = 0
for i in aranan_sayilar: # en son bulunan sayıları yazdır
    print(i)
    sayac += 1
print(sayac) # kaç tane bulunduğunu yazdır