def islem_sec(islem:str):
    islem = islem.lower()

    def toplama(sayi1:int,sayi2:int):
        return sayi1 + sayi2

    def carpma(sayi1: int, sayi2: int):
        return sayi1 * sayi2

    def cikarma(sayi1:int,sayi2:int):
        return sayi1 - sayi2

    def bolme(sayi1:int,sayi2:int):
        return sayi1 / sayi2

    def hata(sayi1:int,sayi2:int):
        return "Geçersiz bir metod değeri girildi"

    # match islem:
    #     case "toplama":
    #         return toplama
    #     case "çarpma" | "carpma":
    #         return carpma
    #     case "çıkarma" | "cikarma":
    #         return cikarma
    #     case "bölme" | "bolme":
    #         return bolme

    if islem == "toplama":
        return toplama
    elif islem == "çarpma" or islem == "carpma":
        return carpma
    elif islem == "çıkarma" or islem == "cikarma":
        return cikarma
    elif islem == "bölme" or islem == "bolme":
        return bolme
    return hata

print(f"Sonuç: {islem_sec("cIkarma")(7,8)}")

toplayan = islem_sec("toplama")
print(f"Sonuç: {toplayan(13,7)}")