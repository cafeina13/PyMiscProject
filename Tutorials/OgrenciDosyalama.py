kalanlar = []
gecenler = []

with open("ornek_metin.txt", 'r', encoding="UTF-8") as m:
    baslik = m.readline()
    while True:
        satir = m.readline()
        if len(satir) <= 0:
            break
        satirList = satir.split(' ')
        isim  = satirList[0]
        satirList.remove(isim)
        notlar = satirList[-1]
        satirList.remove(notlar)

        bolum = ' '.join(satirList)

        isimList = isim.split('-')

        soyad = isimList[-1]
        isimList.remove(soyad)
        ad = ' '.join(isimList)

        notlar = notlar.split('/')

        vize1 = int(notlar[0])
        vize2 = int(notlar[1])
        final = int(notlar[2])

        ortalama = round(vize1 * 0.3  + vize2 * 0.3 + final * 0.4, 1)

        if ortalama >= 70 and final >= 70:
            durum = "GEÇTİ"
            gecenler.append(ad + ';' + soyad + ';' + bolum + ';' + str(ortalama) + ';' + durum)
        else:
            durum = "KALDI"
            kalanlar.append(ad + ';' + soyad + ';' + bolum + ';' + str(ortalama) + ';' + durum)

def dosyaya_yaz(dosya_adi:str,liste:list):
    with open(dosya_adi,'w',encoding='UTF-8') as g:
        g.write("Ad" + ' ' * 28 + "Soyad" + ' ' * 25 + "Bolum" + ' ' * 25 + "Ortalama" + ' ' * 22 + "Durum\n")
        for l in liste:
            ogrenci = l.split(';')
            g.write('\n')
            for i in ogrenci:
                if i == ogrenci[-1]:
                    g.write(i)
                    continue
                g.write(i + ' ' * (30 - len(i)))


dosyaya_yaz("Gecenler.txt",gecenler)
dosyaya_yaz("Kalanlar.txt",kalanlar)