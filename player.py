import pygame as pg
player_area=pg.image.load('images/player_stats.png').convert()
health_img=pg.image.load('images/health.png').convert()
money_img=pg.image.load('images/money.png').convert()
health_img.set_colorkey((255,255,255))
money_img.set_colorkey((255,255,255))
Black=(0,0,0)
Red=(255,0,0)
Color_rect=(210,220,220)


class Player:
    font=None
    area=None
    area_pos=None
    health=None
    money=None
    health_text_pos=None
    money_text_pos=None
    wave_text_pos=None
    health_rect=None
    money_rect = None
    wave_rect=None
    health_img_pos=None
    money_img_pos=None

    def __init__(self,surface,health,money,wave,waves):
        self.surface=surface
        self.health=health
        self.max_health=health
        self.money=money
        self.waves=waves
        self.wave=wave
        self.old_health=health
        self.old_money=money
        self.old_wave=wave
        self.area=Player.area
        self.area_center=self.area.get_rect(center=Player.area_pos)
        self.area.blit(Player.health,Player.health.get_rect(center=Player.health_img_pos))
        self.area.blit(Player.money, Player.money.get_rect(center=Player.money_img_pos))
        self.health_rect_center=self.health_rect.get_rect(center=Player.health_text_pos)
        self.money_rect_center = self.money_rect.get_rect(center=Player.money_text_pos)
        self.wave_rect_center=self.wave_rect.get_rect(center=Player.wave_text_pos)
        self.render_health()
        self.render_money()
        self.render_wave()

    def render_health(self):
        text_health = self.font.render(str(self.old_health), Black, True)
        self.area.blit(self.health_rect, self.health_rect_center)
        self.area.blit(text_health, text_health.get_rect(center=self.health_text_pos))

    def render_money(self):
        text_money = self.font.render(str(round(self.old_money)), Black, True)
        self.area.blit(self.money_rect, self.money_rect_center)
        self.area.blit(text_money, text_money.get_rect(center=self.money_text_pos))

    def render_wave(self):
        text_wave = self.font.render('Волна ' + str(self.old_wave), Black, True)
        self.area.blit(self.wave_rect, self.wave_rect_center)
        self.area.blit(text_wave, text_wave.get_rect(center=self.wave_text_pos))

    def render_countdown_wave(self,time,time_to_wave):
        text=self.font.render('Время до волны '+str((time_to_wave-time)//60),True,Black)
        self.area.blit(self.wave_rect, self.wave_rect_center)
        self.area.blit(text,text.get_rect(center=self.wave_text_pos))

    def draw(self):
        if not self.old_health==self.health:
            self.old_health = self.health
            self.render_health()
        if not self.old_money==self.money:
            self.old_money=self.money
            self.render_money()
        if not self.old_wave==self.wave:
            self.old_wave=self.wave
            self.render_wave()
        self.surface.blit(self.area,self.area_center)

    @staticmethod
    def scaling_attributes(w,h):
        width=round(w/2.1,1)
        height=round(h/20,1)
        Player.area_pos = (round(w / 2, 1), round(height/2,1))
        Player.area=pg.transform.scale(player_area,(width,height))
        Player.health=pg.transform.scale(health_img,(round(width/18,1),round(height/1.25,1)))
        Player.money=pg.transform.scale(money_img,(round(width/12),round(height/1.35)))
        font_size=round(height/1.4)
        Player.font=pg.font.Font('font1/font.ttf',font_size)
        Player.health_img_pos=(round(width/14,1),round(height/2,1))
        Player.money_img_pos = (round(width / 1.09,1), round(height / 2,1))
        Player.health_text_pos = (round(width / 12,1)+1.5*Player.health.get_width(), round(height / 2,1))
        Player.money_text_pos = (round(width / 1.1, 1) - 1.5*Player.money.get_width(), round(height / 2, 1))
        Player.wave_text_pos = (round(width / 2.2, 1), round(height / 2, 1))
        Player.health_rect=pg.Surface((round(font_size*2,1),round(height/1.2,1)))
        Player.money_rect = pg.Surface((round(font_size * 4,1),round( height / 1.2,1)))
        Player.wave_rect=pg.Surface((round(font_size*10,1),round(height/1.2,1)))
        Player.health_rect.fill(Color_rect)
        Player.money_rect.fill(Color_rect)
        Player.wave_rect.fill(Color_rect)
