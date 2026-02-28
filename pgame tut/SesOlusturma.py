import time

import pygame as p

p.init()

# Pencere oluşturma
genislik = 700
yukseklik = 500
isim = "Seslerim"
resim = p.image.load("Resim/coffee-beans.png")
pencere = p.display.set_mode((genislik,yukseklik))
p.display.set_caption(isim)
p.display.set_icon(resim)

# Ses ayarlama
ses_efekti1 = p.mixer.Sound("Ses\\Splash.wav")
ses_efekti2 = p.mixer.Sound("Ses\\OhFak.wav")
p.mixer.music.load("Ses\\Flute.wav")
p.mixer_music.play(-1)

# Pencere işleme
pencere_acik = True
while pencere_acik:
    for olay in p.event.get():
        print(olay)
        if olay.type == p.QUIT:
            pencere_acik = False
        if olay.type == p.MOUSEBUTTONUP:
            ses_efekti1.play()
        if olay.type == p.MOUSEBUTTONDOWN:
            ses_efekti2.play()
    pencere.blit(resim,(334,234),resim.get_rect())
    p.display.update()
    pencere.fill((0,0,0))
    time.sleep(1/25)

p.quit()