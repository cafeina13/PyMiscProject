with open("Metoo.txt", "r", encoding="UTF-8") as f:
    icerik = f.read(2)
    while len(icerik) > 0:
        print(icerik,end='')
        icerik = f.read(1)
