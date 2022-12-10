from Tower import BasicTower
from Bullets_turret import BulletTurret
import pygame as pg
import math
tower_image1=pg.image.load("images/Turret_images/tower1_level1.png").convert()
tower_image2=pg.image.load("images/Turret_images/tower1_level2.png").convert()
tower_image3=pg.image.load("images/Turret_images/tower1_level3.png").convert()
tower_path1_image1=pg.image.load("images/Turret_images/tower1_path1_level1.png").convert()
tower_path1_image2=pg.image.load("images/Turret_images/tower1_path1_level2.png").convert()
tower_path1_image3=pg.image.load("images/Turret_images/tower1_path1_level3.png").convert()
tower_path2_image1=pg.image.load("images/Turret_images/tower1_path2_level1.png").convert()
tower_path2_image2=pg.image.load("images/Turret_images/tower1_path2_level2.png").convert()
tower_path2_image3=pg.image.load("images/Turret_images/tower1_path2_level3.png").convert()
tower_image1.set_colorkey((255,255,255))
tower_image2.set_colorkey((255, 255, 255))
tower_image3.set_colorkey((255,255,255))
tower_path1_image1.set_colorkey((255, 255, 255))
tower_path1_image2.set_colorkey((255,255,255))
tower_path1_image3.set_colorkey((255, 255, 255))
tower_path2_image1.set_colorkey((255, 255, 255))
tower_path2_image2.set_colorkey((255,255,255))
tower_path2_image3.set_colorkey((255, 255, 255))
RED=(255,0,0)


class Turret(BasicTower):
    tower_image = None
    name='Турель'
    damage_list=[40,40,60,(200,180),(300,280),(400,360)]
    fire_rate_list=[60,60,60,(60,60),(55,55),(50,50)]
    range_list=[]
    punching_list=[0,0.2,0.3,(0.7,0.2),(0.8,0.2),(1,0.2)]
    damage_shield_list=[0.4,0.5,0.5,(0.2,0.8),(0.2,1),(0.2,1.3)]
    color_bullet_list=[RED,RED,RED,RED,RED,RED]
    image_list=[]
    speed_bullet=None
    size_bullet=None
    guns_list=[]
    cost_list=[100,150,200,500,700,1000]

    def __init__(self,x,y,surface):
        self.path=None
        self.damage=self.damage_list[0]
        self.fire_rate = self.fire_rate_list[0]
        self.punching = self.punching_list[0]
        self.damage_shield = self.damage_shield_list[0]
        self.color_bullet = self.color_bullet_list[0]
        self.guns=self.guns_list[0]
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
            self.guns=self.guns_list[self.number_upgrade]
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

    @staticmethod
    def get_cost_tower():
        return Turret.cost_list[0]

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
            for angle1 in self.guns:
                x = self.x + self.half_height * math.cos(angle + angle1)
                y = self.y - self.half_height * math.sin(angle + angle1)
                bullets.append(BulletTurret(self, x, y,sin,cos))
            self.delay=0
        self.delay += 1

    @staticmethod
    def scaling_attributes(width_tower,height_tower,w,h):
        width=width_tower
        height=height_tower
        BasicTower.half_width = round(width/2,1)
        BasicTower.half_height=round(height_tower/2,1)
        BasicTower.width = width
        BasicTower.height=height
        image1=pg.transform.scale(tower_image1,(width,height))
        image2 = pg.transform.scale(tower_image2, (width, height))
        image3 = pg.transform.scale(tower_image3, (width, height))
        path1_image1=pg.transform.scale(tower_path1_image1,(width,height))
        path1_image2 = pg.transform.scale(tower_path1_image2, (width, height))
        path1_image3 = pg.transform.scale(tower_path1_image3, (width, height))
        path2_image1=pg.transform.scale(tower_path2_image1,(width,height))
        path2_image2 = pg.transform.scale(tower_path2_image2, (width, height))
        path2_image3 = pg.transform.scale(tower_path2_image3, (width, height))
        range1 = round(w/5.7, 1)
        Turret.size_bullet = round(width / 25)
        Turret.speed_bullet=round(w*h/200000,1)
        Turret.tower_image = image1
        Turret.image_list = []
        Turret.image_list.append(image1)
        Turret.image_list.append(image2)
        Turret.image_list.append(image3)
        Turret.image_list.append((path1_image1,path2_image1))
        Turret.image_list.append((path1_image2,path2_image2))
        Turret.image_list.append((path1_image3,path2_image3))
        Turret.range_list = []
        Turret.range_list.append(range1)
        Turret.range_list.append(round(range1*1.1,1))
        Turret.range_list.append(round(range1 * 1.25, 1))
        Turret.range_list.append(round(range1 * 1.3, 1))
        Turret.range_list.append(round(range1 * 1.4, 1))
        Turret.range_list.append(round(range1 * 1.4, 1))
        x_pos_gun1=round(width*0.631,1)
        x_pos_gun2=round(width*0.371,1)
        angle_double_gun1=math.sin((x_pos_gun1-BasicTower.half_width)/BasicTower.half_height)
        angle_double_gun2 = math.sin((x_pos_gun2 - BasicTower.half_width) / BasicTower.half_height)
        Turret.guns_list.append([0])
        Turret.guns_list.append([angle_double_gun1,angle_double_gun2])
        Turret.guns_list.append([angle_double_gun1, angle_double_gun2])
        Turret.guns_list.append([angle_double_gun1,angle_double_gun2])
        Turret.guns_list.append([angle_double_gun1, angle_double_gun2])
        Turret.guns_list.append([angle_double_gun1, angle_double_gun2])
