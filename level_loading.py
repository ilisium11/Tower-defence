from random import randint


class LevelLoading:
    width_road=None
    half_width_road=None

    def __init__(self,road_list):
        self.wave_list=[]
        self.waves_list=[]
        self.road_list=road_list
        self.random_position=None

    def create_new_wave(self):
        self.waves_list.append(self.wave_list)
        self.wave_list=[]

    def no_wave(self):
        self.waves_list.append(None)
        self.wave_list=[]

    def new_road(self,road_list):
        self.waves_list=[]
        self.road_list=road_list

    def two_lines(self,enemy,availability_shield,deviation,count_enemy,delay_across_enemy,delay_across_mini_wave):
        mini_wave_list=[]
        type_enemy=enemy[0]
        level_enemy=enemy[1]
        pos1=-deviation*LevelLoading.width_road
        pos2=deviation*LevelLoading.width_road
        if self.road_list[0][0]==self.road_list[1][0]:
            pos1=(self.road_list[0][0]+pos1,self.road_list[0][1])
            pos2 = (self.road_list[0][0]+pos2, self.road_list[0][1])
        else:
            pos1=(self.road_list[0][0],self.road_list[0][1]+pos1)
            pos2 = (self.road_list[0][0], self.road_list[0][1] + pos2)
        for w in range(count_enemy):
            two_enemy=(type_enemy(level_enemy,availability_shield),type_enemy(level_enemy,availability_shield))
            two_enemy[0].set_center(*pos1)
            two_enemy[1].set_center(*pos2)
            self.set_path(two_enemy[0])
            self.set_path(two_enemy[1])
            mini_wave_list.append(two_enemy)
        mini_wave_list.append(delay_across_enemy)
        mini_wave_list.append(delay_across_mini_wave)
        self.wave_list.append(mini_wave_list)

    def chaotic(self,enemy,availability_shield,count_enemy,delay_across_enemy,delay_across_mini_wave):
        mini_wave_list = []
        type_enemy=enemy[0]
        level_enemy=enemy[1]
        if self.road_list[0][0]==self.road_list[1][0]:
            lower_bound = round(self.road_list[0][0]-type_enemy.half_width)
            upper_bound = round(self.road_list[0][0]+type_enemy.half_width)
            self.random_position = lambda: (randint(lower_bound, upper_bound), self.road_list[0][1])
        else:
            lower_bound = round(self.road_list[0][1]-type_enemy.half_width)
            upper_bound = round(self.road_list[0][1]+type_enemy.half_width)
            self.random_position = lambda: (self.road_list[0][0], randint(lower_bound, upper_bound))
        for w in range(count_enemy):
            enemy=type_enemy(level_enemy,availability_shield)
            enemy.set_center(*self.random_position())
            self.set_path(enemy)
            mini_wave_list.append(enemy)
        mini_wave_list.append(delay_across_enemy)
        mini_wave_list.append(delay_across_mini_wave)
        self.wave_list.append(mini_wave_list)

    def set_path(self,enemy):
        list1=self.road_list
        if list1[0][0] == list1[1][0]:
            t1 = 1
            enemy.direction=1
            list2 = [[enemy.x, list1[0][1]]]
            if list1[0][1]-list1[1][1]<0:
                enemy.local_speed=enemy.speed
            else:
                enemy.local_speed = -enemy.speed
        else:
            t1 = 0
            enemy.direction = 0
            list2 = [[list1[0][0], enemy.y]]
            if list1[0][0] - list1[1][0] < 0:
                enemy.local_speed = enemy.speed
            else:
                enemy.local_speed = -enemy.speed
        enemy.len_path=len(self.road_list)
        enemy.position_path=0
        distance_to_end=0
        for i in range(1, len(list1)):
            if i % 2 == t1:
                if i < len(list1) - 1:
                    difference = list2[i - 1][0] - list1[i - 1][0]
                    if list1[i - 1][1] - list1[i][1] < 0:
                        difference1 = -difference
                    else:
                        difference1 = difference
                    if difference > 0:
                        if list1[i + 1][0] - list1[i][0] > 0:
                            list2.append([list2[i - 1][0], list1[i][1] + difference1])
                        else:
                            list2.append([list2[i - 1][0], list1[i][1] - difference1])
                    else:
                        if list1[i + 1][0] - list1[i][0] < 0:
                            list2.append([list2[i - 1][0], list1[i][1] - difference1])
                        else:
                            list2.append([list2[i - 1][0], list1[i][1] + difference1])
                    list2[-1][1]=round(list2[-1][1],1)
                else:
                    list2.append([list2[i - 1][0], list1[i][1]])
                distance_to_end += abs(list2[-1][1] - list2[-2][1])
            else:
                if i < len(list1) - 1:
                    difference = list2[i - 1][1] - list1[i - 1][1]
                    if list1[i][0] - list1[i - 1][0] < 0:
                        difference1 = -difference
                    else:
                        difference1 = difference
                    if difference > 0:
                        if list1[i + 1][1] - list1[i][1] > 0:
                            list2.append([list1[i][0] - difference1, list2[i - 1][1]])
                        else:
                            list2.append([list1[i][0] + difference1, list2[i - 1][1]])
                    else:
                        if list1[i + 1][1] - list1[i][1] < 0:
                            list2.append([list1[i][0] + difference1, list2[i - 1][1]])
                        else:
                            list2.append([list1[i][0] - difference1, list2[i - 1][1]])
                    list2[-1][0] = round(list2[-1][0], 1)
                else:
                    list2.append([list1[i][0],list2[i - 1][1]])
                distance_to_end += abs(list2[-1][0] - list2[-2][0])
        enemy.path=list2
        enemy.distance_to_end=distance_to_end
        enemy.lower_border = enemy.path[enemy.position_path + 1][enemy.direction]-enemy.half_speed
        enemy.upper_border = enemy.path[enemy.position_path + 1][enemy.direction]+enemy.half_speed

    @staticmethod
    def scaling_attributes(width):
        LevelLoading.width_road=width
        LevelLoading.half_width_road=round(width/2,1)


class WaveLoading:
    def __init__(self,waves):
        self.waves=waves
        self.wave=None
        self.enemy_list=[]
        self.number_wave = -1
        self.number_mini_wave = 0
        self.delay_enemy=0
        self.delay_mini_wave=0
        self.n=0
        self.counter_enemy=0
        self.n1=0
        self.count_mini_wave=0

    def switching_mini_wave(self):
        mini_wave=self.wave[self.number_mini_wave]
        self.delay_enemy=mini_wave[-2]
        self.delay_mini_wave=mini_wave[-1]
        self.enemy_list=mini_wave[0:-2]
        self.counter_enemy = 0
        self.n1= 0

    def switching_wave(self):
        self.number_wave+=1
        self.wave=self.waves[self.number_wave]
        if self.wave:
            self.count_mini_wave=len(self.wave)-1
            self.number_mini_wave=0
            self.switching_mini_wave()

    def generation_enemy(self,wave):
        if self.wave:
            if self.counter_enemy < len(self.enemy_list):
                if self.n % self.delay_enemy == 0:
                    if type(self.enemy_list[self.counter_enemy]) is tuple:
                        for j in self.enemy_list[self.counter_enemy]:
                            wave.append(j)
                    else:
                        wave.append(self.enemy_list[self.counter_enemy])
                    self.counter_enemy += 1
                self.n += 1
                return 1
            elif self.number_mini_wave < self.count_mini_wave:
                if self.n1 == self.delay_mini_wave:
                    self.n = 0
                    self.number_mini_wave += 1
                    self.switching_mini_wave()
                else:
                    self.n1 += 1
                return 1
            elif self.number_mini_wave == self.count_mini_wave:
                return 0
        else:
            return 0
