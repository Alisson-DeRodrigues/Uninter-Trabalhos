import pygame
from code.Const import deposit_data
from code.Entity import Entity
from code.import_archive import import_folder

class DepositOre(Entity):
    def __init__(self, deposit_name, pos, groups, obstacle_sprites, add_loot):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'deposit_ore'
        self.frame_index = 0
        self.deposit_name = deposit_name
        self.amount = deposit_data[deposit_name]['amount']
        self.add_loot = add_loot

        # graphic setup
        self.import_deposit_graphics(deposit_name)
        self.stage = 'stage_3'
        self.image = self.animations[self.stage][self.frame_index]
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.animations = {}
        self.obstacle_sprites = obstacle_sprites

    def import_deposit_graphics(self, name):
        self.animations = {'full': [], 'stage_0': [], 'stage_1': [], 'stage_2': [], 'stage_3': [], 'stage_4': []}
        main_path = f'./Mapa/DepositOre/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_action(self, attack_type):
        # mining
        if attack_type == 'tool':
            self.add_loot(self.deposit_name, self.amount)

