from enemy1 import Enemy1
from enemy2 import Enemy2
from enemy3 import Enemy3
from enemy4 import Enemy4
from enemy5 import Enemy5
import pygame as pg
from level_loading import LevelLoading,WaveLoading
from object_terrain import ObjTerrain
surface=pg.image.load('images/road1.png').convert()
bush=pg.image.load('images/objects_terrain/куст1.png').convert_alpha()
water=pg.image.load('images/objects_terrain/water.png').convert()
stone=pg.image.load('images/objects_terrain/stone.png').convert()
stone.set_colorkey((255,255,255))


class Levels:
    width_cell=None
    bush=None
    stone=None
    water=None

    @staticmethod
    def level1(width_window=None,height_window=None):
        width=Levels.width_cell
        road_list = [[width * 7.5, -0.5 * width], [width * 7.5, width * 11.5], [width * 3.5, width * 11.5],[width * 3.5, width * 15.5], [width * 27.5, width * 15.5], [width * 27.5, width * 9.5]]
        path_list = [road_list]
        water_cells=[(8, 7), (8, 8), (8, 9), (8, 10),(9, 8), (9, 9), (9, 10), (9, 11), (9, 12),(10,11),(10,12),(11,11),(11,12),(12,11),(12,12),(13,12),(13,13),
        (0,11),(1,11),(2,11),(0,12),(1,13),(1,14),(1,12),(1,15),(2,15),(2,16),(2,17),
                     (21,16),(22,16),(23,16),(21,17),(22,17),(23,17),

                     ]

        def return_window(w,h):
            window=surface.copy()
            window=pg.transform.scale(window,(w,h))
            Levels.draw_road(window,path_list)
            Levels.draw_water(window,water_cells)
            return window

        if width_window:
            return return_window(width_window,height_window)

        half_width = round(width / 2, 1)

        bush_cells = [(5,6),(5,7),(5,8),(5,9),(5,10),(4,6),(4,7),(4,8),(6,4),(6,3),(6,2),(6,1),(5,4),
                      (0, 10), (1, 10), (2, 10),(3,10),(16,16),(17,17),(18,16),(19,17),(20,16),(20,17),
                      (12,16),(13,16),(13,17),(14,16),(14,17),(15,16),(15,17),
                      (6, 16), (7, 16), (8, 17), (9, 16), (10, 17), (11, 16),
                      (16,13),(17,13),(18,13),(19,13),(20,13),(20,13),
                      (18, 14), (19, 14), (20, 14), (21, 14), (22, 14), (23, 14),
                      (6,13),(8,11),(10,14),(11,14),(9,5),(9,6),(10,7)
                      ]
        bushes=Levels.create_bush(bush_cells)
        stone_cells=[
            (6,14),(4,14),(5,14),(7,12),(8,12),(13,14),(14,14),(15,14),
            (8,1),(8,2),(8,2),(8,3),(9,4)
        ]
        stones=Levels.create_stone(stone_cells)
        closed_cells=[]
        for i in range(1,len(road_list)):
            if road_list[i][0]==road_list[i-1][0]:
                dif=road_list[i][1]-road_list[i-1][1]
                k=dif//width
                cell_by_x=(road_list[i - 1][0] - half_width) // width
                cell_by_y = (road_list[i - 1][1] - half_width) // width
                if k>0:
                    t=1
                else:
                    t=-1
                for j in range(abs(int(k))):
                    closed_cells.append((cell_by_x,cell_by_y+t*j))
            else:
                dif=road_list[i][0]-road_list[i-1][0]
                k=dif//width
                cell_by_x = (road_list[i - 1][0] - half_width) // width
                cell_by_y = (road_list[i - 1][1] - half_width) // width
                if k>0:
                    t=1
                else:
                    t=-1
                for j in range(abs(int(k))):
                    closed_cells.append((cell_by_x+t*j,cell_by_y))
        closed_cells.extend(bush_cells)
        closed_cells.extend(stone_cells)
        closed_cells.extend(water_cells)
        roads=[]
        road = LevelLoading(road_list)
        road.no_wave()
        road.chaotic((Enemy1,1),True,4,80,200),road.chaotic((Enemy1,2),True,4,40,200),road.chaotic((Enemy1,3),True,4,80,200),road.create_new_wave()
        road.chaotic((Enemy2,1),True,4,80,200), road.chaotic((Enemy2,2),True,4,80,200), road.chaotic((Enemy2,3),True,4,80,200),road.create_new_wave()
        road.chaotic((Enemy3, 1), True, 4, 80, 200), road.chaotic((Enemy3, 2), True, 4, 80, 200), road.chaotic((Enemy3, 3), True, 4, 80, 200), road.create_new_wave()
        road.chaotic((Enemy4, 1), True, 4, 80, 200), road.chaotic((Enemy4, 2), True, 4, 80, 200), road.chaotic((Enemy4, 3), True, 4, 80, 200), road.create_new_wave()
        road.chaotic((Enemy5, 1), True, 4, 80, 200), road.chaotic((Enemy5, 2), True, 4, 80, 200), road.chaotic((Enemy5, 3), True, 4, 80, 200), road.create_new_wave()
        roads.append(WaveLoading(road.waves_list))
        delay_level=[1000,500,500,500,500,500]
        health=1000
        money=500000
        return health,money,roads,delay_level,closed_cells,bushes,stones

    @staticmethod
    def level2():
        width = Levels.width_cell
        road_list = [[width * 10, 0], [width * 10, width * 12], [width * 3, width * 12], [width * 3, width * 20]]
        for i in range(len(road_list)):
            road_list[i][0] = round(road_list[i][0], 1)
            road_list[i][1] = round(road_list[i][1], 1)
        wave = [0, [2, (Enemy1, False), 20, 200, 100], [2, (Enemy2, True), 1, 24, 100]]
        delay_level = [1200]
        waves1=[]
        waves1.append(wave)
        waves = []
        waves.append(waves1)
        path_list = [road_list]
        health=10
        money=1000
        max_level_tower=2
        return health,money,max_level_tower,waves,delay_level,path_list

    @staticmethod
    def draw_road(window,path_list):
        for road_list in path_list:
            list1=road_list
            width=Levels.width_cell
            rect=pg.Rect(0,0,width,width)
            for i in range(len(list1) - 1):
                if road_list[i][0] == road_list[i+1][0]:
                    dif=(road_list[i][1]-road_list[i+1][1])//width
                    if dif>0:
                        t=-width
                    else:
                        t=width
                    for j in range(abs(int(dif))):
                        rect.center=(road_list[i][0],road_list[i][1]+t*j)
                        pg.draw.rect(window,(0,0,0),rect)
                else:
                    dif=(road_list[i][0]-road_list[i+1][0])//width
                    if dif>0:
                        t=-width
                    else:
                        t=width
                    for j in range(abs(int(dif))):
                        rect.center=(road_list[i][0]+t*j,road_list[i][1])
                        pg.draw.rect(window,(0,0,0),rect)

    @staticmethod
    def create_bush(bush_cells):
        bushes=[]
        for bush_cell in bush_cells:
            bushes.append(ObjTerrain(Levels.bush,'Куст',100,(bush_cell[0]*Levels.width_cell,bush_cell[1]*Levels.width_cell),bush_cell))
        return bushes

    @staticmethod
    def create_stone(stone_cells):
        stones=[]
        for stone_cell in stone_cells:
            stones.append(ObjTerrain(Levels.stone,'Куст',100,(stone_cell[0]*Levels.width_cell,stone_cell[1]*Levels.width_cell),stone_cell))
        return stones

    @staticmethod
    def draw_water(window,water_cells):
        for water_cell in water_cells:
            window.blit(Levels.water,(water_cell[0]*Levels.width_cell,water_cell[1]*Levels.width_cell))

    @staticmethod
    def scaling_attributes(width_cell):
        Levels.width_cell=width_cell
        Levels.bush=pg.transform.scale(bush,(width_cell,width_cell))
        Levels.water = pg.transform.scale(water, (width_cell, width_cell))
        Levels.stone = pg.transform.scale(stone, (width_cell, width_cell))
        LevelLoading.scaling_attributes(width_cell)
        width_enemy = round(width_cell / 2.5, 1)
        Enemy1.scaling_attributes(width_cell,width_enemy)
        Enemy2.scaling_attributes(width_cell,width_enemy)
        Enemy3.scaling_attributes(width_cell, width_enemy)
        Enemy4.scaling_attributes(width_cell,width_enemy)
        Enemy5.scaling_attributes(width_cell, width_enemy)
