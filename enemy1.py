import pygame as pg
from enemy import Enemy
enemy1=pg.image.load("images/enemy_images/enemy1.png").convert()
enemy1.set_colorkey((255, 255, 255))
RED=(255,0,0)
GREEN=(0,255,0)


class Enemy1(Enemy):
    image=None
    image_for_selected=None
    width=None
    half_width=None
    health=[150,600,2500]
    shield_points=[150,600,2500]
    cost_money=[15,45,160]
    cost_health=1
    armor=[0.25,0.5,0.8]
    speed=None
    shield=None
    health_bar_width=None
    half_health_bar_width=None
    health_bar_height=None
    red_health_bar=None

    def __init__(self,level,shield=None):
        super().__init__(Enemy1.speed,Enemy1.image)
        level=level-1
        self.level=level
        self.health=Enemy1.health[level]
        self.max_health = self.health
        self.armor=Enemy1.armor[level]
        self.shield=0
        self.max_shield=0
        if shield:
            self.shield_img=Enemy1.shield
            self.shield=Enemy1.shield_points[level]
            self.max_shield=self.shield
        self.cost_money=Enemy1.cost_money[level]
        self.cost_hp=Enemy1.cost_health
        self.rect=pg.Rect(self.x-self.half_width,self.y-self.half_width,self.width,self.width)

    def draw_health_bar(self,surface):
        rect=pg.Surface((round(self.health/self.max_health,1)*self.health_bar_width,self.health_bar_height))
        rect.fill(GREEN)
        health_bar_pos=(self.x-self.half_health_bar_width,self.y-self.width)
        surface.blit(self.red_health_bar,health_bar_pos)
        surface.blit(rect,health_bar_pos)

    @staticmethod
    def scaling_attributes(width_road,width_enemy):
        width=width_enemy
        img = pg.transform.scale(enemy1, (width, width))
        img1=pg.transform.scale(enemy1, (width*1.5, width*1.5))
        shield=pg.transform.scale(Enemy.shield, (round(width*1.7,1), round(width*1.7,1)))
        Enemy1.image = img
        Enemy1.image_for_selected=img1
        Enemy1.shield=shield
        Enemy1.speed = round(width_road/60,1)
        Enemy1.width=width
        Enemy1.half_width=round(width/2,1)
        Enemy1.health_bar_width=round(width_enemy/1.2,1)
        Enemy1.half_health_bar_width=round(Enemy1.health_bar_width/2,1)
        Enemy1.health_bar_height=round(width_enemy/9,1)
        Enemy1.red_health_bar=pg.Surface((Enemy1.health_bar_width,Enemy1.health_bar_height))
        Enemy1.red_health_bar.fill(RED)
