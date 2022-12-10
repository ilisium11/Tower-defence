RED=(255,0,0)
Black=(0,0,0)


class Button1:
    def __init__(self,pos,image,surface=None):
        self.image=image
        self.width=image.get_width()
        self.height=image.get_height()
        self.center = self.image.get_rect(center=(pos[0], pos[1]))
        self.x=pos[0]-round(self.width/2,1)
        self.y=pos[1]-round(self.height/2,1)
        self.surface=surface

    def collide(self,x1,y1):
        if self.x<x1<self.x+self.width:
            if self.y<y1<self.y+self.height:
                return True
        else:
            return False

    def draw(self):
        self.surface.blit(self.image, self.center)


class TextButton(Button1):

    def __init__(self,pos,image,surface,font,text):
        super().__init__(pos,image,surface)
        self.text=font.render(text, True, RED)
        self.center=self.image.get_rect(center=pos)
        self.center_text=self.text.get_rect(center=pos)

    def draw(self):
        super().draw()
        self.surface.blit(self.text,self.center_text)


class AlgButton(Button1):

    def __init__(self,pos,image,surface,font,text,algoritm):
        super().__init__(pos,image,surface)
        self.text=font.render(text, True, RED)
        self.center=self.image.get_rect(center=pos)
        self.center_text=self.text.get_rect(center=pos)
        self.algoritm=algoritm

    def draw(self):
        super().draw()
        self.surface.blit(self.text,self.center_text)


class LevelButton(Button1):
    def __init__(self,pos,image,surface,text,font,level):
        super().__init__(pos,image,surface)
        self.center=self.image.get_rect(center=(pos[0],pos[1]))
        self.level=level
        self.text=font.render(text,True,Black)
        self.text_center=self.text.get_rect(center=(pos[0],pos[1]))

    def draw(self):
        self.surface.blit(self.image,self.center)
        self.surface.blit(self.text, self.text_center)


class MovingButton(Button1):
    def __init__(self,pos,image,surface):
        super().__init__(pos,image,surface)
        self.moving=None

    def collide(self,x1,y1):
        self.moving=super().collide(x1,y1)

    def set_pos_x(self,x):
        self.x=x-round(self.width/2,1)
        self.center.x=self.x

    def draw(self):
        self.surface.blit(self.image,self.center)
