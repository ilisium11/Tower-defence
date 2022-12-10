import pygame as pg
from button import Button1
window_selection=pg.image.load('images/selected_obj_terrain.png').convert()
accept_button=pg.image.load('images/accept_button.png').convert()
accept_button.set_colorkey((255,255,255))
cansel_button=pg.image.load('images/cansel_button.png').convert()
cansel_button.set_colorkey((255,255,255))
Green=(85, 107, 47)


class WindowObjTerrain:
    window_selection=None
    window_pos=None
    image_pos_center=None
    text_pos=None
    accept_button_pos_center=None
    cansel_button_pos_center=None
    accept_button=None
    cansel_button=None
    font=None

    def __init__(self,obj):
        self.obj=obj
        self.pos_cell=obj.pos_cell
        self.image=obj.image
        self.cost=obj.cost
        self.window_selection = WindowObjTerrain.window_selection.copy()
        self.window_center=self.window_selection.get_rect(center=self.window_pos)
        self.width_window=self.window_selection.get_width()
        self.height_window=self.window_selection.get_height()
        self.rect = pg.Rect(self.window_center.x,self.window_center.y,self.width_window,self.height_window)
        self.window_selection.blit(self.image, self.image.get_rect(center=self.image_pos_center))
        text = self.font.render('Уничтожить за ' + str(self.cost) + ' ?', True, Green)
        self.window_selection.blit(text,self.text_pos)
        self.accept_button = Button1(self.accept_button_pos_center, self.accept_button, self.window_selection)
        self.cansel_button = Button1(self.cansel_button_pos_center, self.cansel_button, self.window_selection)
        self.accept_button.draw()
        self.cansel_button.draw()

    def draw(self,surface):
        surface.blit(self.window_selection,self.window_center)

    def collide(self,mouse):
        if self.rect.collidepoint(mouse[0],mouse[1]):
            return True

    def pos_click(self,mouse):
        return mouse[0]-self.window_center.x,mouse[1]-self.window_center.y

    def collide_accept_button(self,mouse):
        pos=self.pos_click(mouse)
        if self.accept_button.collide(pos[0],pos[1]):
            return True

    def collide_cansel_button(self,mouse):
        pos = self.pos_click(mouse)
        if self.cansel_button.collide(pos[0],pos[1]):
            return True

    @staticmethod
    def scaling_attributes(width,height,width_cell):
        width_window=round(width/2.9,1)
        height_window=round(height/13,1)
        WindowObjTerrain.window_selection=pg.transform.scale(window_selection,(width_window,height_window))
        WindowObjTerrain.window_pos=(round(width/2,1),round(height-height_window/2,1))
        font_size=round(height_window / 2)
        WindowObjTerrain.font = pg.font.SysFont('arial', font_size)
        x_pos_image=round(width_window/7,1)

        WindowObjTerrain.image_pos_center=(x_pos_image,round(height_window/2,1))
        WindowObjTerrain.text_pos=(x_pos_image+width_cell,round(height_window/2-font_size/2,1))

        x_center_pos_button2=round(width_window/1.1,1)
        WindowObjTerrain.accept_button_pos_center = (x_center_pos_button2,round(height_window/2,1))
        WindowObjTerrain.cansel_button_pos_center=(x_center_pos_button2-width_cell*1.2,round(height_window/2,1))
        WindowObjTerrain.accept_button=pg.transform.scale(accept_button,(width_cell,width_cell))
        WindowObjTerrain.cansel_button = pg.transform.scale(cansel_button, (width_cell, width_cell))


class ObjTerrain:

    def __init__(self,img,name,cost,pos,pos_cell):
        self.image=img
        self.width=img.get_width()
        self.name=name
        self.cost=cost
        self.pos_cell=pos_cell
        self.rect=pg.Rect(pos[0],pos[1],self.width,self.width)
        self.window_selection=None

    def collide(self,mouse):
        if self.rect.collidepoint(mouse):
            return True

    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))
