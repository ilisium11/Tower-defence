import pygame as pg
from enemy import Enemy
enemy2=pg.image.load("images/enemy_images/enemy2.png").convert()
enemy2.set_colorkey((255,255,255))
RED=(255,0,0)
GREEN=(0,255,0)


class Enemy2(Enemy):
    image=None
    image_for_selected = None
    width=None
    half_width=None
    health=[400,1600,8000]
    shield_points=[400,1600,8000]
    cost_money=[45,135,500]
    cost_health=3
    armor=[0.45,0.75,0.9]
    speed=None
    shield=None
    health_bar_width=None
    half_health_bar_width=None
    health_bar_height=None
    red_health_bar=None

    def __init__(self,level,shield=None):
        super().__init__(Enemy2.speed,Enemy2.image)
        level = level - 1
        self.level = level
        self.health=Enemy2.health[level]
        self.max_health = self.health
        self.armor = Enemy2.armor[level]
        self.shield=0
        self.max_shield=0
        if shield:
            self.shield_img=Enemy2.shield
            self.shield=Enemy2.shield_points[level]
            self.max_shield=self.shield
        self.cost_money=Enemy2.cost_money[level]
        self.cost_hp=Enemy2.cost_health
        self.rect=pg.Rect(self.x-self.half_width,self.y-self.half_width,self.width,self.width)

    def draw_health_bar(self,surface):
        rect=pg.Surface((round(self.health/self.max_health,1)*self.health_bar_width,self.health_bar_height))
        rect.fill(GREEN)
        health_bar_pos=(self.x-self.half_health_bar_width,self.y-self.width-self.health_bar_height)
        surface.blit(self.red_health_bar,health_bar_pos)
        surface.blit(rect,health_bar_pos)

    @staticmethod
    def scaling_attributes(width_road,width_enemy):
        width=round(width_enemy,1)
        img = pg.transform.scale(enemy2, (width, width))
        img1=pg.transform.scale(enemy2, (width*1.5, width*1.5))
        shield=pg.transform.scale(Enemy.shield, (round(width*1.7,1), round(width*1.7,1)))
        Enemy2.image = img
        Enemy2.image_for_selected=img1
        Enemy2.shield=shield
        Enemy2.speed = round(width_road/80,1)
        Enemy2.width=width
        Enemy2.half_width=round(width/2,1)
        Enemy2.health_bar_width=round(width/1.2,1)
        Enemy2.half_health_bar_width=round(Enemy2.health_bar_width/2,1)
        Enemy2.health_bar_height=round(width_enemy/10,1)
        Enemy2.red_health_bar=pg.Surface((Enemy2.health_bar_width,Enemy2.health_bar_height))
        Enemy2.red_health_bar.fill(RED)
