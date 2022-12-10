import pygame as pg


class Enemy:
    shield = pg.image.load('images/shield2.png').convert()
    shield.set_colorkey((255,255,255))
    width=None
    half_width=None

    def __init__(self,speed,image):
        self.speed = speed
        self.half_speed = round(speed/1.1,1)
        self.image = image
        self.pos_path = 1
        self.x = 0
        self.y = 0
        self.path = None
        self.position_path = None
        self.direction = None
        self.lower_border = None
        self.upper_border = None
        self.center = None
        self.len_path = None
        self.local_speed = None
        self.rect = None
        self.shield_img=None
        self.center_shield=None
        self.distance_to_end=0

    def run(self,*args):
        self.path[self.position_path][self.direction] += self.local_speed
        self.set_center(self.path[self.position_path][0], self.path[self.position_path][1])
        self.distance_to_end-=self.speed
        if self.lower_border < self.path[self.position_path][self.direction] < self.upper_border:
            self.direction = abs(self.direction - 1)
            self.position_path += 1
            if self.position_path == self.len_path - 1:
                return True
            a = self.direction
            s = self.path
            b = self.position_path
            self.lower_border = self.path[self.position_path + 1][self.direction] - self.half_speed
            self.upper_border = self.path[self.position_path + 1][self.direction] + self.half_speed
            if s[b][a] - s[b + 1][a] < 0:
                self.local_speed = self.speed
            else:
                self.local_speed = -self.speed

    def draw(self,surface):
        if self.shield_img:
            surface.blit(self.shield_img, self.center_shield)
        surface.blit(self.image,self.center)

    def set_center(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x - self.half_width
        self.rect.y = y - self.half_width
        self.center = self.image.get_rect(center=(x, y))
        if self.shield_img:
            self.center_shield=self.shield_img.get_rect(center=(x,y))

    def set_pos_path(self, pos_path):
        self.pos_path = pos_path

    def get_pos_path(self):
        return self.pos_path
