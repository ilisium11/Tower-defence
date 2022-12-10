import pygame as pg
from button import TextButton
area=pg.image.load('images/end_game_area.png').convert()
star=pg.image.load('images/star.png').convert()
star_white=pg.image.load('images/star_white.png').convert()
continue_button=pg.image.load('images/end_game_button.png').convert()
restart_button=pg.image.load('images/end_game_button.png').convert()
area.set_colorkey((255,255,255))
star.set_colorkey((255,255,255))
star_white.set_colorkey((255,255,255))
continue_button.set_colorkey((255,255,255))
Green=(10,220,10)
Red=(210,0,0)


class EndGame:
    area=None
    area_center=None
    font=None
    star=None
    star_white=None
    continue_button=None
    restart_button=None
    text_pos=None
    first_star_pos_x=None
    difference_star_pos_x=None
    star_pos_y=None
    continue_button_pos=None
    restart_button_pos=None
    restart_button_button_pos=None

    def __init__(self,surface):
        self.surface=surface
        self.area=EndGame.area.copy()
        self.area_center=self.area.get_rect(center=self.area_center)
        self.continue_button = TextButton(self.continue_button_pos, self.continue_button, self.area,self.font,'Продолжить')
        self.restart_button = TextButton(self.restart_button_pos, self.restart_button, self.area,self.font,'Заново')
        self.continue_button.draw()
        self.restart_button.draw()

    def pos_click_menu(self,mouse):
        return mouse[0]-self.area_center.x,mouse[1]-self.area_center.y

    def collide_continue_button(self,mouse):
        pos = self.pos_click_menu(mouse)
        if self.continue_button.collide(pos[0],pos[1]):
            return True

    def collide_restart_button(self,mouse):
        pos = self.pos_click_menu(mouse)
        if self.restart_button.collide(pos[0],pos[1]):
            return True

    def draw_end_game(self,stars):
        if stars>0:
            text=self.font.render('Победа',True,Green)
        else:
            text = self.font.render('Поражение', True, Red)
        self.area.blit(text,text.get_rect(center=self.text_pos))
        for i in range(stars):
            self.area.blit(self.star,self.star.get_rect(center=(self.first_star_pos_x+i*self.difference_star_pos_x,self.star_pos_y)))
        for i in range(stars,3):
            self.area.blit(self.star_white, self.star.get_rect(center=(self.first_star_pos_x + i * self.difference_star_pos_x, self.star_pos_y)))
        self.surface.blit(self.area,self.area_center)

    @staticmethod
    def scaling_attributes(width,height):
        width_area=round(width/3,1)
        height_area=round(height/2.5,1)
        EndGame.area=pg.transform.scale(area,(width_area,height_area))
        EndGame.area_center=(round(width/2,1),round(height/2,1))
        EndGame.font=pg.font.Font('font1/font.ttf',round(height_area/9))
        width_button=round(width_area/2.3,1)
        height_button=round(width_button/6,1)
        EndGame.continue_button=pg.transform.scale(continue_button,(width_button,height_button))
        EndGame.restart_button = pg.transform.scale(restart_button, (width_button, height_button))
        width_star=round(width_area/7,1)
        height_star=round(width_star/1.2,1)
        EndGame.star=pg.transform.scale(star,(width_star,height_star))
        EndGame.star_white = pg.transform.scale(star_white, (width_star, height_star))
        EndGame.text_pos=(round(width_area/2,1),round(height_area/9,1))
        medium_star_pos_x=round(width_area/2,1)
        EndGame.difference_star_pos_x=round(width_star*1.5,1)
        EndGame.first_star_pos_x=medium_star_pos_x-EndGame.difference_star_pos_x
        EndGame.star_pos_y=round(height_area/2.3)
        EndGame.continue_button_pos=(round(width_area/2,1),round(height_area/1.5,1))
        EndGame.restart_button_pos = (round(width_area / 2, 1), round(height_area / 1.2, 1))
