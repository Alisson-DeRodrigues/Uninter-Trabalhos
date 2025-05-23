import pygame
from code.Const import *
from code.import_archive import import_folder
from code.Entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, summon_tool, destroy_summon_tool, menu):
        super().__init__(groups)

        # graphics setup
        self.image = pygame.image.load('./Mapa/Player/right/right_0.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -26)
        self.import_player_assets()
        self.status = 'right'

        self.obstacle_sprites = obstacle_sprites

        # tool
        self.summon_tool = summon_tool
        self.destroy_summon_tool = destroy_summon_tool
        self.tool_index = 0
        self.tool = list(tool_data.keys())[self.tool_index]
        self.can_switch_tool = True
        self.tool_switch_time = None
        self.switch_duration_cooldown = 200

        # stats
        self.stats = {'health': 300, 'attack': 10, 'speed': 5}
        self.health = self.stats['health']
        self.exp = 000
        self.speed = self.stats['speed']
        self.using_tool = False
        self.tool_cooldown = 400
        self.tool_time = None

        # damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

        # menu
        self.menu = menu
        self.can_activate_menu = True
        self.menu_activation_time = None
        self.activation_menu_cooldown = 200

        # inventory
        self.inventory = {'corn': 0, 'tomato': 0, 'stone': 0, 'coal': 0, 'iron': 0}

    def import_player_assets(self):
        character_path = './Mapa/Player/'
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [],'left_idle': [],'up_idle': [],'down_idle': [],
            'right_attack': [],'left_attack': [],'up_attack': [],'down_attack': [],
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.using_tool:
            keys = pygame.key.get_pressed()
            # movement input
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # attack input
            if keys[pygame.K_SPACE]:
                self.using_tool = True
                self.tool_time = pygame.time.get_ticks()
                self.summon_tool()

            if keys[pygame.K_q] and self.can_switch_tool:
                self.can_switch_tool = False
                self.tool_switch_time = pygame.time.get_ticks()

                if self.tool_index < len(list(tool_data.keys())) - 1:
                    self.tool_index += 1
                else:
                    self.tool_index = 0
                self.tool = list(tool_data.keys())[self.tool_index]

            # menu
            if keys[pygame.K_m] and self.can_activate_menu:
                self.menu()
                self.can_activate_menu = False
                self.menu_activation_time = pygame.time.get_ticks()


    def get_status(self):

        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.using_tool:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    if 'attack' in self.status:
                        self.status = self.status + '_attack'
        else:
            self.status = self.status.replace('_attack', '')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.using_tool:
            if current_time - self.tool_time >= self.tool_cooldown + tool_data[self.tool]['cooldown']:
                self.using_tool = False
                self.destroy_summon_tool()

        if not self.can_switch_tool:
            if current_time - self.tool_switch_time >= self.switch_duration_cooldown:
                self.can_switch_tool = True

        if not self.can_activate_menu:
            if current_time - self.menu_activation_time >= self.activation_menu_cooldown:
                self.can_activate_menu = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(center = self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_tool_damage(self):
        base_damage = self.stats['attack']
        tool_damage = tool_data[self.tool]['damage']
        return base_damage + tool_damage

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
