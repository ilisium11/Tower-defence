import pygame as pg
import math
from enemy4 import Enemy4
from enemy5 import Enemy5
Aqua=(0,255,255)


class BasicTower:
    half_width=None
    half_height=None
    width=None
    height=None
    upgrades_tower1=None

    def __init__(self, x, y, surface,image,radius,cost):
        self.number_upgrade = 0
        self.radius = radius
        self.image=image
        self.cost_upgrade=cost
        self.start_cost = cost
        radius = self.radius
        self.circle = pg.Surface((radius*2, radius*2), pg.SRCALPHA)
        pg.draw.circle(self.circle, (*Aqua, 180), (radius, radius), radius)
        self.q=self.image
        self.delay=0
        self.x = x
        self.y = y
        self.target = None
        self.surface = surface
        self.find_target=self.find_enemy
        self.number_alg=0
        self.rect=pg.Rect(self.x-BasicTower.half_width,self.y-BasicTower.half_width,self.width,self.width)

    def upgrade(self):
        self.start_cost += self.cost_upgrade
        radius = self.radius
        self.circle = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.circle, (*Aqua, 180), (radius, radius), radius)
        self.q = self.image
        self.delay = 0

    def get_cost_upgrade(self):
        return self.upgrades_tower1[self.number_upgrade+1][-1]

    def get_circle(self):
        return self.circle

    def get_rect(self):
        return pg.Rect(self.x-BasicTower.half_width,self.y-BasicTower.half_width,self.width,self.width)

    def set_target(self,target):
        self.target=target

    def rotation(self):
        b = self.y - self.target.y
        c = self.target.x - self.x
        hypot = math.sqrt(b * b + c * c)
        if self.radius >= hypot:
            sin_x = b / hypot
            cos_x=c/hypot
            angle = math.degrees(math.asin(sin_x))
            if self.target.x > self.x:
                self.q = pg.transform.rotate(self.image, angle - 90)
                angle=math.radians(angle)
            else:
                self.q = pg.transform.rotate(self.image, 90 - angle)
                angle = math.radians(180-angle)
            return angle,sin_x,cos_x

    def find_enemy1(self,wave):
        min_rast=100000
        x1, y1 = self.x, self.y
        radius = self.radius
        target=None
        for enemy in wave:
            x, y = enemy.x, enemy.y
            rast = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y)
            if radius * radius >= rast:
                if rast<min_rast:
                    min_rast=rast
                    target=enemy
        self.set_target(target)

    def find_enemy(self,wave):
        min_rast = 100000
        x1, y1 = self.x, self.y
        radius = self.radius
        target=None
        for enemy in wave:
            x, y = enemy.x, enemy.y
            rast = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y)
            if radius * radius >= rast:
                if enemy.distance_to_end<min_rast:
                    min_rast=enemy.distance_to_end
                    target=enemy
        self.set_target(target)
    
    def find_enemy2(self,wave):
        x1, y1 = self.x, self.y
        radius = self.radius
        target=None
        points=0
        for enemy in wave:
            x, y = enemy.x, enemy.y
            rast = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y)
            if radius * radius >= rast:
                if enemy.health>points:
                    points=enemy.health
                    target=enemy
        self.set_target(target)

    def find_enemy3(self, wave):
        x1, y1 = self.x, self.y
        radius = self.radius
        target = None
        target1=None
        points = 0
        min_rast=10000
        for enemy in wave:
            x, y = enemy.x, enemy.y
            rast = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y)
            if radius * radius >= rast:
                if enemy.shield > points:
                    points = enemy.shield
                    target = enemy
                elif enemy.distance_to_end<min_rast:
                    min_rast=enemy.distance_to_end
                    target1=enemy
        if target:
            self.set_target(target)
        else:
            self.set_target(target1)

    def find_enemy4(self, wave):
        x1, y1 = self.x, self.y
        radius = self.radius
        target = None
        target1 = None
        points = 0
        min_rast=10000
        for enemy in wave:
            x, y = enemy.x, enemy.y
            rast = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y)
            if radius * radius >= rast:
                if type(enemy)==Enemy4:
                    if enemy.max_health>points:
                        points=enemy.max_health
                        target=enemy
                elif enemy.distance_to_end<min_rast:
                    min_rast=enemy.distance_to_end
                    target1=enemy
        if target:
            self.set_target(target)
        else:
            self.set_target(target1)

    def find_enemy5(self, wave):
        x1, y1 = self.x, self.y
        radius = self.radius
        target = None
        target1 = None
        points = 0
        min_rast=10000
        for enemy in wave:
            x, y = enemy.x, enemy.y
            rast = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y)
            if radius * radius >= rast:
                if type(enemy)==Enemy5:
                    if enemy.max_health>points:
                        points=enemy.max_health
                        target=enemy
                elif enemy.distance_to_end<min_rast:
                    min_rast=enemy.distance_to_end
                    target1=enemy
        if target:
            self.set_target(target)
        else:
            self.set_target(target1)

    def draw(self,surface):
        center = self.q.get_rect(center=(self.x, self.y))
        surface.blit(self.q, center)
