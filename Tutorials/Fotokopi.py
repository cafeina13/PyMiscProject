with open("oGeliyor.png", "br") as okunacak:
    with open("buGeliyor.png", "bw") as yazilacak:
        icerik = okunacak.read(1000)
        sayac = 0
        while len(icerik) > 0:
            yazilacak.write(icerik)
            icerik = okunacak.read(1000)
            sayac += 1
        print(sayac) 