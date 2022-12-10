import pygame as pg


class BulletShotgun:
    def __init__(self, tower, x, y, sin, cos):
        self.destruction_armor=tower.destruction_armor
        self.color = tower.color_bullet
        self.damage = tower.damage
        self.speed = tower.speed_bullet
        self.size = tower.size_bullet
        self.x = x
        self.y = y
        self.x_speed = cos * self.speed
        self.y_speed = sin * self.speed
        self.n = 0
        self.old_x = None
        self.old_y = None
        self.punching = tower.punching
        self.damage_shield = tower.damage_shield
        self.target = tower.target

    def move(self, wave, list_killed_enemy):
        self.old_x = self.x
        self.old_y = self.y
        self.x = self.x + self.x_speed
        self.y = self.y - self.y_speed
        self.n += 1
        for target in reversed(wave):
            if target.rect.collidepoint(self.x, self.y):
                if target.shield > 0:
                    target.shield -= self.damage * self.damage_shield
                    if target.shield <= 0:
                        target.shield = 0
                        target.shield_img = None
                else:
                    damage = self.damage * (1 - target.armor * (1-self.punching))
                    target.health -= damage
                    if target.health <= 0 and target in wave:
                        target.health = 0
                        wave.remove(target)
                        list_killed_enemy.append(target)
                    elif target.armor>0:
                        target.armor-=self.destruction_armor
                        target.armor=round(target.armor,4)
                        if target.armor<=0:
                            target.armor=0
                return True
        if self.n > 120:
            return True

    def draw(self, surface):
        pg.draw.circle(surface, self.color, (self.x, self.y), self.size)
