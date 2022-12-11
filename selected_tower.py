import pygame as pg
from button import TextButton,AlgButton
area=pg.image.load('images/Selected_tower_prot.png').convert()
upgrade_button=pg.image.load("images/upgrade_button.png").convert()
algoritm_buttons=pg.image.load('images/algoritm_buttons.png').convert()
algoritm_buttons1=pg.image.load('images/algoritm_buttons1.png').convert()
algoritm_button=pg.image.load('images/algoritm_button.png').convert()
algoritm_button1=pg.image.load('images/algoritm_button1.png').convert()
ORANGE=(190,135,0)
Black=(0,0,0)


class SelectedTower:
    area=None
    upg_button_img=None
    choice_button_img=None
    alg_buttons_img=None
    alg_buttons1_img = None
    alg_button_img=None
    alg_button1_img=None
    image_pos=None
    name_pos = None
    text_x=None
    first_text_y=None
    difference_text_y=None
    font_button=None
    font_name=None
    font_text=None
    upgrade_button_pos=None
    choice1_button_pos=None
    choice2_button_pos = None
    first_alg_button_y=None
    sell_button_pos = None

    def __init__(self,surface,tower):
        self.surface=surface
        self.area = SelectedTower.area.copy()
        self.width=self.area.get_width()
        self.height = self.area.get_height()
        self.alg_button=TextButton((self.width/2,self.first_alg_button_y), self.alg_button_img,self.surface,self.font_button, "Выбор цели")
        self.alg_button_pressed=None
        self.alg_buttons=[]
        self.alg_buttons.append(AlgButton((self.width/2,self.first_alg_button_y+self.alg_button.height), SelectedTower.alg_buttons_img,self.surface,self.font_button, 'Ближайшая к выходу',tower.find_enemy))
        self.alg_buttons.append(AlgButton((self.width/2, self.first_alg_button_y + 2*self.alg_button.height), SelectedTower.alg_buttons_img, self.surface,self.font_button, 'Ближайшая к башне', tower.find_enemy1))
        self.alg_buttons.append(AlgButton((self.width/2,self.first_alg_button_y+3*self.alg_button.height), SelectedTower.alg_buttons_img,self.surface,self.font_button, 'Наибольшее здоровье',tower.find_enemy2))
        self.alg_buttons.append(AlgButton((self.width/2, self.first_alg_button_y + 4*self.alg_button.height), SelectedTower.alg_buttons_img, self.surface,self.font_button, 'Наибольший щит', tower.find_enemy3))
        self.alg_buttons.append(AlgButton((self.width/2,self.first_alg_button_y+5*self.alg_button.height), SelectedTower.alg_buttons_img,self.surface,self.font_button, 'Генераторы здоровья',tower.find_enemy4))
        self.alg_buttons.append(AlgButton((self.width/2, self.first_alg_button_y + 6*self.alg_button.height), SelectedTower.alg_buttons_img, self.surface,self.font_button, 'Генераторы щитов', tower.find_enemy5))
        for i in range(len(self.alg_buttons)):
            if self.alg_buttons[i].algoritm==tower.find_target:
                self.alg_buttons[i].image=SelectedTower.alg_buttons1_img
                self.alg_buttons_pressed = self.alg_buttons[i]
        self.sell_button = TextButton(self.sell_button_pos, self.upg_button_img,self.area,self.font_button, "Продать")
        if tower.number_upgrade + 1 == 3 and not tower.path:
            self.choice_button=[]
            self.choice_button.append(TextButton(self.choice1_button_pos, SelectedTower.choice_button_img,self.area,self.font_button, "Развитие I"))
            self.choice_button.append(TextButton(self.choice2_button_pos, SelectedTower.choice_button_img, self.area, self.font_button, "Развитие II"))
            self.choice_button[0].draw()
            self.choice_button[1].draw()
        elif tower.number_upgrade + 1 < 6:
            self.cost_upgrade = tower.get_cost_upgrade()
            self.upg_button=TextButton(self.upgrade_button_pos, self.upg_button_img,self.area,self.font_button, "Улучшить "+str(self.cost_upgrade)+"")
            self.upg_button.draw()
        else:
            self.upg_button=None
        self.sell_button.draw()
        self.x=0
        self.y=0
        self.tower = tower
        self.level = tower.number_upgrade
        self.start_cost = tower.start_cost
        self.circle=tower.circle.copy()
        self.center=self.circle.get_rect(center=(tower.x,tower.y))
        image = pg.transform.scale(tower.image,(tower.width*1.5,tower.height*1.5))
        name = tower.name
        name_text=self.font_name.render(name,True,ORANGE)
        if hasattr(tower, 'min_damage'):
            damage_text=self.font_text.render("Урон  "+str(tower.min_damage*10)+"-"+str(tower.max_damage*10)+"",True,Black)
        else:
            damage_text=self.font_text.render("Урон  "+str(tower.damage)+"",True,Black)
        level_text = self.font_text.render("Уровень  " + str(tower.number_upgrade+1) + "", True, Black)
        radius_text=self.font_text.render("Радиус  " + str(tower.radius) + "", True, Black)
        fire_rate_text=self.font_text.render("Скорострельность  " + str(round(tower.fire_rate/60,3)) + "", True, Black)
        punching_text=self.font_text.render("Пробивание брони  " + str(round(tower.punching*100,2)) + "%", True, Black)
        damage_shield_text=self.font_text.render("Урон по щитам  " + str(round(tower.damage_shield*100,2)) + "%", True, Black)
        self.area.blit(image,image.get_rect(center=self.image_pos))
        self.area.blit(name_text,name_text.get_rect(center=self.name_pos))
        self.area.blit(level_text, (self.text_x,self.first_text_y))
        self.area.blit(damage_text,(self.text_x,self.first_text_y+self.difference_text_y))
        self.area.blit(radius_text, (self.text_x,self.first_text_y+2*self.difference_text_y))
        self.area.blit(fire_rate_text, (self.text_x,self.first_text_y+3*self.difference_text_y))
        self.area.blit(punching_text, (self.text_x,self.first_text_y+4*self.difference_text_y))
        self.area.blit(damage_shield_text, (self.text_x, self.first_text_y + 5 * self.difference_text_y))
        if hasattr(tower, 'count_fraction'):
            fraction_text=self.font_text.render("Дробин  "+str(tower.count_fraction),True,Black)
            self.area.blit(fraction_text, (self.text_x, self.first_text_y + 6 * self.difference_text_y))
            destruction_text=self.font_text.render("Разр. брони (1 дробь) "+str(tower.destruction_armor*100),True,Black)
            self.area.blit(destruction_text, (self.text_x, self.first_text_y + 7 * self.difference_text_y))
        elif hasattr(tower, 'kindling_speed'):
            kindling_speed_text = self.font_text.render("Скорость разжигания  " + str(tower.kindling_speed*10), True, Black)
            self.area.blit(kindling_speed_text , (self.text_x, self.first_text_y + 6 * self.difference_text_y))

    def draw(self):
        self.surface.blit(self.circle,self.center)
        self.surface.blit(self.area, (self.x, self.y))
        if self.alg_button_pressed:
            for alg_button in self.alg_buttons:
                alg_button.draw()
        self.alg_button.draw()

    def pos_click_area(self,mouse):
        return mouse[0]-self.x,mouse[1]-self.y

    def collide(self,x1,y1):
        if self.x<x1<self.x+self.width:
            if self.y<y1<self.y+self.height:
                return True
        else:
            return False

    def collide_upgrade_button(self,mouse):
        pos=self.pos_click_area(mouse)
        if self.tower.number_upgrade+1==3 and not self.tower.path:
            if self.choice_button[0].collide(pos[0],pos[1]):
                self.tower.path=1
                self.__init__(self.surface, self.tower)
            elif self.choice_button[1].collide(pos[0],pos[1]):
                self.tower.path = 2
                self.__init__(self.surface,self.tower)
        elif self.upg_button:
            if self.upg_button.collide(pos[0],pos[1]):
                return True

    def collide_sell_button(self, mouse):
        pos = self.pos_click_area(mouse)
        if self.sell_button.collide(pos[0], pos[1]):
            return True

    def collide_alg_buttons(self,mouse):
        for i in range(len(self.alg_buttons)):
            if self.alg_buttons[i].collide(mouse[0],mouse[1]):
                self.alg_buttons_pressed.image=SelectedTower.alg_buttons_img
                self.tower.find_target=self.alg_buttons[i].algoritm
                self.alg_buttons_pressed=self.alg_buttons[i]
                self.alg_buttons[i].image=SelectedTower.alg_buttons1_img
                return True

    def collide_alg_button(self,mouse):
        pos=self.pos_click_area(mouse)
        if self.alg_button.collide(pos[0],pos[1]):
            if not self.alg_button_pressed:
                self.alg_button_pressed=True
                self.alg_button.image=SelectedTower.alg_button1_img
            else:
                self.alg_button_pressed = False
                self.alg_button.image = SelectedTower.alg_button_img
            return True
        elif self.alg_button_pressed:
            return self.collide_alg_buttons(mouse)

    @staticmethod
    def scaling_attributes(w,h):
        width=round((w/19.2)*4,1)
        height=round((h/7.71)*4,1)
        SelectedTower.area=pg.transform.scale(area,(width,height))
        SelectedTower.image_pos=(round(width*0.24,1),round(height/5.6,1))
        SelectedTower.name_pos=(round(width*0.73,1),round(height/17.5,1))
        SelectedTower.text_x=round(width/2,1)
        SelectedTower.first_text_y=round(height/7,1)
        SelectedTower.difference_text_y=round(height/15,1)
        SelectedTower.font_button = pg.font.Font('font1/font.ttf', round(height / 19))
        SelectedTower.font_name = pg.font.Font('font1/font.ttf', round(height / 13))
        SelectedTower.font_text = pg.font.Font('font1/font.ttf', round(height / 35))
        SelectedTower.upg_button_img=pg.transform.scale(upgrade_button,(round(width/1.2),round(height/12,1)))
        SelectedTower.choice_button_img = pg.transform.scale(upgrade_button, (round(width / 2.5), round(height / 11, 1)))
        height_alg_button=round(width/6,1)
        SelectedTower.alg_button_img=pg.transform.scale(algoritm_button,(width,height_alg_button))
        SelectedTower.alg_button1_img = pg.transform.scale(algoritm_button1, (width, height_alg_button))
        SelectedTower.alg_buttons_img = pg.transform.scale(algoritm_buttons, (width, height_alg_button))
        SelectedTower.alg_buttons1_img = pg.transform.scale(algoritm_buttons1, (width, height_alg_button))
        y_pos = round(height * 0.75, 1)
        SelectedTower.upgrade_button_pos = (round(width/2,1),y_pos+round(height/7,1))
        SelectedTower.sell_button_pos = (round(width/2,1),y_pos)
        SelectedTower.first_alg_button_y=height+round(SelectedTower.alg_button_img.get_height()/2,1)
        indent=round(width/4,1)
        SelectedTower.choice1_button_pos=(indent,y_pos+round(height/7,1))
        SelectedTower.choice2_button_pos =(width-indent,y_pos+round(height/7,1))
