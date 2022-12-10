import pygame as pg
Brown=(210, 180, 140)
Black=(0,0,0)
Red=(139,0,0)
Blue=(65,105,205)
White=(220,220,220)
Green=(34,139,34)
Area=pg.image.load('images/selected_enemy.png').convert()


class SelectedEnemy:
    font=None
    area=None
    width = None
    height = None
    pos=None
    length_bar=None
    thickness = None
    bar_pos_x=None
    health_bar_pos_y=None
    shield_bar_pos_y=None
    health_bar_center=None
    shield_bar_center=None
    image_pos=None
    name_pos = None
    first_text_pos_y = None
    text_pos_x=None
    difference_text_y=None

    def __init__(self,surface,enemy):
        self.surface=surface
        self.enemy=enemy
        self.area=SelectedEnemy.area.copy()
        self.image=type(enemy).image_for_selected
        self.max_health=enemy.max_health
        self.old_health=0
        self.max_shield=enemy.max_shield
        self.old_shield = 0
        self.armor_text=self.font.render('Броня '+str(enemy.armor*100)+"%",True,Black)
        self.cost_money_text=self.font.render('Стоимость '+str(enemy.cost_money),True,Black)
        self.cost_hp_text=self.font.render('Здоровье '+str(enemy.cost_hp),True,Black)
        self.level_text=self.font.render('Уровень  '+str(enemy.level+1),True,Black)
        self.area.blit(self.armor_text, self.image.get_rect(center=(self.text_pos_x,self.first_text_pos_y)))
        self.area.blit(self.cost_money_text, self.image.get_rect(center=(self.text_pos_x,self.first_text_pos_y+self.difference_text_y)))
        self.area.blit(self.cost_hp_text, self.image.get_rect(center=(self.text_pos_x,self.first_text_pos_y+2*self.difference_text_y)))
        self.area.blit(self.level_text, self.image.get_rect(center=(self.text_pos_x, self.first_text_pos_y+3*self.difference_text_y)))
        self.area.blit(self.image,self.image.get_rect(center=SelectedEnemy.image_pos))

    def draw(self):
        if not (self.old_health==self.enemy.health):
            self.old_health=self.enemy.health
            pg.draw.rect(self.area, Red, (self.bar_pos_x, self.health_bar_pos_y, self.length_bar, self.thickness))
            length=round((self.enemy.health/self.max_health)*self.length_bar)
            pg.draw.rect(self.area,Green,(self.bar_pos_x,self.health_bar_pos_y,length,self.thickness))
            text=self.font.render(str(int(self.enemy.health))+'/'+str(self.max_health),Black,True)
            self.area.blit(text,text.get_rect(center=self.health_bar_center))
        else:
            if self.enemy.health==0:
                return True
        if not (self.old_shield==self.enemy.shield):
            self.old_shield=self.enemy.shield
            pg.draw.rect(self.area, White, (self.bar_pos_x, self.shield_bar_pos_y, self.length_bar, self.thickness))
            length = round((self.enemy.shield / self.max_shield) * self.length_bar)
            pg.draw.rect(self.area, Blue,(self.bar_pos_x, self.shield_bar_pos_y, length, self.thickness))
            text=self.font.render(str(int(self.enemy.shield))+'/'+str(self.max_shield),Black,True)
            self.area.blit(text,text.get_rect(center=self.shield_bar_center))
        self.surface.blit(self.area,self.pos)

    @staticmethod
    def scaling_attributes(w,h):
        SelectedEnemy.width=round(w/6,1)
        SelectedEnemy.height = round(h / 6, 1)
        SelectedEnemy.pos=(0,round(h-SelectedEnemy.height,1))
        SelectedEnemy.area=pg.transform.scale(Area,(SelectedEnemy.width,SelectedEnemy.height))
        SelectedEnemy.length_bar=round(SelectedEnemy.width/1.12,1)
        SelectedEnemy.thickness=round(SelectedEnemy.height/10,1)
        bar_center_x=round(SelectedEnemy.width/2,1)
        SelectedEnemy.bar_pos_x=round(bar_center_x-SelectedEnemy.length_bar/2,1)
        health_bar_center_y=round(SelectedEnemy.height/10,1)
        shield_bar_center_y=health_bar_center_y+SelectedEnemy.thickness*1.5
        SelectedEnemy.health_bar_pos_y=health_bar_center_y
        SelectedEnemy.shield_bar_pos_y=shield_bar_center_y
        SelectedEnemy.health_bar_center=(bar_center_x,health_bar_center_y+round(SelectedEnemy.thickness/2,1))
        SelectedEnemy.shield_bar_center = (bar_center_x, shield_bar_center_y+round(SelectedEnemy.thickness/2,1))
        SelectedEnemy.font=pg.font.Font('font1/font.ttf',round(SelectedEnemy.thickness/1.2))
        SelectedEnemy.image_pos=(round(SelectedEnemy.width/5,1),round(SelectedEnemy.height/1.5,1))
        SelectedEnemy.first_text_pos_y = round(SelectedEnemy.height/2,1)
        SelectedEnemy.text_pos_x = round(SelectedEnemy.width/2.2,1)
        SelectedEnemy.difference_text_y = round(SelectedEnemy.height/7,1)
