#coding=utf-8
import pygame
from GameSprite import *
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))
#把图片加载进来
bg =pygame.image.load("./images/bg.png")
#把图片加载进来
hero =pygame.image.load("./images/hero1.png")

rect = pygame.Rect(150,500,102,126)


enemy1 = GameSprite("./images/enemy-1.gif")#敌机精灵
enemy2 = GameSprite("./images/enemy-1.gif",2)#敌机精灵
enemy2.rect.x = 200
group = pygame.sprite.Group(enemy1,enemy2)#创建一个精灵组

#游戏时钟
clock = pygame.time.Clock()
while True:
    clock.tick(60)#一秒刷新60次
    rect.y-=2
    screen.blit(bg,(0,0))
    screen.blit(hero,rect)
    if rect.bottom == 0:
        rect.top = 700

    group.update()#群通知
    group.draw(screen)#绘制屏幕上
    #监听

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #更新的意思
    pygame.display.update()

pygame.quit()



