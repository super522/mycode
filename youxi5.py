#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import pygame
import random
from os import path
from pygame.locals import *

WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (222,0,222)
img_dir = "/home/yiqing/Desktop/test/images"
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       # self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 0

        self.shield = 100
        self.lives = 3
        self.hidden =  False
        self.hide_timer  = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center= (SCREEN_WIDTH//2,SCREEN_HEIGHT-20)



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.speedx = -5
        elif keys[K_RIGHT]:
            self.speedx = 5

        else:
            self.speedx = 0
        self.rect.x += self.speedx


        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.speedy = -5
        elif keys[K_DOWN]:
            self.speedy = 5
        else:
            self.speedy = 0
        self.rect.y += self.speedy

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def  shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_snd.play()



class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = meteor_img
        #self.image.fill(RED)
        self.image = random.choice(meteor_img)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)




    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or \
                self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img,(60,80))
        #self.image.fill(YELLOW)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        #self.image.fill(YELLOW)
        self.image = explosion_mob[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_mob[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_mob[self.size][self.frame]
                self.rect.center = center


font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    s1 = font.render(text, True, WHITE)
    rect = s1.get_rect()
    rect.midtop = (x,y)
    surf.blit(s1,rect)

def draw_shield_bar(surf,pt, x, y):
    if pt < 0:
        pt = 0
    WIDTH = 100
    HEIGHT = 10
    fill = (pt / 100) * WIDTH
    outline_rect = pygame.Rect(x, y, WIDTH, HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE,outline_rect,2)



def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        rect = img.get_rect()
        rect.x = x + 30 * i
        rect.y = y
        surf.blit(img, rect)



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Flight")
#set_modeI(chuang kou da xiao)

background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()

player_img_mini = pygame.transform.scale(player_img, (25,19))
player_img_mini.set_colorkey(player_img_mini.get_at((0,0)))

meteor_img = []
meteor_list = ["meteorBrown_big1.png","meteorBrown_big2.png","meteorBrown_med1.png","meteorBrown_med3.png","meteorBrown_small1.png","meteorBrown_small2.png","meteorBrown_tiny1.png","meteorBrown_tiny2.png"]
for x in meteor_list:
    img = pygame.image.load(path.join(img_dir,x)).convert()
    meteor_img.append(img)



background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

shoot_snd = pygame.mixer.Sound(path.join("test/sound", "pew.wav"))
explode_sounds = []
for s in ['expl3.wav', 'expl6.wav']:
    snd = pygame.mixer.Sound(path.join("test/sound", s))
    explode_sounds.append(snd)
bk_snd = pygame.mixer.Sound(path.join("test/sound", "hhh.ogg"))



explosion_mob = {}
explosion_mob['lg'] = []
explosion_mob['sm'] = []
explosion_mob['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(img.get_at((0,0)))
    img_lg = pygame.transform.scale(img,(75,75))
    explosion_mob['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img,(32,32))
    explosion_mob['sm'].append(img_sm)
    filename_pl = 'sonicExplosion0{}.png'.format(i)
    img_pl = pygame.image.load(path.join(img_dir, filename_pl)).convert()
    img_pl.set_colorkey(img.get_at((0,0)))
    explosion_mob['player'].append(img_pl)





all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
bullets = pygame.sprite.Group()

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

for i in range(8):
    m1 = Mob()
    all_sprites.add(m1)
    mobs.add(m1)


clock = pygame.time.Clock()

bk_snd.play(-1)
play_scores = 0


running = True

while running:
    clock.tick(FPS)
#event(xiao xi dui lie)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type  == KEYDOWN:
            if event.key == K_SPACE:
                player.shoot()

    hits = pygame.sprite.spritecollide(player,mobs,False)
    


    all_sprites.update()

    hits = pygame.sprite.spritecollide(player,mobs,False)


    for m in hits: 
        player.shield -= m.rect.width/1000
        if player.shield <= 0:
            running = False

    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for m in hits: 
        player.shield -= m.radius // 2
        expl = Explosion(m.rect.center, 'sm')
        all_sprites.add(expl)

        newm = Mob()
        all_sprites.add(newm)
        mobs.add(newm)

        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center,'player')
            all_sprites.add(death_explosion)


            player.hide()
            player.lives -= 1
            player.shield = 100
            print(player.lives)
        
    if player.lives <= 0 and not death_explosion.alive():
        running = False
          




    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        snd = random.choice(explode_sounds)
        snd.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        snd.play()


        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

        play_scores += 50 - hit.rect.width//100


    # render this frame
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    draw_shield_bar(screen,player.shield, SCREEN_WIDTH // 2, 10)

    draw_text(screen, str(play_scores),18,SCREEN_WIDTH // 2, 10)
    draw_lives(screen, SCREEN_WIDTH - 100, 5, player.lives, player_img_mini)
    # display this frame
    pygame.display.flip()





"""
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.speedx = -8
            if event.key = K_RIGHT:
                player.speedx = 8
"""
