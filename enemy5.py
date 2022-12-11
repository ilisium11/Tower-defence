import pygame as pg
from enemy import Enemy
enemy3=pg.image.load("images/enemy_images/enemy5.png").convert()
enemy3.set_colorkey((255,255,255))
RED=(255,0,0)
GREEN=(0,255,0)


class Enemy5(Enemy):
    image=None
    image_for_selected = None
    width=None
    half_width=None
    health=[1500,6000,15000]
    shield_regen=[8,32,100]
    shield_points=[3000,12000,55000]
    cost_money=[180,540,1800]
    cost_health=5
    armor=[0.15,0.35,0.5]
    speed=None
    shield=None
    health_bar_width=None
    half_health_bar_width=None
    health_bar_height=None
    red_health_bar=None

    def __init__(self,level,shield=None):
        super().__init__(Enemy5.speed,Enemy5.image)
        level = level - 1
        self.level = level
        self.health=Enemy5.health[level]
        self.max_health = self.health
        self.shield_regen=Enemy5.shield_regen[level]
        self.armor = Enemy5.armor[level]
        self.shield=0
        self.max_shield=0
        if shield:
            self.shield_img=Enemy5.shield
            self.shield=Enemy5.shield_points[level]
            self.max_shield=self.shield
        self.cost_money=Enemy5.cost_money[level]
        self.cost_hp=Enemy5.cost_health
        self.rect=pg.Rect(self.x-self.half_width,self.y-self.half_width,self.width,self.width)
        self.width_area_regen=self.width*5
        self.half_width_area_regen=round(self.width_area_regen/2,1)
        self.rect_area_regen=pg.Rect(self.x-self.half_width_area_regen,self.y-self.half_width_area_regen,self.width_area_regen,self.width_area_regen)
        self.delay_regeneration=20
        self.counter_delay=0

    def run(self,wave):
        if super().run():
            return True
        self.set_center_area()
        if self.counter_delay==self.delay_regeneration:
            self.counter_delay=0
            for enemy in wave:
                if self.rect_area_regen.colliderect(enemy.rect):
                    if enemy.shield<enemy.max_shield:
                        enemy.shield+=self.shield_regen
                        if enemy.shield>enemy.max_shield:
                            enemy.shield=enemy.max_shield
        else:
            self.counter_delay+=1

    def draw_health_bar(self,surface):
        rect=pg.Surface((round(self.health/self.max_health,1)*self.health_bar_width,self.health_bar_height))
        rect.fill(GREEN)
        health_bar_pos=(self.x-self.half_health_bar_width,self.y-self.width-self.health_bar_height)
        surface.blit(self.red_health_bar,health_bar_pos)
        surface.blit(rect,health_bar_pos)

    def set_center_area(self):
        self.rect_area_regen.x=self.x-self.half_width_area_regen
        self.rect_area_regen.y = self.y - self.half_width_area_regen

    @staticmethod
    def scaling_attributes(width_road,width_enemy):
        width=round(width_enemy*1.5,1)
        img = pg.transform.scale(enemy3, (width, width))
        img1=pg.transform.scale(enemy3, (width*1.5, width*1.5))
        shield=pg.transform.scale(Enemy.shield, (round(width*1.7,1), round(width*1.7,1)))
        Enemy5.image = img
        Enemy5.image_for_selected=img1
        Enemy5.shield=shield
        Enemy5.speed = round(width_road/110,1)
        Enemy5.width=width
        Enemy5.half_width=round(width/2,1)
        Enemy5.health_bar_width=round(width/1.2,1)
        Enemy5.half_health_bar_width=round(Enemy5.health_bar_width/2,1)
        Enemy5.health_bar_height=round(width_enemy/10,1)
        Enemy5.red_health_bar=pg.Surface((Enemy5.health_bar_width,Enemy5.health_bar_height))
        Enemy5.red_health_bar.fill(RED)
