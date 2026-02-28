import pygame as pg
import random

pg.init()

class Karakter(pg.sprite.Sprite):
    def __init__(self, img_path, konum):
        pg.sprite.Sprite.__init__(self)
        self.image: pg.Surface = pg.image.load(img_path).convert_alpha()
        self.rect: pg.Rect = self.image.get_rect(center=konum)

class Ordek(Karakter):
    def __init__(self, konum):
        super().__init__("Resim/Ordek.png", konum)
        self.sag = self.image.copy()
        self.sol = pg.transform.flip(self.image, True, False)
        self.hiz = 5
        self.sag_gider = False
        self.sol_gider = False
        self.ziplama_gucu = 0
        self.yerde = False
        self.vak = pg.mixer.Sound("Ses/CAWFEE.mp3")
        self.score = 0

    def update(self, basilan_tuslar_ordek, boyut, platformlar):
        self.sag_gider = False
        self.sol_gider = False

        # Horizontal movement
        for tus in basilan_tuslar_ordek:
            match tus:
                case 'sol':
                    self.rect.x -= self.hiz
                    self.sol_gider = True
                case 'sag':
                    self.rect.x += self.hiz
                    self.sag_gider = True
                case 'zipla':
                    if self.yerde:
                        self.ziplama_gucu = -15
                        self.yerde = False

        if self.sag_gider and not self.sol_gider:
            self.image = self.sag
        elif self.sol_gider and not self.sag_gider:
            self.image = self.sol

        # Boundaries
        self.rect.x = max(0, min(self.rect.x, boyut[0] - self.rect.width))

        # Gravity
        self.ziplama_gucu += 0.6
        self.rect.y += self.ziplama_gucu

        # Platform collision
        self.yerde = False
        for platform in platformlar:
            if self.rect.colliderect(platform.rect):
                if self.ziplama_gucu > 0:  # Falling down
                    if self.rect.bottom - self.ziplama_gucu <= platform.rect.top:
                        self.rect.bottom = platform.rect.top
                        self.ziplama_gucu = 0
                        self.yerde = True

        # Death if fall off screen
        if self.rect.y > boyut[1]:
            self.rect.center = (boyut[0] // 2, 50)
            self.ziplama_gucu = 0

class Para(Karakter):  # Coin class
    def __init__(self, konum):
        super().__init__("Resim/coffee-beans.png", konum)
        self.collected = False

    def update(self):
        pass

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image: pg.Surface = pg.Surface((width, height))
        self.image.fill((100, 100, 100))  # Gray platforms
        self.rect: pg.Rect = self.image.get_rect(topleft=(x, y))

def get_key(event_key: int):
    match event_key:
        case pg.K_UP | pg.K_w | pg.K_SPACE:
            return 'zipla'
        case pg.K_LEFT | pg.K_a:
            return 'sol'
        case pg.K_RIGHT | pg.K_d:
            return 'sag'
        case _:
            return ''

def update_window(ordek, platformlar, paralar):
    pencere.fill((0, 0, 0))
    
    # Draw platforms
    for platform in platformlar:
        pencere.blit(platform.image, platform.rect)
    
    # Draw coins
    for para in paralar:
        if not para.collected:
            pencere.blit(para.image, para.rect)
    
    # Draw duck
    pencere.blit(ordek.image, ordek.rect)
    
    # Draw score
    font = pg.font.Font(None, 36)
    score_text = font.render(f"Coins: {ordek.score}", True, (255, 255, 255))
    pencere.blit(score_text, (10, 10))
    
    pg.display.update()
    saat.tick(fps)

# Game setup
genx = 700
geny = 500
boyut = (genx, geny)
fps = 60
pencere = pg.display.set_mode(boyut)
pg.display.set_caption("Para Kapma - Level 1")

saat = pg.time.Clock()

# Create platforms
platformlar = [
    Platform(0, 450, 700, 50),      # Ground
    Platform(100, 380, 120, 20),    # Platform 1
    Platform(300, 320, 120, 20),    # Platform 2
    Platform(500, 260, 120, 20),    # Platform 3
    Platform(150, 200, 120, 20),    # Platform 4
    Platform(450, 140, 120, 20),    # Platform 5
]

# Create coins on platforms
paralar = [
    Para((160, 340)),
    Para((360, 280)),
    Para((560, 220)),
    Para((210, 160)),
    Para((510, 100)),
]

ordek = Ordek((350, 400))

pencere_acik = True
basilan_tuslar = set()
level_complete = False

while pencere_acik:
    for olay in pg.event.get():
        if olay.type == pg.QUIT:
            pencere_acik = False
        elif olay.type == pg.WINDOWLEAVE:
            pencere_acik = False
        elif olay.type == pg.KEYDOWN:
            key = get_key(olay.key)
            if key:
                basilan_tuslar.add(key)
        elif olay.type == pg.KEYUP:
            key = get_key(olay.key)
            basilan_tuslar.discard(key)

    ordek.update(basilan_tuslar, boyut, platformlar)

    # Check coin collision
    for para in paralar:
        if not para.collected and ordek.rect.colliderect(para.rect):
            para.collected = True
            ordek.vak.play()
            ordek.vak.fadeout(2000)
            ordek.score += 1

    # Win condition
    if ordek.score >= 5:
        level_complete = True

    update_window(ordek, platformlar, paralar)

    # Draw win message
    if level_complete:
        font_big = pg.font.Font(None, 72)
        win_text = font_big.render("LEVEL 1 COMPLETE!", True, (0, 255, 0))
        text_rect = win_text.get_rect(center=(boyut[0]//2, boyut[1]//2))
        pencere.blit(win_text, text_rect)
        pg.display.update()

pg.quit()