import pygame as pg
import sys
from wave_stats import Levels
from button import LevelButton,TextButton
from game import Game
YELLOW=(255,255,0)
Green=(124,252,0)
Black=(0,0,0)
level_choice=pg.image.load("images/selection_level.png").convert()


class LevelSelection:

    def __init__(self,surface,button_image,font):
        self.surface=surface
        width=surface.get_width()
        height=surface.get_height()
        width_button=round(width / 6, 1)
        self.width_cell=(round((width/16)*0.5,1))
        self.font=font
        self.menu_button_image = pg.transform.scale(button_image, (width_button, round(width_button/6,1)))
        self.window_road1=Levels.level1(width,height)
        self.window_road1_selection_level=pg.transform.scale(self.window_road1,(round(width/2,1),round(height/2,1)))
        self.center_window_road1=self.window_road1_selection_level.get_rect(center=(round(width/2,2),round(height/2,1)))
        self.level_choice = pg.transform.scale(level_choice,(width,height))
        self.button1_selection_pos = (round(width/2,1),round(height/1.2,2))
        self.back_button_settings_pos = (round(width / 9, 2), round(height / 1.1, 2))
        self.game=None
        self.return_menu=None
        self.restart=None

    def new_game(self,level):
        self.game=Game(self.surface,level,self.window_road1,self.width_cell)
        self.restart,self.return_menu=self.game.game()

    def selection_level(self):
        run=True
        buttons=[]
        button_cansel=(TextButton(self.back_button_settings_pos, self.menu_button_image, self.level_choice,self.font, 'Назад'))
        buttons.append(LevelButton(self.button1_selection_pos,self.menu_button_image,self.level_choice,"Уровень 1",self.font,Levels.level1))
        self.level_choice.blit(self.window_road1_selection_level, self.center_window_road1)
        for button in buttons:
            button.draw()
        button_cansel.draw()
        self.surface.blit(self.level_choice,(0,0))
        while run:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    for i in buttons:
                        if i.collide(mouse[0],mouse[1]):
                            pg.mixer.music.load('music/game_music.mp3')
                            pg.mixer.music.play(-1)
                            self.new_game(i.level)
                            while self.restart:
                                self.new_game(i.level)
                            if self.return_menu:
                                return True
                            else:
                                self.surface.blit(self.level_choice, (0, 0))
                        elif button_cansel.collide(mouse[0],mouse[1]):
                            run=False
            pg.display.update()
