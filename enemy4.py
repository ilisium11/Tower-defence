import pygame as pg
from enemy import Enemy
enemy4=pg.image.load("images/enemy_images/enemy4.png").convert()
enemy4.set_colorkey((255,255,255))
RED=(255,0,0)
GREEN=(0,255,0)


class Enemy4(Enemy):
    image=None
    image_for_selected = None
    width=None
    half_width=None
    health=[3000,12000,48000]
    health_regen=[10,40,120]
    shield_points=[500,2000,8000]
    cost_money=[180,540,1800]
    cost_health=5
    armor=[0.6,0.8,0.95]
    speed=None
    shield=None
    health_bar_width=None
    half_health_bar_width=None
    health_bar_height=None
    red_health_bar=None

    def __init__(self,level,shield=None):
        super().__init__(Enemy4.speed,Enemy4.image)
        level = level - 1
        self.level = level
        self.health=Enemy4.health[level]
        self.max_health = self.health
        self.health_regen=Enemy4.health_regen[level]
        self.armor = Enemy4.armor[level]
        self.shield=0
        self.max_shield=0
        if shield:
            self.shield_img=Enemy4.shield
            self.shield=Enemy4.shield_points[level]
            self.max_shield=self.shield
        self.cost_money=Enemy4.cost_money[level]
        self.cost_hp=Enemy4.cost_health
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
                    if enemy.health<enemy.max_health:
                        enemy.health+=self.health_regen
                        if enemy.health>enemy.max_health:
                            enemy.health=enemy.max_health
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
        img = pg.transform.scale(enemy4, (width, width))
        img1=pg.transform.scale(enemy4, (width*1.5, width*1.5))
        shield=pg.transform.scale(Enemy.shield, (round(width*1.7,1), round(width*1.7,1)))
        Enemy4.image = img
        Enemy4.image_for_selected=img1
        Enemy4.shield=shield
        Enemy4.speed = round(width_road/110,1)
        Enemy4.width=width
        Enemy4.half_width=round(width/2,1)
        Enemy4.health_bar_width=round(width/1.2,1)
        Enemy4.half_health_bar_width=round(Enemy4.health_bar_width/2,1)
        Enemy4.health_bar_height=round(width_enemy/10,1)
        Enemy4.red_health_bar=pg.Surface((Enemy4.health_bar_width,Enemy4.health_bar_height))
        Enemy4.red_health_bar.fill(RED)
