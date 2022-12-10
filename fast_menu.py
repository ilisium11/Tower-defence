import pygame as pg
from button import Button1
area=pg.image.load('images/fast_menu_game.png').convert()
menu_button=pg.image.load('images/menu_button.png').convert()
restart_button=pg.image.load('images/restart_button.png').convert()
continue_button=pg.image.load('images/continue_button.png').convert()
calling_menu_button=pg.image.load('images/settings_button.png').convert()
calling_menu_button1=pg.image.load('images/settings_button1.png').convert()
pause_button=pg.image.load('images/pause_button.png').convert()
pause_button1=pg.image.load('images/pause_button1.png').convert()
area.set_colorkey((255,255,255))
menu_button.set_colorkey((255,255,255))
restart_button.set_colorkey((255,255,255))
continue_button.set_colorkey((255,255,255))
calling_menu_button.set_colorkey((255,255,255))
calling_menu_button1.set_colorkey((255,255,255))
pause_button.set_colorkey((255,255,255))
pause_button1.set_colorkey((255,255,255))


class GameMenuButton(Button1):
    def __init__(self,pos,image,image_when_clicked,surface):
        super().__init__(pos,image,surface)
        self.image_when_not_clicked=image
        self.image_when_clicked=image_when_clicked

    def collide(self,x,y):
        ret=super().collide(x,y)
        if ret:
            if self.image==self.image_when_clicked:
                self.image = self.image_when_not_clicked
            else:
                self.image = self.image_when_clicked
            return ret


class MenuGame:
    area=None
    area_center=None
    menu_button=None
    restart_button=None
    continue_button=None
    menu_button_pos=None
    restart_button_pos=None
    continue_button_pos=None
    calling_menu_button=None
    calling_menu_button1 = None
    pause_button = None
    pause_button1 = None
    calling_menu_button_pos=None
    pause_button_pos=None

    def __init__(self,surface):
        self.surface=surface
        self.calling_menu_button=GameMenuButton(self.calling_menu_button_pos,self.calling_menu_button,self.calling_menu_button1,surface)
        self.pause_button=GameMenuButton(self.pause_button_pos,self.pause_button,self.pause_button1,surface)
        self.area=MenuGame.area.copy()
        self.area_center=self.area.get_rect(center=self.area_center)
        self.menu_button=Button1(self.menu_button_pos,self.menu_button,self.area)
        self.restart_button = Button1(self.restart_button_pos, self.restart_button, self.area)
        self.continue_button = Button1(self.continue_button_pos, self.continue_button, self.area)
        self.menu_button.draw()
        self.restart_button.draw()
        self.continue_button.draw()

    def pos_click_menu(self,mouse):
        return mouse[0]-self.area_center.x,mouse[1]-self.area_center.y

    def collide_pause_button(self,mouse):
        if self.pause_button.collide(mouse[0],mouse[1]):
            return True

    def collide_calling_button(self,mouse):
        if self.calling_menu_button.collide(mouse[0],mouse[1]):
            return True

    def collide_menu_button(self,mouse):
        pos=self.pos_click_menu(mouse)
        if self.menu_button.collide(pos[0],pos[1]):
            return True

    def collide_restart_button(self,mouse):
        pos = self.pos_click_menu(mouse)
        if self.restart_button.collide(pos[0],pos[1]):
            return True

    def collide_continue_button(self,mouse):
        pos = self.pos_click_menu(mouse)
        if self.continue_button.collide(pos[0],pos[1]):
            return True

    def draw_game_buttons(self):
        self.calling_menu_button.draw()
        self.pause_button.draw()

    def draw_menu(self):
        self.surface.blit(self.area,self.area_center)

    @staticmethod
    def scaling_attributes(width,height):
        width_menu=round(width/3,1)
        height_menu=round(height/2.5,1)
        MenuGame.area=pg.transform.scale(area,(width_menu,height_menu))
        MenuGame.area_center=(round(width/2,1),round(height/2,1))
        width_button=round(width_menu/5,1)
        height_button=round(width_button/1.2,1)
        MenuGame.menu_button=pg.transform.scale(menu_button,(width_button,height_button))
        MenuGame.restart_button=pg.transform.scale(restart_button,(width_button,height_button))
        MenuGame.continue_button=pg.transform.scale(continue_button,(width_button,height_button))
        y_pos_button=round(height_menu/1.3,1)
        MenuGame.menu_button_pos=(round(width_menu/6),y_pos_button)
        MenuGame.restart_button_pos = (round(width_menu/ 2), y_pos_button)
        MenuGame.continue_button_pos = (round(width_menu*5 / 6), y_pos_button)
        width_calling_menu_button=round(width/20,1)
        MenuGame.calling_menu_button=pg.transform.scale(calling_menu_button,(width_calling_menu_button,width_calling_menu_button))
        MenuGame.calling_menu_button1 = pg.transform.scale(calling_menu_button1,(width_calling_menu_button, width_calling_menu_button))
        calling_menu_button_pos_x=round(width-width_calling_menu_button/2,1)
        MenuGame.calling_menu_button_pos=(calling_menu_button_pos_x,round(width_calling_menu_button/2,1))
        MenuGame.pause_button=pg.transform.scale(pause_button,(width_calling_menu_button,width_calling_menu_button))
        MenuGame.pause_button1 = pg.transform.scale(pause_button1, (width_calling_menu_button, width_calling_menu_button))
        MenuGame.pause_button_pos=(calling_menu_button_pos_x-width_calling_menu_button,round(width_calling_menu_button/2,1))
