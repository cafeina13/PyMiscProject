with open("Metoo.txt", encoding="UTF-8") as okunacak:
    with open("Metin2", 'w', encoding="UTF-8") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)