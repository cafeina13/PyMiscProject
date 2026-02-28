from os import chdir, listdir, path as tpath, mkdir, rename, getcwd, rmdir, stat
import time as t


def hSDznl(yol: str, klasorKlasoru: str = "MainFolder",
           dosyaKlasoru: str = "FileFolder"):  # Klasör ve dosya düzenleme fonksiyonlarını çağırır
    sayacD, hata_sayacD = dDnl(yol, dosyaKlasoru)  # dDnl'den gelen sayaç ve hata_sayaci
    sayacK, hata_sayacK = kDnl(yol, klasorKlasoru)  # kDnl'den gelen sayaç ve hata_sayaci

    toplam_hata_sayaci = hata_sayacD + hata_sayacK
    toplam_sayac = sayacD + sayacK
    return f"{toplam_sayac} |E {toplam_hata_sayaci}"


def kDnl(yol: str, anaKlasorAdi: str = "MainFolder"):  # Klasör düzenler
    cwd = getcwd()  # Düzenlenecek yolu alır, default haricinde ana klasör adı alır
    sayac = 0
    hata_sayaci = 0
    try:
        chdir(yol)  # Kaç klasör yer değiştirildi bilgisini döndürür
    except OSError as e:
        print(f"Hata: '{yol}' dizinine geçilemedi. Sebep: {e}")
        hata_sayaci += 1
        return 0, hata_sayaci  # Hata durumunda işlem yapmadığı için 0 döndür

    for i in listdir():
        if tpath.isdir(i):
            dirKlasor = anaKlasorAdi
            try:
                if not tpath.exists(dirKlasor):
                    mkdir(dirKlasor)
            except OSError as e:
                print(f"Hata: '{dirKlasor}' klasörü oluşturulamadı. Sebep: {e}")
                hata_sayaci += 1
                continue  # Bu klasörü atla

            try:
                rename(i, tpath.join(dirKlasor, i))
                sayac += 1
            except OSError as e:
                print(f"Hata: '{i}' klasörü taşınamadı. Sebep: {e}")
                hata_sayaci += 1
                # Hata olsa bile sayacı artırmıyoruz, çünkü taşınmadı.
    try:
        chdir(cwd)
    except OSError as e:
        print(f"Hata: Orijinal dizine ('{cwd}') geri dönülemedi. Sebep: {e}")
        hata_sayaci += 1
    return sayac, hata_sayaci


def dDnl(yol: str, anaKlasorAdi: str = "FileFolder"):  # Dosyaları Düzenler
    cwd = getcwd()  # Düzenlenecek yolu alır, default haricinde Dosya klasörü adını alır
    sayac = 0
    hata_sayaci = 0
    try:
        chdir(yol)  # Kaç dosya yer değiştirildi bilgisini döndürür
    except OSError as e:
        print(f"Hata: '{yol}' dizinine geçilemedi. Sebep: {e}")
        hata_sayaci += 1
        return 0, hata_sayaci  # Hata durumunda işlem yapmadığı için 0 döndür

    for i in listdir():
        if tpath.isfile(i):
            klasor = tpath.splitext(i)[1].replace(".", "")
            if klasor == '' or i.startswith('.'):
                continue
            aKlasor = tpath.join(anaKlasorAdi, klasor)

            try:
                if not tpath.exists(anaKlasorAdi):
                    mkdir(anaKlasorAdi)
            except OSError as e:
                print(f"Hata: '{anaKlasorAdi}' klasörü oluşturulamadı. Sebep: {e}")
                hata_sayaci += 1
                continue  # Bu dosyayı atla, çünkü ana klasör yok

            try:
                if not tpath.exists(aKlasor):
                    mkdir(aKlasor)
            except OSError as e:
                print(f"Hata: '{aKlasor}' klasörü oluşturulamadı. Sebep: {e}")
                hata_sayaci += 1
                continue  # Bu dosyayı atla, çünkü alt klasör yok

            try:
                rename(i, tpath.join(aKlasor, i))
                sayac += 1
            except OSError as e:
                print(f"Hata: '{i}' dosyası taşınamadı. Sebep: {e}")
                hata_sayaci += 1
                # Hata olsa bile sayacı artırmıyoruz, çünkü taşınmadı.
    try:
        chdir(cwd)
    except OSError as e:
        print(f"Hata: Orijinal dizine ('{cwd}') geri dönülemedi. Sebep: {e}")
        hata_sayaci += 1
    return sayac, hata_sayaci


"""__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---__---"""


def tarih_sirala_klasor2(
        yol: str):  # ana klasörün içine onun içindeki klasörlerin içindeki öğeleri tarihe göre kategorize eder
    cwd = getcwd()
    sayac = 0
    hata_sayaci = 0
    try:
        chdir(yol)
    except OSError as e:
        print(f"Hata: '{yol}' dizinine geçilemedi. Sebep: {e}")
        hata_sayaci += 1
        return 0, hata_sayaci

    anaKlasor = listdir(yol)
    for i in anaKlasor:
        if tpath.isdir(i):
            try:
                chdir(tpath.join(yol, i))
            except OSError as e:
                print(f"Hata: '{tpath.join(yol, i)}' alt dizinine geçilemedi. Sebep: {e}")
                hata_sayaci += 1
                continue

            try:
                gezelienKlasor = listdir()
            except OSError as e:
                print(f"Hata: '{tpath.join(yol, i)}' alt dizini listelenemedi. Sebep: {e}")
                hata_sayaci += 1
                gezelienKlasor = []

            for j in gezelienKlasor:
                try:
                    degistirmeTarihiTuple = t.localtime(stat(j)[8])
                except OSError as e:
                    print(f"Hata: '{j}' öğesinin istatistik bilgisi alınamadı. Sebep: {e}")
                    hata_sayaci += 1
                    continue

                dTarihiSTR = t.strftime("%d %B %Y %A, %H.%M", degistirmeTarihiTuple)
                klasor = tpath.join(yol, dTarihiSTR)
                yeniYol = tpath.join(klasor, j)

                try:
                    if not tpath.exists(klasor):
                        mkdir(klasor)
                except OSError as e:
                    print(f"Hata: '{klasor}' tarih klasörü oluşturulamadı. Sebep: {e}")
                    hata_sayaci += 1
                    continue

                try:
                    rename(j, yeniYol)
                    sayac += 1
                except OSError as e:
                    print(f"Hata: '{j}' öğesi taşınamadı. Sebep: {e}")
                    hata_sayaci += 1

            try:
                chdir(yol)
            except OSError as e:
                print(f"Hata: '{yol}' ana dizinine geri dönülemedi. Sebep: {e}")
                hata_sayaci += 1
    try:
        chdir(cwd)
    except OSError as e:
        print(f"Hata: Orijinal dizine ('{cwd}') geri dönülemedi. Sebep: {e}")
        hata_sayaci += 1
    return f"{sayac} |E {hata_sayaci}"


def tarihSiralaDosya(yol: str):  # ana klasör içindeki öğeleri tarihe göre kategorize eder
    cwd = getcwd()
    sayac = 0
    hata_sayaci = 0
    try:
        chdir(yol)
    except OSError as e:
        print(f"Hata: '{yol}' dizinine geçilemedi. Sebep: {e}")
        hata_sayaci += 1
        return 0, hata_sayaci

    anaKlasor = listdir(yol)
    for i in anaKlasor:
        if tpath.isfile(i):
            try:
                degistirmeTarihiTuple = t.localtime(stat(i)[8])
            except OSError as e:
                print(f"Hata: '{i}' dosyasının istatistik bilgisi alınamadı. Sebep: {e}")
                hata_sayaci += 1
                continue

            dTarihiSTR = t.strftime("%d %B %Y %A, %H.%M", degistirmeTarihiTuple)
            klasor = tpath.join(yol, dTarihiSTR)
            yeniYol = tpath.join(klasor, i)

            try:
                if not tpath.exists(klasor):
                    mkdir(klasor)
            except OSError as e:
                print(f"Hata: '{klasor}' tarih klasörü oluşturulamadı. Sebep: {e}")
                hata_sayaci += 1
                continue

            try:
                rename(i, yeniYol)
                sayac += 1
            except OSError as e:
                print(f"Hata: '{i}' dosyası taşınamadı. Sebep: {e}")
                hata_sayaci += 1
    try:
        chdir(cwd)
    except OSError as e:
        print(f"Hata: Orijinal dizine ('{cwd}') geri dönülemedi. Sebep: {e}")
        hata_sayaci += 1
    return f"{sayac} |E {hata_sayaci}"


def dosyaCikar(yol: str):  # bir klasörün içindeki klasörlerdeki öğeleri bir üst dizine çıkarır
    cwd = getcwd()
    sayac = 0
    hata_sayaci = 0
    try:
        chdir(yol)
    except OSError as e:
        print(f"Hata: '{yol}' dizinine geçilemedi. Sebep: {e}")
        hata_sayaci += 1
        return 0, hata_sayaci

    anaKlasor = listdir()
    for i in anaKlasor:
        if tpath.isdir(i):
            try:
                chdir(tpath.join(yol, i))
            except OSError as e:
                print(f"Hata: '{tpath.join(yol, i)}' alt dizinine geçilemedi. Sebep: {e}")
                hata_sayaci += 1
                continue

            try:
                gezelienKlasor = listdir()
            except OSError as e:
                print(f"Hata: '{tpath.join(yol, i)}' alt dizini listelenemedi. Sebep: {e}")
                hata_sayaci += 1
                gezelienKlasor = []

            for j in gezelienKlasor:
                yeniYol = tpath.join(yol, j)

                try:
                    rename(j, yeniYol)
                    sayac += 1
                except OSError as e:
                    print(f"Hata: '{j}' öğesi '{yol}' dizinine taşınamadı. Sebep: {e}")
                    hata_sayaci += 1

            try:
                chdir(yol)
            except OSError as e:
                print(f"Hata: '{yol}' ana dizinine geri dönülemedi. Sebep: {e}")
                hata_sayaci += 1
    try:
        chdir(cwd)
    except OSError as e:
        print(f"Hata: Orijinal dizine ('{cwd}') geri dönülemedi. Sebep: {e}")
        hata_sayaci += 1
    return f"{sayac} |E {hata_sayaci}"


def bosKlasorSil(yol: str):  # bir klasördeki içi boş klasörleri siler
    cwd = getcwd()
    sayac = 0
    hata_sayaci = 0
    try:
        chdir(yol)
    except OSError as e:
        print(f"Hata: '{yol}' dizinine geçilemedi. Sebep: {e}")
        hata_sayaci += 1
        return 0, hata_sayaci

    for i in listdir(yol):
        try:
            if tpath.isdir(i) and len(listdir(i)) == 0:
                rmdir(i)
                sayac += 1
        except OSError as e:
            print(f"Hata: '{i}' klasörü silinemedi. Sebep: {e}")
            hata_sayaci += 1
    try:
        chdir(cwd)
    except OSError as e:
        print(f"Hata: Orijinal dizine ('{cwd}') geri dönülemedi. Sebep: {e}")
        hata_sayaci += 1
    return f"{sayac} |E {hata_sayaci}"