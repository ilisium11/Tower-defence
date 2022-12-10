import pygame as pg
import sys
from Shotgun_tower import Shotgun
from Turret_tower import Turret
from Laser_tower import Laser
from selected_enemy import SelectedEnemy
from selected_tower import SelectedTower
from player import Player
from buy_towers import MenuTowers
from object_terrain import WindowObjTerrain
from fast_menu import MenuGame
from end_game import EndGame


YELLOW=(255,255,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
ORANGE=(255,165,0)
Blue=(0,0,255)
Clock=pg.time.Clock()
GREEN_1=(100,255,0)
RED1=(150,50,50)
font=pg.font.SysFont('arial',30)


def lose():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                run = False


class Moving:
    road=None
    width=None
    width_cell=None
    half_width_cell=None
    surface_true = None
    half_width = None

    def __init__(self,image,surface):
        self.image=image
        self.x=0
        self.y=0
        self.surface=surface
        self.true_place=False

    def move(self,x,y,closed_cells):
        cell_by_x=x//self.width_cell
        cell_by_y=y//self.width_cell
        self.x=cell_by_x*self.width_cell+self.half_width_cell
        self.y = cell_by_y * self.width_cell + self.half_width_cell
        center_img=self.image.get_rect(center=(self.x,self.y))
        lokal_surface=Moving.surface_true.copy()
        center_surf=lokal_surface.get_rect(center=(self.x,self.y))
        self.true_place=True
        if (cell_by_x,cell_by_y) in closed_cells:
            self.true_place=False
            lokal_surface.fill(RED1)
        else:
            lokal_surface.fill(GREEN_1)
        self.surface.blit(lokal_surface,center_surf)
        self.surface.blit(self.image,center_img)

    @staticmethod
    def scaling_moving(width_tower):
        width = width_tower
        Moving.width_cell=width
        Moving.half_width_cell=round(width/2,1)
        Moving.surface_true = pg.Surface((width, width))
        Moving.half_width = round(width / 2, 2)


class Game:

    @staticmethod
    def scaling_attributes(width_cell,w,h):
        width_tower=width_cell
        height_tower=round((width_tower*4)/3,1)
        Turret.scaling_attributes(width_tower,height_tower,w,h)
        Shotgun.scaling_attributes(width_tower,height_tower,w,h)
        Laser.scaling_attributes(width_tower,height_tower,w,h)
        Moving.scaling_moving(width_tower)
        SelectedEnemy.scaling_attributes(w,h)
        SelectedTower.scaling_attributes(w,h)
        Player.scaling_attributes(w,h)
        MenuTowers.scaling_attributes(w,h)
        WindowObjTerrain.scaling_attributes(w,h,width_cell)
        MenuGame.scaling_attributes(w,h)
        EndGame.scaling_attributes(w,h)

    def __init__(self,surface,level,window,width_cell):
        self.run=True
        self.clock=pg.time.Clock()
        self.surface = surface
        self.level=level
        health, money, roads, delay_level,closed_cells,bushes,stones=self.level()
        self.objects=[]
        self.objects.extend(bushes)
        self.objects.extend(stones)
        self.roads=roads
        self.window=window
        self.number_wave = 1
        self.player=Player(surface,health,money,self.number_wave,len(delay_level))
        self.menu_game=MenuGame(self.surface)
        self.end_game=EndGame(self.surface)
        self.width_cell=width_cell
        self.closed_cells=[]
        self.closed_cells.extend(closed_cells)
        self.max_level_tower = 6
        self.delay_level=delay_level
        self.background_menu=pg.Surface((surface.get_width(),surface.get_height()),pg.SRCALPHA)
        self.background_menu.fill(BLACK)
        self.background_menu.set_alpha(150)
        self.distance_end = []
        self.Towers = []
        self.wave = []
        self.bullets = []
        self.buttons=[]
        self.moving_object = None
        self.sel_tower=None
        self.click_enemy=None
        self.selected_obj_terrain=None
        self.true_buttons=True
        self.menu_towers=MenuTowers(Turret,Shotgun,Laser)
        self.tower=None
        self.pause_game=False
        self.return_menu=False
        self.restart=False

    def checking_click(self,mouse):
        self.sel_tower = None
        self.click_enemy = None
        self.selected_obj_terrain = None
        if self.true_buttons:
            button=self.menu_towers.click_buttons(mouse)
            if button:
                self.moving_object = Moving(button.image_tower, self.surface)
                self.true_buttons=None
                self.tower=button.tower
                return True
        for i in self.Towers:
            if i.get_rect().collidepoint(mouse):
                self.sel_tower = SelectedTower(self.surface,i)
                self.true_buttons = False
                return True
        for i in self.wave:
            if i.rect.collidepoint(mouse):
                self.click_enemy = SelectedEnemy(self.surface, i)
                return True
        for obj in self.objects:
            if obj.collide(mouse):
                self.selected_obj_terrain = WindowObjTerrain(obj)

    def selected_obj_collide(self,mouse):
        if self.selected_obj_terrain.collide_accept_button(mouse):
            self.del_object()
        elif self.selected_obj_terrain.collide_cansel_button(mouse):
            self.selected_obj_terrain = None

    def new_tower(self):
        if self.player.money>=self.tower.get_cost_tower():
            x,y=self.moving_object.x,self.moving_object.y
            self.Towers.append(self.tower(x, y, self.surface))
            self.closed_cells.append((x//self.width_cell,y//self.width_cell))
            self.player.money -= self.Towers[-1].cost_upgrade
            self.moving_object = None
            self.true_buttons = True

    def upgrade_tower(self):
        if self.sel_tower.level + 1 < self.max_level_tower:
            if self.sel_tower.cost_upgrade <= self.player.money:
                self.sel_tower.tower.upgrade()
                self.player.money -= self.sel_tower.cost_upgrade
                self.sel_tower = SelectedTower(self.surface,self.sel_tower.tower)

    def sell_tower(self):
        x,y=self.sel_tower.tower.x,self.sel_tower.tower.y
        self.player.money += self.sel_tower.start_cost*0.3
        self.Towers.remove(self.sel_tower.tower)
        self.sel_tower = None
        self.true_buttons = True
        self.closed_cells.remove((x//self.width_cell,y//self.width_cell))

    def del_object(self):
        if self.player.money>=self.selected_obj_terrain.cost:
            self.player.money -= self.selected_obj_terrain.cost
            self.objects.remove(self.selected_obj_terrain.obj)
            self.closed_cells.remove(self.selected_obj_terrain.pos_cell)
            self.selected_obj_terrain = None

    def setup_stars(self):
        health=self.player.health
        max_health=self.player.max_health
        stars=0
        if max_health*0.8<health:
            stars=3
        elif max_health*0.5<health:
            stars=2
        elif health>0:
            stars=1
        return stars

    def fast_menu(self):
        self.surface.blit(self.background_menu,(0,0))
        self.menu_game.calling_menu_button.draw()
        self.menu_game.draw_menu()
        self.clock.tick(60)
        pg.display.update()
        run=True
        while run:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if event.button==1:
                        mouse = pg.mouse.get_pos()
                        if self.menu_game.collide_menu_button(mouse):
                            run=False
                            self.run=False
                            self.return_menu=True
                        elif self.menu_game.collide_restart_button(mouse):
                            run=False
                            self.restart=True
                            self.run=False
                        elif self.menu_game.collide_continue_button(mouse):
                            run=False
                            self.menu_game.calling_menu_button.image=self.menu_game.calling_menu_button.image_when_not_clicked

    def end(self):
        self.surface.blit(self.background_menu,(0,0))
        self.end_game.draw_end_game(self.setup_stars())
        self.clock.tick(60)
        pg.display.update()
        run=True
        while run:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if event.button==1:
                        mouse = pg.mouse.get_pos()
                        if self.end_game.collide_continue_button(mouse):
                            run=False
                        elif self.end_game.collide_restart_button(mouse):
                            run=False
                            self.restart=True

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                if self.menu_game.collide_calling_button(mouse):
                    self.fast_menu()
                    return False
                elif self.menu_game.collide_pause_button(mouse):
                    if self.pause_game:
                        self.pause_game = False
                    else:
                        self.pause_game=True
                if not self.moving_object:
                    if self.selected_obj_terrain:
                        if self.selected_obj_terrain.collide(mouse):
                            self.selected_obj_collide(mouse)
                        else:
                            self.checking_click(mouse)
                    elif self.sel_tower:
                        if self.sel_tower.collide(mouse[0], mouse[1]):
                            if self.sel_tower.collide_upgrade_button(mouse):
                                self.upgrade_tower()
                            elif self.sel_tower.collide_sell_button(mouse):
                                self.sell_tower()
                        elif not self.sel_tower.collide_alg_button(mouse):
                            self.true_buttons = True
                            self.checking_click(mouse)
                    else:
                        self.checking_click(mouse)
                elif self.moving_object.true_place:
                    if event.button == 3:
                        self.moving_object = None
                        self.true_buttons = True
                    elif event.button == 1:
                        self.new_tower()

    def game(self):
        count_wave = len(self.delay_level)
        for road in self.roads:
            road.switching_wave()
        count_delay=0
        while self.run:
            self.events()
            if not self.pause_game:
                check_end_wave_roads=0
                for road in self.roads:
                    check_end_wave_roads+=road.generation_enemy(self.wave)
                if check_end_wave_roads==0:
                    if self.number_wave < count_wave:
                        if count_delay == self.delay_level[self.number_wave-1]:
                            self.number_wave += 1
                            self.player.wave+=1
                            for road in self.roads:
                                road.switching_wave()
                            count_delay=0
                        else:
                            count_delay += 1
                            self.player.render_countdown_wave(count_delay,self.delay_level[self.number_wave-1])
                    elif len(self.wave)==0:
                        self.run=False
                for enemy in self.wave:
                    if enemy.run(self.wave):
                        self.wave.remove(enemy)
                        self.player.health-=enemy.cost_hp
                        continue
                killed_enemys = []
                if self.run:
                    for tower in self.Towers:
                        if type(tower)==Laser:
                            tower.attack(self.wave,killed_enemys)
                        else:
                            tower.attack(self.wave, self.bullets)

                for bullet in reversed(self.bullets):
                    if bullet.move(self.wave, killed_enemys):
                        self.bullets.remove(bullet)
                for enemy in killed_enemys:
                    self.player.money+=enemy.cost_money
            self.draws()
            if self.player.health<1:
                self.run=False
        if not self.restart and not self.return_menu:
            self.end()
        return self.restart,self.return_menu

    def draws(self):
        self.surface.blit(self.window, (0, 0))
        self.player.draw()
        self.menu_game.draw_game_buttons()
        for enemy in self.wave:
            enemy.draw(self.surface)
            enemy.draw_health_bar(self.surface)
        for tower in self.Towers:
            tower.draw(self.surface)
        for obj in self.objects:
            obj.draw(self.surface)
        for bullet in self.bullets:
            bullet.draw(self.surface)
        if self.true_buttons:
            self.menu_towers.draw(self.surface)
        elif self.moving_object:
            mouse = pg.mouse.get_pos()
            self.moving_object.move(mouse[0], mouse[1], self.closed_cells)
        if self.click_enemy:
            if self.click_enemy.draw():
                self.click_enemy=None
        if self.sel_tower:
            self.sel_tower.draw()
        if self.selected_obj_terrain:
            self.selected_obj_terrain.draw(self.surface)
        self.clock.tick(60)
        pg.display.update()
