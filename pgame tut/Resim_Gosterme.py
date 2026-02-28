import pygame as p, time as t

p.init()

#Pencere ayarları
genislik = 700
yukseklik = 500
gen_yuk = (genislik,yukseklik)
isim = "Resim Göster"
pencere = p.display.set_mode(gen_yuk)
p.display.set_caption(isim)

#resim gösterme
cekirdek = p.image.load("Resim/coffee-beans.png")
cekirdek_koordinat_x = 10
cekirdek_koordinat_y = 10
cekirdek_rect = cekirdek.get_rect()
cekirdek_rect.topleft = (cekirdek_koordinat_x,cekirdek_koordinat_y)

sayac = 0

pencere_acik = True
while pencere_acik:
    for i in p.event.get():
        if i.type == p.QUIT:
            pencere_acik = False
    pencere.fill((0,0,0))
    if sayac <= 50:
        pencere.blit(cekirdek, cekirdek_rect)
    sayac += 1
    p.display.update()
    t.sleep(1/25)
p.quit()