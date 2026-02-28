import pygame as p
import time

p.init()


def update_window():
    pencere.blit(ordek, ordek_rect)
    p.display.update()
    pencere.fill((0, 0, 0))
    saat.tick(fps)

def get_key(event_key:int):
    match event_key:
        case p.K_UP | p.K_w:
            return 'w'
        case p.K_DOWN | p.K_s:
            return 's'
        case p.K_LEFT | p.K_a:
            return 'a'
        case p.K_RIGHT | p.K_d:
            return 'd'
        case _:
            return ''

genx = 700
yuky = 500
pencere = p.display.set_mode((genx,yuky))
fps = 30

ordek = p.image.load("Resim/Ordek.png")
ordek_sag = ordek.copy()
ordek_sol = p.transform.flip(ordek, 1,0)
ordek_rect = ordek.get_rect(center=(genx//2, yuky//2))
ordek_hiz = 10

sound_fak = p.mixer.Sound("Ses/OhFak.wav")
sound_slash = p.mixer.Sound("Ses/Splash.wav")

ordek_gitmek_sol = False
ordek_gitmek_sag = False

saat = p.time.Clock()

pencere_acik = True
basilan_tuslar = set()
while pencere_acik:
    for olay in p.event.get():
        print(olay)
        if olay.type == p.QUIT:
            pencere_acik = False
        if olay.type == p.KEYDOWN:
            key = get_key(olay.key)
            if key:
                basilan_tuslar.add(key)
        if olay.type == p.KEYUP:
            key = get_key(olay.key)
            basilan_tuslar.discard(key)

        if olay.type == p.MOUSEBUTTONDOWN:
            mouse_pos_x = olay.pos[0]
            mouse_pos_y = olay.pos[1]

            if olay.button == 3 and ordek_rect.collidepoint(olay.pos):
            # if abs(ordek_rect.centerx - mouse_pos_x) < ordek.get_width()/1.5 and abs(ordek_rect.centery - mouse_pos_y) < ordek.get_height()/1.5:
                sound_slash.play()
            elif olay.button == 1:
                while ordek_rect.center != (mouse_pos_x,mouse_pos_y):
                    if ordek_rect.centery < mouse_pos_y:
                        gidilen_nokta_y = max((ordek_rect.centery - mouse_pos_y)//-2,1)
                        ordek_rect.centery += gidilen_nokta_y
                        # print(f"y değeri {gidilen_nokta_y} oldu")
                    elif ordek_rect.centery > mouse_pos_y:
                        gidilen_nokta_y = max((ordek_rect.centery - mouse_pos_y)//2,1)
                        ordek_rect.centery -= gidilen_nokta_y
                        # print(f"y değeri {gidilen_nokta_y} oldu")
                    else:
                        pass

                    if ordek_rect.centerx < mouse_pos_x:
                        gidilen_nokta_x = max((ordek_rect.centerx - mouse_pos_x)//-2,1)
                        ordek_rect.centerx += gidilen_nokta_x
                        # print(f"x değeri {gidilen_nokta_x} oldu")
                    elif ordek_rect.centerx > mouse_pos_x:
                        gidilen_nokta_x = max((ordek_rect.centerx - mouse_pos_x)//2, 1)
                        ordek_rect.centerx -= gidilen_nokta_x
                        # print(f"x değeri {gidilen_nokta_x} oldu")

                    else:
                        pass
                    time.sleep(0.01)
                    update_window()

    ordek_gitmek_sag = False
    ordek_gitmek_sol = False

    for i in basilan_tuslar:
        match i:
            case 'a':
                ordek_rect.x += -ordek_hiz
                ordek_gitmek_sol = True
            case 'd':
                ordek_rect.x += ordek_hiz
                ordek_gitmek_sag = True
            case 'w':
                ordek_rect.y += -ordek_hiz
            case 's':
                ordek_rect.y += ordek_hiz

    if ordek_gitmek_sag and not ordek_gitmek_sol:
        ordek = ordek_sag
    elif ordek_gitmek_sol and not ordek_gitmek_sag:
        ordek = ordek_sol

    ordek_rect.x = max(0, min(ordek_rect.x, genx - ordek_rect.width))
    ordek_rect.y = max(0, min(ordek_rect.y, yuky - ordek_rect.height))

    update_window()

p.quit()