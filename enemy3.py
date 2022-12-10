import pygame as pg
from enemy import Enemy
enemy3=pg.image.load("images/enemy_images/enemy3.png").convert()
enemy3.set_colorkey((255,255,255))
RED=(255,0,0)
GREEN=(0,255,0)


class Enemy3(Enemy):
    image=None
    image_for_selected = None
    width=None
    half_width=None
    health=[80,320,1500]
    shield_points=[80,320,1500]
    cost_money=[12,36,145]
    cost_health=1
    armor=[0.15,0.35,0.6]
    speed=None
    shield=None
    health_bar_width=None
    half_health_bar_width=None
    health_bar_height=None
    red_health_bar=None

    def __init__(self,level,shield=None):
        super().__init__(Enemy3.speed,Enemy3.image)
        level = level - 1
        self.level = level
        self.health=Enemy3.health[level]
        self.max_health = self.health
        self.armor = Enemy3.armor[level]
        self.shield=0
        self.max_shield=0
        if shield:
            self.shield_img=Enemy3.shield
            self.shield=Enemy3.shield_points[level]
            self.max_shield=self.shield
        self.cost_money=Enemy3.cost_money[level]
        self.cost_hp=Enemy3.cost_health
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
        img = pg.transform.scale(enemy3, (width, width))
        img1=pg.transform.scale(enemy3, (width*1.5, width*1.5))
        shield=pg.transform.scale(Enemy.shield, (round(width*1.7,1), round(width*1.7,1)))
        Enemy3.image = img
        Enemy3.image_for_selected=img1
        Enemy3.shield=shield
        Enemy3.speed = round(width_road/40,1)
        Enemy3.width=width
        Enemy3.half_width=round(width/2,1)
        Enemy3.health_bar_width=round(width/1.2,1)
        Enemy3.half_health_bar_width=round(Enemy3.health_bar_width/2,1)
        Enemy3.health_bar_height=round(width_enemy/10,1)
        Enemy3.red_health_bar=pg.Surface((Enemy3.health_bar_width,Enemy3.health_bar_height))
        Enemy3.red_health_bar.fill(RED)
