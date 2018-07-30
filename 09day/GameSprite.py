#coding=utf-8
import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class GameSprite(pygame.sprite.Sprite):#父类 大写

    def __init__(self,image,speed=1):
        super(GameSprite,self).__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y +=self.speed


#创建背景精灵
class BackGround(GameSprite):
	def __init__(self,is_alt=False):
		image_name="./images/bg.png"
		super(BackGround,self).init__(imagename,10)
		if is_alt:
			self.rect.y = -self.rect.height
	

	def update(self):
		super(GameSprite,self).update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Enemy(GameSprite):
	"""敌机精灵"""

	def __init__(self):
		imagename = "./images/enemy-1.gif"
		super(BackGround,self).__init__imagename)
		self.speed = random.randint(1,3)
		# 2. 设置敌机的随机初始速度
		self.rect.bottom = 0
		# 3. 设置敌机的随机初始位置

	def update(self):

		# 1. 调用父类方法，让敌机在垂直方向运动
		super(BackGround).update()

		# 2. 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
		if self.rect.y >= SCREEN_RECT.height:
			print("敌机飞出屏幕...")	

'''
class Hero(GameSprite):
	def __init__(self):
		super().__init__("")
		self.rect.ccenterx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
'''
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("")
	def update(self):
		siper().update()
		
		if self.rect.bottom < 0:
			self.kill()






