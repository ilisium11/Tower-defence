import pygame as pg
from button import Button1
panel=pg.image.load("images/panel.png").convert()
tower1_button=pg.image.load("images/tower1_button.png").convert()
tower2_button=pg.image.load("images/tower2_button - .png").convert()
tower3_button=pg.image.load("images/tower3_button.png").convert()
YELLOW=(255,255,0)


class MenuTowers:
    menu=None
    button_tower1_pos=None
    button_tower2_pos=None
    button_tower3_pos = None
    button_tower1=None
    button_tower2=None
    button_tower3 = None

    def __init__(self,turret,shotgun,laser):
        self.menu=MenuTowers.menu.copy()
        img_tower1_level1=turret.image_list[0]
        img_tower2_level1=shotgun.image_list[0]
        img_tower3_level1 = laser.image_list[0]
        cost_tower1=str(turret.cost_list[0])
        cost_tower2 = str(shotgun.cost_list[0])
        cost_tower3 = str(laser.cost_list[0])
        self.button_tower1=MenuTowers.BuyButton(MenuTowers.button_tower1_pos,MenuTowers.button_tower1,img_tower1_level1,self.menu,cost_tower1,turret)
        self.button_tower2 = MenuTowers.BuyButton(MenuTowers.button_tower2_pos, MenuTowers.button_tower2, img_tower2_level1,self.menu, cost_tower2, shotgun)
        self.button_tower3 = MenuTowers.BuyButton(MenuTowers.button_tower3_pos, MenuTowers.button_tower3,img_tower3_level1, self.menu, cost_tower3, laser)

    def click_buttons(self,mouse_pos):
        if self.button_tower1.collide(mouse_pos[0],mouse_pos[1]):
            return self.button_tower1
        elif self.button_tower2.collide(mouse_pos[0],mouse_pos[1]):
            return self.button_tower2
        elif self.button_tower3.collide(mouse_pos[0],mouse_pos[1]):
            return self.button_tower3

    def draw(self,surface):
        surface.blit(self.menu,(0,0))

    class BuyButton(Button1):
        font = None
        text_cost_pos_x=None

        def __init__(self, pos, icon_tower, image_tower, surface, cost_tower, tower):
            image = icon_tower
            super().__init__(pos, image, surface)
            self.image_tower = image_tower
            self.cost_tower = cost_tower
            self.tower = tower
            self.text = MenuTowers.BuyButton.font.render(self.cost_tower, True, YELLOW)
            center = self.image.get_rect(center=pos)
            center_text = self.text.get_rect(center=(MenuTowers.BuyButton.text_cost_pos_x, pos[1]))
            self.surface.blit(self.text, center_text)
            self.surface.blit(self.image, center)

    @staticmethod
    def scaling_attributes(width,height):
        menu_width=round(width/8,1)
        menu_height=round(height/2.5,1)
        MenuTowers.menu = pg.transform.scale(panel, (menu_width, menu_height))
        buy_button_pos_x=round(menu_width/3,1)
        MenuTowers.button_tower1_pos=(buy_button_pos_x,round(menu_height/6,2))
        MenuTowers.button_tower2_pos=(buy_button_pos_x,round(menu_height/2,2))
        MenuTowers.button_tower3_pos = (buy_button_pos_x, round(menu_height * 5 / 6, 1))
        MenuTowers.button_tower1=pg.transform.scale(tower1_button,(round(menu_width/2,2),round(menu_height/5,2)))
        MenuTowers.button_tower2=pg.transform.scale(tower2_button,(round(menu_width/2,2),round(menu_height/5,2)))
        MenuTowers.button_tower3 = pg.transform.scale(tower3_button,(round(menu_width / 2, 2), round(menu_height / 5, 2)))
        MenuTowers.BuyButton.font = pg.font.SysFont('arial', round(height/30))
        MenuTowers.BuyButton.text_cost_pos_x = round(menu_width/2+buy_button_pos_x/2+MenuTowers.button_tower1.get_width()/4)
