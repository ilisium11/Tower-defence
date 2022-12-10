from Tower import BasicTower
import pygame as pg
import math
tower_image1=pg.image.load("images/Laser_images/laser_level1.png").convert()
tower_image2=pg.image.load("images/Laser_images/laser_level2.png").convert()
tower_image3=pg.image.load("images/Laser_images/laser_level3.png").convert()
tower_path1_image1=pg.image.load("images/Laser_images/laser_path2_level1.png").convert()
tower_path1_image2=pg.image.load("images/Laser_images/laser_path2_level2.png").convert()
tower_path1_image3=pg.image.load("images/Laser_images/laser_path2_level3.png").convert()
tower_path2_image1=pg.image.load("images/Laser_images/laser_path1_level1.png").convert()
tower_path2_image2=pg.image.load("images/Laser_images/laser_path1_level2.png").convert()
tower_path2_image3=pg.image.load("images/Laser_images/laser_path1_level3.png").convert()
tower_image1.set_colorkey((255,255,255))
tower_image2.set_colorkey((255, 255, 255))
tower_image3.set_colorkey((255,255,255))
tower_path1_image1.set_colorkey((255, 255, 255))
tower_path1_image2.set_colorkey((255,255,255))
tower_path1_image3.set_colorkey((255, 255, 255))
tower_path2_image1.set_colorkey((255,255,255))
tower_path2_image2.set_colorkey((255, 255, 255))
tower_path2_image3.set_colorkey((255,255,255))
RED=(255,0,0)
Yellow=(210,210,0)
Blue=(0,50,200)


class Laser(BasicTower):
    tower_image = None
    name='Лазер'
    damage_list=[(2,12),(4,24),(6,34),((10,80),(15,55)),((30,150),(40,100)),((80,350),(70,190))]
    kindling_speed_list=[0.5,0.5,0.5,(1,2),(1.5,2.5),(1.5,3)]
    fire_rate=6
    punching=1
    range_list=[]
    damage_shield_list=[0.8,1,1.2,1.2,1.3,1.5]
    image_list=[]
    cost_list=[350,400,500,1000,1400,1800]

    def __init__(self,x,y,surface):
        self.path=None
        self.min_damage=self.damage_list[0][0]
        self.damage=self.min_damage
        self.max_damage=self.damage_list[0][1]
        self.kindling_speed = self.kindling_speed_list[0]
        self.delay_find_target=60
        self.counter_delay_damage=0
        self.damage_shield = self.damage_shield_list[0]
        super().__init__(x,y,surface,self.image_list[0],self.range_list[0],self.cost_list[0])
        self.x_gun=self.x
        self.y_gun=self.y-self.half_height

    def upgrade(self):
        self.number_upgrade += 1
        if not self.path:
            self.image=self.image_list[self.number_upgrade]
            self.radius=self.range_list[self.number_upgrade]
            self.cost_upgrade=self.cost_list[self.number_upgrade]
            super().upgrade()
            self.kindling_speed = self.kindling_speed_list[self.number_upgrade]
            self.min_damage=self.damage_list[self.number_upgrade][0]
            self.damage=self.min_damage
            self.max_damage=self.damage_list[self.number_upgrade][1]
            self.damage_shield = self.damage_shield_list[self.number_upgrade]
        else:
            path=self.path-1
            self.image=self.image_list[self.number_upgrade][path]
            self.radius=self.range_list[self.number_upgrade]
            self.cost_upgrade=self.cost_list[self.number_upgrade]
            super().upgrade()
            self.kindling_speed = self.kindling_speed_list[self.number_upgrade][path]
            self.min_damage=self.damage_list[self.number_upgrade][path][0]
            self.damage=self.min_damage
            self.max_damage=self.damage_list[self.number_upgrade][path][1]
            self.damage_shield = self.damage_shield_list[self.number_upgrade]

    @staticmethod
    def get_cost_tower():
        return Laser.cost_list[0]

    def get_cost_upgrade(self):
        return self.cost_list[self.number_upgrade+1]

    def ready_shot(self,wave):
        if self.delay == self.delay_find_target:
            target=self.target
            self.find_target(wave)
            if not target==self.target:
                self.damage=self.min_damage
            self.delay=0
        else:
            self.delay+=1

    def delay_damage(self):
        if self.counter_delay_damage == self.fire_rate:
            self.counter_delay_damage = 0
            if self.damage<self.max_damage:
                self.damage+=self.kindling_speed
            return True
        else:
            self.counter_delay_damage+=1

    def attack(self,wave,list_killed_enemy):
        self.ready_shot(wave)
        if self.target:
            if self.target in wave:
                attr=self.rotation()
                if attr:
                    angle=attr[0]
                    self.x_gun = self.x + self.half_height * math.cos(angle)
                    self.y_gun = self.y - self.half_height * math.sin(angle)
                    if self.delay_damage():
                        if self.target.shield>0:
                            self.target.shield-=self.damage * self.damage_shield
                            if self.target.shield<=0:
                                self.target.shield = 0
                                self.target.shield_img = None
                        else:
                            self.target.health-=self.damage
                            if self.target.health<=0:
                                self.target.health=0
                                wave.remove(self.target)
                                list_killed_enemy.append(self.target)
            else:
                self.target=None

    def draw(self,surface):
        if self.target:
            pg.draw.line(self.surface, Blue, (self.x_gun, self.y_gun), (self.target.x, self.target.y), 8)
        super().draw(surface)

    @staticmethod
    def scaling_attributes(width_tower,height_tower,w,h):
        width=width_tower
        height=height_tower
        image1=pg.transform.scale(tower_image1,(width,height))
        image2 = pg.transform.scale(tower_image2, (width, height))
        image3=pg.transform.scale(tower_image3,(width,height))
        path1_image1 = pg.transform.scale(tower_path1_image1, (width, height))
        path1_image2=pg.transform.scale(tower_path1_image2,(width,height))
        path1_image3 = pg.transform.scale(tower_path1_image3, (width, height))
        path2_image1 = pg.transform.scale(tower_path2_image1, (width, height))
        path2_image2=pg.transform.scale(tower_path2_image2,(width,height))
        path2_image3 = pg.transform.scale(tower_path2_image3, (width, height))
        range1 = round(w/4.5, 1)
        Laser.tower_image = image1
        Laser.image_list.append(image1)
        Laser.image_list.append(image2)
        Laser.image_list.append(image3)
        Laser.image_list.append((path1_image1,path2_image1))
        Laser.image_list.append((path1_image2, path2_image2))
        Laser.image_list.append((path1_image3, path2_image3))
        Laser.range_list.append(range1)
        Laser.range_list.append(round(range1*1.1,1))
        Laser.range_list.append(round(range1*1.1,1))
        Laser.range_list.append(round(range1*1.2,1))
        Laser.range_list.append(round(range1*1.3,1))
        Laser.range_list.append(round(range1 * 1.5, 1))
