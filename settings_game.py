import pygame as pg
import sys
from button import TextButton,Button1,MovingButton
YELLOW=(255,255,0)
Green=(124,252,0)
Red=(255,0,0)
Blue=(0,0,210)
settings_color=(52,75,55)

window_settings=pg.image.load("images/window_settings.png").convert()
switch_left=pg.image.load('images/switch_left.png').convert()
switch_left.set_colorkey((255,255,255))
switch_right=pg.image.load('images/switch_right.png').convert()
switch_right.set_colorkey((255,255,255))
music_button=pg.image.load('images/music_button.png').convert()


class ChangeSound:

    def __init__(self,width,height,pos,surface):
        self.music_button_img=pg.transform.scale(music_button,(round(width/120,1),round(height/30,1)))
        self.length_line=round(width/3,1)
        self.half_length_line=round(self.length_line/2,1)
        self.thickness=round(self.length_line/40)
        self.surface=surface
        self.moving_button = MovingButton(pos, self.music_button_img,surface)
        self.pos_line=pos
        self.line_bottom_left_x=pos[0]-self.half_length_line
        self.rect = pg.Rect(pos[0]-self.half_length_line*1.1,pos[1]-self.thickness*1.2,self.length_line*1.1,self.thickness*2.4)
        pg.draw.rect(self.surface,settings_color,self.rect)
        self.line_rect=pg.draw.line(self.surface, Blue, (self.line_bottom_left_x, self.pos_line[1]),(self.line_bottom_left_x + self.length_line, self.pos_line[1]), self.thickness)
        self.moving_button.draw()

    def collide(self,mouse):
        if self.moving_button.collide(mouse[0],mouse[1]):
            return True

    def moving(self,mouse):
        if self.moving_button.moving:
            if self.line_rect.x<mouse[0]<self.line_rect.x+self.line_rect.width:
                self.moving_button.set_pos_x(mouse[0])
                music_volume=(mouse[0]-self.line_bottom_left_x)/self.length_line
                pg.mixer.music.set_volume(music_volume)
                return True

    def draw(self):
        pg.draw.rect(self.surface,settings_color,self.rect)
        pg.draw.line(self.surface, Blue, (self.pos_line[0] - self.half_length_line, self.pos_line[1]),(self.pos_line[0] + self.half_length_line, self.pos_line[1]), self.thickness)
        self.moving_button.draw()


class Resolution:

    def __init__(self,width,height,font,surface):
        self.surface=surface
        self.resolution = [(1280, 720), (1600, 900), (1920, 1080)]
        self.count_resolution=len(self.resolution)
        self.selected_resolution=self.resolution.index((width,height))
        self.native_resolution=self.selected_resolution
        self.font=font
        self.resolution_text=font.render('Разрешение',True,Green)
        pos_y_resolution=round(height/6,1)
        self.resolution_text_pos=self.resolution_text.get_rect(center=(round(width/7,2),pos_y_resolution))
        self.res_choice_text=font.render(str(width)+'x'+str(height),True,YELLOW)
        pos_x_resolution=round(width/1.8,1)
        self.res_choice_text_pos = self.res_choice_text.get_rect(center=(pos_x_resolution,pos_y_resolution))
        switch_button_w, switch_button_h = round(width / 12.5, 2), round(height / 12.5, 2)
        switch_left_img=pg.transform.scale(switch_left,(switch_button_w,switch_button_h))
        switch_right_img=pg.transform.scale(switch_right,(switch_button_w,switch_button_h))
        pos_x_switch_left, pos_x_switch_right = pos_x_resolution - round(width / 5, 2), pos_x_resolution + round(width / 5, 2)
        switch_left_pos=(pos_x_switch_left,pos_y_resolution)
        switch_right_pos=(pos_x_switch_right,pos_y_resolution)
        self.switch_left=Button1(switch_left_pos,switch_left_img,surface)
        self.switch_right = Button1(switch_right_pos, switch_right_img, surface)
        self.rect = pg.Rect(pos_x_switch_left + round(switch_button_w / 2, 2),pos_y_resolution - round(switch_button_h / 2, 2),pos_x_switch_right - pos_x_switch_left - switch_button_w, switch_button_h)

    def collide(self,mouse):
        if self.switch_left.collide(mouse[0], mouse[1]):
            self.selected_resolution -= 1
            self.setup_resolution_text()
            return True
        elif self.switch_right.collide(mouse[0], mouse[1]):
            self.selected_resolution += 1
            self.setup_resolution_text()
            return True

    def is_the_resolution_new(self):
        if self.native_resolution != self.selected_resolution:
            size = self.resolution[self.selected_resolution]
            return size

    def setup_old_resolution(self):
        if self.native_resolution!=self.selected_resolution:
            self.selected_resolution=self.native_resolution
            self.setup_resolution_text()

    def setup_resolution_text(self):
        if self.selected_resolution == self.count_resolution:
            self.selected_resolution = 0
        elif self.selected_resolution == -1:
            self.selected_resolution = self.count_resolution-1
        self.res_choice_text = self.font.render(str(self.resolution[self.selected_resolution][0]) + 'x' + str(self.resolution[self.selected_resolution][1]),True, YELLOW)
        self.res_choice_text_pos = self.res_choice_text.get_rect(center=(self.res_choice_text_pos.centerx,self.res_choice_text_pos.centery))
        pg.draw.rect(self.surface, settings_color, self.rect)
        self.surface.blit(self.res_choice_text, self.res_choice_text_pos)
        self.surface.blit(self.surface, (0, 0))

    def draw(self):
        self.surface.blit(self.resolution_text, self.resolution_text_pos)
        self.switch_left.draw()
        self.switch_right.draw()
        self.surface.blit(self.res_choice_text, self.res_choice_text_pos)


class Settings:
    def __init__(self,surface,button_image,font):
        width=surface.get_width()
        height=surface.get_height()
        self.clock=pg.time.Clock()
        self.window_settings = pg.transform.scale(window_settings, (width, height))
        self.font=font
        width_button=round(width / 6, 1)
        self.menu_button_image = pg.transform.scale(button_image, (width_button, round(width_button/6,1)))
        self.surface=surface
        self.back_button_settings_pos=(round(width/9,2),round(height/1.15,2))
        self.accept_button_settings_pos=(round(width/1.15,2),round(height/1.15,2))
        self.font_settings=pg.font.SysFont('arial',round(height/15))
        self.music_settings=ChangeSound(width,height,(round(width/4,1),round(height/2,1)),self.window_settings)
        self.resolution=Resolution(width,height, self.font_settings,self.window_settings)
        self.text_music=self.font_settings.render('Изменение громкости музыки',True,Green)
        self.text_music_pos=self.text_music.get_rect(center=(round(width/3.7,1),round(height/2.4,1)))
        self.button_cansel=(TextButton(self.back_button_settings_pos,self.menu_button_image,self.window_settings,self.font,"Назад"))
        self.button_accept=(TextButton(self.accept_button_settings_pos,self.menu_button_image,self.window_settings,self.font,'Принять'))
        self.draw()

    def draw(self):
        self.resolution.draw()
        self.button_cansel.draw()
        self.button_accept.draw()
        self.window_settings.blit(self.text_music,self.text_music_pos)

    def settings(self):
        run=True
        self.surface.blit(self.window_settings, (0, 0))
        while run:
            key = pg.mouse.get_pressed()
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if self.button_cansel.collide(mouse[0],mouse[1]):
                        run=False
                        self.resolution.setup_old_resolution()
                    elif self.button_accept.collide(mouse[0],mouse[1]):
                        return self.resolution.is_the_resolution_new()
                    elif self.resolution.collide(mouse):
                        self.surface.blit(self.window_settings, (0, 0))
                    self.music_settings.collide(mouse)
                elif event.type==pg.MOUSEMOTION:
                    if key[0]:
                        if self.music_settings.moving(mouse):
                            self.music_settings.draw()
                            self.surface.blit(self.window_settings, (0, 0))
            pg.display.update()
