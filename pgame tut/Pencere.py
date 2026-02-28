import pygame as pg, time as t

pg.init()

#Pencere ayarları
genislik = 700
yukseklik = 500
gen_yuk = (genislik,yukseklik)
isim = "Pigeon"
pencere = pg.display.set_mode(gen_yuk)
pg.display.set_caption(isim)

#Renk ön ayarı
kirmizi = (255,0 ,0)
mavi = (0,0,255)
sari = (0,255,255)
teal = (0,128,128)

cizgi_gen = 3
pg.draw.line(pencere, kirmizi,(genislik/2,0),(genislik/2,yukseklik),3)
pg.draw.line(pencere, mavi,(0,yukseklik/2),(genislik,yukseklik/2),3)
pg.draw.circle(pencere, teal, (genislik/2,yukseklik/2),155,80)
fps = 10

pencere_acik = True
while pencere_acik:
    for etkinlik in pg.event.get():
        print(etkinlik)
        if etkinlik.type == pg.QUIT:
            pencere_acik = False
    pg.display.set_caption(isim + " : " + str(fps)+" FPS")
    cizgi_gen += 1
    pg.draw.line(pencere, kirmizi, (genislik / 2, 0), (genislik / 2, yukseklik), cizgi_gen)
    pg.draw.line(pencere, mavi, (0, yukseklik / 2), (genislik, yukseklik / 2), cizgi_gen)
    pg.display.update()
    t.sleep(1/fps)
pg.quit()