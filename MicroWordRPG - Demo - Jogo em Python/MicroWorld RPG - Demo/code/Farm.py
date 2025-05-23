import pygame
from code.Const import farm_data
from code.Entity import Entity
from code.import_archive import import_folder

class Farm(Entity):
    def __init__(self, farm_name, pos, groups, obstacle_sprites, add_loot):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'farm'
        self.frame_index = 0
        self.pos = pos

        # graphic setup
        self.import_farm_graphics(farm_name)
        self.stage = 'stage_4'
        self.image = self.animations[self.stage][self.frame_index]
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # farming
        self.farm_name = farm_name
        self.amount = farm_data[farm_name]['amount']
        self.stage_time = 2000
        self.farming_time = None
        self.can_farming = True

        self.add_loot = add_loot

    def import_farm_graphics(self, name):
        self.animations = {'full': [], 'stage_0': [], 'stage_1': [], 'stage_2': [], 'stage_3': [], 'stage_4': []}
        main_path = f'./Mapa/Farm/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_action(self, attack_type):
        # farming
        if attack_type == 'tool':
            if self.can_farming:
                self.can_farming = False
                self.farming_time = pygame.time.get_ticks()
                self.add_loot(self.farm_name, self.amount)

    def farm_growth(self):
        current_time = pygame.time.get_ticks()
        if not self.can_farming:
            if self.stage == 'stage_4':
                self.stage = 'stage_0'
                self.draw()
                self.farming_time = pygame.time.get_ticks()
            if self.stage == 'stage_0' and current_time - self.farming_time >= self.stage_time:
                self.stage = 'stage_1'
                self.draw()
                self.farming_time = pygame.time.get_ticks()
            if self.stage == 'stage_1' and current_time - self.farming_time >= self.stage_time:
                self.stage = 'stage_2'
                self.draw()
            if self.stage == 'stage_2' and current_time - self.farming_time >= self.stage_time:
                self.stage = 'stage_3'
                self.draw()
                self.farming_time = pygame.time.get_ticks()
            if self.stage == 'stage_3' and current_time - self.farming_time >= self.stage_time:
                self.stage = 'stage_4'
                self.draw()
                self.can_farming = True

    def draw(self):
        self.image = self.animations[self.stage][self.frame_index]
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft=self.pos)

    def farm_update(self):
        self.farm_growth()