import pygame
import time
import random

# Oyun alanı boyutları
genislik = 800
yukseklik = 600

# Renkler
siyah = (0, 0, 0)
beyaz = (255, 255, 255)
kirmizi = (255, 0, 0)

# Yılanın başlangıç pozisyonu ve boyutu
bas_x = genislik / 2
bas_y = yukseklik / 2
yilan_bas = 10
yilan_boy = 10

# Yılanın hızı
hiz = 5

pygame.init()

# Oyun ekranını oluştur
oyun_ekrani = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Yılan Oyunu")

saat = pygame.time.Clock()

# Yılanın hareket yönü
yilan_x = 0
yilan_y = 0

# Yılanın vücudu
yilan_vucut = []
yilan_uzunlugu = 1

# Yem oluştur
yem_x = round(random.randrange(0, genislik - yilan_bas) / 10.0) * 10.0
yem_y = round(random.randrange(0, yukseklik - yilan_bas) / 10.0) * 10.0

# Oyun döngüsü
oyun_bitti = False
oyun_sonu = False

while not oyun_bitti:

    while oyun_sonu == True:
        oyun_ekrani.fill(beyaz)
        font = pygame.font.Font('freesansbold.ttf', 30)
        mesaj = font.render("Oyunu bitirdin! Tekrar oynamak için R'ye basın, çıkmak için Q'ya basın", True, siyah)
        oyun_ekrani.blit(mesaj, [genislik / 6, yukseklik / 3])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    oyun_bitti = True
                    oyun_sonu = False
                if event.key == pygame.K_r:
                    bas_x = genislik / 2
                    bas_y = yukseklik / 2
                    yilan_x = 0
                    yilan_y = 0
                    yilan_vucut = []
                    yilan_uzunlugu = 1
                    yem_x = round(random.randrange(0, genislik - yilan_bas) / 10.0) * 10.0
                    yem_y = round(random.randrange(0, yukseklik - yilan_bas) / 10.0) * 10.0
                    oyun_sonu = False

            if event.type == pygame.QUIT:
                oyun_bitti = True
                oyun_sonu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun_bitti = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yilan_x = -hiz
                yilan_y = 0
            elif event.key == pygame.K_RIGHT:
                yilan_x = hiz
                yilan_y = 0
            elif event.key == pygame.K_UP:
                yilan_y = -hiz
                yilan_x = 0
            elif event.key == pygame.K_DOWN:
                yilan_y = hiz
                yilan_x = 0

    if bas_x >= genislik or bas_x < 0 or bas_y >= yukseklik or bas_y < 0:
        oyun_sonu = True
    bas_x += yilan_x
    bas_y += yilan_y
    oyun_ekrani.fill(beyaz)
    pygame.draw.rect(oyun_ekrani, kirmizi, [yem_x, yem_y, yilan_bas, yilan_bas])

    yilan_baslar = []
    yilan_baslar.append(bas_x)
    yilan_baslar.append(bas_y)
    yilan_vucut.append(yilan_baslar)
    if len(yilan_vucut) > yilan_uzunlugu:
        del yilan_vucut[0]

    for parca in yilan_vucut[:-1]:
        if parca == yilan_baslar:
            oyun_sonu = True

    for parca in yilan_vucut:
        pygame.draw.rect(oyun_ekrani, siyah, [parca[0], parca[1], yilan_bas, yilan_bas])

    pygame.display.update()

    if bas_x == yem_x and bas_y == yem_y:
        yem_x = round(random.randrange(0, genislik - yilan_bas) / 10.0) * 10.0
        yem_y = round(random.randrange(0, yukseklik - yilan_bas) / 10.0) * 10.0
        yilan_uzunlugu += 1

    saat.tick(30)

pygame.quit()
