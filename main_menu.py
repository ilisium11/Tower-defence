import pygame as pg
import sys
from button import TextButton
from game import Game
from wave_stats import Levels
from settings_game import Settings
from level_selection import LevelSelection
YELLOW=(255,255,0)
Clock=pg.time.Clock()
Green=(124,252,0)
Black=(0,0,0)
menu=pg.image.load("images/menu.png").convert()
button_image=pg.image.load("images/end_game_button.png").convert()
button_image.set_colorkey((255,255,255))


class Menu:

    def __init__(self,size):
        width=size[0]
        height=size[1]
        width_cell=(round((width/16)*0.5,1))
        Game.scaling_attributes(width_cell,width, height)
        Levels.scaling_attributes(width_cell)
        self.surface = pg.display.set_mode(size,pg.FULLSCREEN)
        pg.display.set_caption("Tower defence")
        self.font = pg.font.SysFont('arial', round(height/22))
        self.menu = pg.transform.scale(menu,(width,height))
        width_button=round(width/5.4,1)
        height_button=round(width_button/6,1)
        self.menu_button_image = pg.transform.scale(button_image,(width_button,height_button))
        self.settings = Settings(self.surface,self.menu_button_image,self.font)
        self.selection_level=LevelSelection(self.surface,self.menu_button_image,self.font)
        y_pos=round(height/1.4,1)
        self.button1_menu_pos = (round(width/2,1),y_pos)
        self.button2_menu_pos = (round(width/2,1),y_pos+height_button*1.3)
        self.button3_menu_pos = (round(width / 2, 1), y_pos+height_button*2.6)
        self.main_menu()

    def main_menu(self):
        run=True
        menu_buttons = []
        menu_buttons.append(TextButton(self.button1_menu_pos,self.menu_button_image,self.menu,self.font,"Начать игру"))
        menu_buttons.append(TextButton(self.button2_menu_pos,self.menu_button_image,self.menu,self.font,"Настройки"))
        menu_buttons.append(TextButton(self.button3_menu_pos, self.menu_button_image, self.menu, self.font, "Выйти"))
        for button in menu_buttons:
            button.draw()
        self.surface.blit(self.menu, (0, 0))
        pg.mixer.music.load('music/main_menu_music.mp3')
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        while run:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    if menu_buttons[0].collide(mouse[0],mouse[1]):
                        self.selection_level.selection_level()
                        self.surface.blit(self.menu, (0, 0))
                        pg.mixer.music.load('music/main_menu_music.mp3')
                        pg.mixer.music.play(-1)
                    elif menu_buttons[1].collide(mouse[0],mouse[1]):
                        returns=self.settings.settings()
                        if returns:
                            self.__init__(returns)
                            run=False
                        self.surface.blit(self.menu, (0, 0))
                    elif menu_buttons[2].collide(mouse[0],mouse[1]):
                        sys.exit()
            pg.display.update()
            Clock.tick(60)
