import pygame as p, time as t

p.init()

genislik = 500
yukseklik = 500
pencere = p.display.set_mode((genislik,yukseklik))
fontum = p.font.SysFont('simsunextb',64)
yazi = fontum.render("Herkese Bye", 1,(80,0,0))
yazi_koordinat = yazi.get_rect()
yazi_koordinat.topleft = (80,150)

pencere_acik = True
while pencere_acik:
    for etkinlik in p.event.get():
        if etkinlik.type == p.QUIT:
            pencere_acik = False
    pencere.blit(yazi,yazi_koordinat)
    p.display.update()
    pencere.fill((0,0,10))
    t.sleep(1/30)




p.quit()