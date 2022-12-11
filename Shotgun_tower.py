from Tower import BasicTower
from Bullets_shotgun import BulletShotgun
import pygame as pg
import math
tower_image1=pg.image.load("images/Shotgun_images/tower2_level1.png").convert()
tower_image2=pg.image.load("images/Shotgun_images/tower2_level2.png").convert()
tower_image3=pg.image.load("images/Shotgun_images/tower2_level3.png").convert()
tower_path1_image1=pg.image.load("images/Shotgun_images/tower2_path1_level1.png").convert()
tower_path1_image2=pg.image.load("images/Shotgun_images/tower2_path1_level2.png").convert()
tower_path1_image3=pg.image.load("images/Shotgun_images/tower2_path1_level3.png").convert()
tower_path2_image1=pg.image.load("images/Shotgun_images/tower2_path2_level1.png").convert()
tower_path2_image2=pg.image.load("images/Shotgun_images/tower2_path2_level2.png").convert()
tower_path2_image3=pg.image.load("images/Shotgun_images/tower2_path2_level3.png").convert()
tower_image1.set_colorkey((255, 255, 255))
tower_image2.set_colorkey((255, 255, 255))
tower_image3.set_colorkey((255, 255, 255))
tower_path1_image1.set_colorkey((255, 255, 255))
tower_path1_image2.set_colorkey((255, 255, 255))
tower_path1_image3.set_colorkey((255, 255, 255))
tower_path2_image1.set_colorkey((255, 255, 255))
tower_path2_image2.set_colorkey((255, 255, 255))
tower_path2_image3.set_colorkey((255, 255, 255))
Yellow=(255,255,0)


class Shotgun(BasicTower):
    tower_image=None
    name='Дробовик'
    damage_list=[10,15,22,(60,30),(80,40),(115,50)]
    fire_rate_list=[90,90,90,(150,130),(150,130),(150,130)]
    range_list=[]
    punching_list=[0.3,0.4,0.55,(0,0.2),(0,0.2),(0,0.2)]
    damage_shield_list=[0.2,0.25,0.3,(0.15,0),(0.15,0),(0.15,0)]
    destruction_armor_list=[0,0,0,(0,0.004),(0,0.006),(0,0.008)]
    color_bullet_list=[Yellow,Yellow,Yellow,Yellow,Yellow,Yellow]
    image_list=[]
    speed_bullet=None
    size_bullet=None
    count_fraction_list=[8,12,12,(14,13),(17,15),(20,17)]
    cost_list=[150,350,400,700,1000,1300]
    fraction=[-0.2,0.2,-0.4,0.4,-0.1,0.1,-0.3,0.3,-0.15,0.15,-0.25,0.25,-0.12,0.12,-0.22,0.22,-0.06,0.06,-0.17,0.17]

    def __init__(self,x,y,surface):
        self.path=None
        self.damage=self.damage_list[0]
        self.fire_rate = self.fire_rate_list[0]
        self.punching = self.punching_list[0]
        self.damage_shield = self.damage_shield_list[0]
        self.color_bullet = self.color_bullet_list[0]
        self.count_fraction = self.count_fraction_list[0]
        self.destruction_armor=self.destruction_armor_list[0]
        super().__init__(x,y,surface,self.image_list[0],self.range_list[0],self.cost_list[0])

    def upgrade(self):
        self.number_upgrade += 1
        if not self.path:
            self.image=self.image_list[self.number_upgrade]
            self.radius=self.range_list[self.number_upgrade]
            self.cost_upgrade=self.cost_list[self.number_upgrade]
            super().upgrade()
            self.damage=self.damage_list[self.number_upgrade]
            self.fire_rate = self.fire_rate_list[self.number_upgrade]
            self.punching = self.punching_list[self.number_upgrade]
            self.damage_shield = self.damage_shield_list[self.number_upgrade]
            self.color_bullet = self.color_bullet_list[self.number_upgrade]
            self.count_fraction=self.count_fraction_list[self.number_upgrade]
        else:
            path=self.path-1
            self.image=self.image_list[self.number_upgrade][path]
            self.radius=self.range_list[self.number_upgrade]
            self.cost_upgrade=self.cost_list[self.number_upgrade]
            super().upgrade()
            self.damage=self.damage_list[self.number_upgrade][path]
            self.fire_rate = self.fire_rate_list[self.number_upgrade][path]
            self.punching = self.punching_list[self.number_upgrade][path]
            self.damage_shield = self.damage_shield_list[self.number_upgrade][path]
            self.color_bullet = self.color_bullet_list[self.number_upgrade]
            self.count_fraction=self.count_fraction_list[self.number_upgrade][path]
            self.destruction_armor = self.destruction_armor_list[self.number_upgrade][path]

    @staticmethod
    def get_cost_tower():
        return Shotgun.cost_list[0]

    def get_cost_upgrade(self):
        return self.cost_list[self.number_upgrade+1]

    def ready_shot(self,wave):
        if self.delay == self.fire_rate:
            self.find_target(wave)
            self.delay=0
            if self.target:
                return True

    def attack(self,wave,bullets):
        if self.ready_shot(wave):
            angle,sin,cos=self.rotation()
            x = self.x + self.half_width * math.cos(angle)
            y = self.y - self.half_height * math.sin(angle)
            bullets.append(BulletShotgun(self,x, y, sin, cos))
            for i in range(self.count_fraction):
                rad=angle+Shotgun.fraction[i]
                bullets.append(BulletShotgun(self,x, y, math.sin(rad), math.cos(rad)))
            self.delay=0
        self.delay += 1

    @staticmethod
    def scaling_attributes(width_tower,height_tower,w,h):
        width=width_tower
        height=height_tower
        image1 = pg.transform.scale(tower_image1, (width, height))
        image2 = pg.transform.scale(tower_image2, (width, height))
        image3=pg.transform.scale(tower_image3, (width, height))
        path1_image1=pg.transform.scale(tower_path1_image1, (width, height))
        path1_image2 = pg.transform.scale(tower_path1_image2, (width, height))
        path1_image3 = pg.transform.scale(tower_path1_image3, (width, height))
        path2_image1=pg.transform.scale(tower_path2_image1, (width, height))
        path2_image2 = pg.transform.scale(tower_path2_image2, (width, height))
        path2_image3 = pg.transform.scale(tower_path2_image3, (width, height))
        range1=round(w/9,1)
        Shotgun.size_bullet=round(width/20)
        Shotgun.speed_bullet = round(w * h / 440000, 1)
        Shotgun.tower_image = image1
        Shotgun.image_list = []
        Shotgun.image_list.append(image1)
        Shotgun.image_list.append(image2)
        Shotgun.image_list.append(image3)
        Shotgun.image_list.append((path1_image1,path2_image1))
        Shotgun.image_list.append((path1_image2,path2_image2))
        Shotgun.image_list.append((path1_image3,path2_image3))
        Shotgun.range_list = []
        Shotgun.range_list.append(range1)
        Shotgun.range_list.append(range1)
        Shotgun.range_list.append(round(range1*1.1,1))
        Shotgun.range_list.append(round(range1*1.2,1))
        Shotgun.range_list.append(round(range1*1.2,1))
        Shotgun.range_list.append(round(range1*1.3,1))
