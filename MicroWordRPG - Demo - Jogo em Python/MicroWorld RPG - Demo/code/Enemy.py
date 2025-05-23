from pygame.math import Vector2
from code.Const import *
from code.Entity import Entity
from code.import_archive import *

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player, add_exp):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.animation = {}
        self.image = self.animations[self.status][self.frame_index]
        self.obstacle_sprites = obstacle_sprites

        # movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -26)

        # stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.damage_player = damage_player
        self.add_exp = add_exp

        # invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'./Mapa/Enemy/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()


        return distance, direction

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0] # 0 para distance e 1 para direction

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage, self.attack_type)
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1] # retorna a direção do player
        else:
            self.direction = pygame.math.Vector2() # retorna as coordenadas do player

    def animate(self):
        self.animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        # set the image
        self.image = self.animation[int(self.frame_index)]
        self.image = pygame.transform.scale_by(self.image, 4) #ativar na troca de sprite
        self.rect = self.image.get_rect(center=self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        # cooldown do ataque
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True


    def get_damage(self, player,attack_type):

        if self.vulnerable:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'tool':
                self.health -= player.get_full_tool_damage()
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False


    def check_death(self):
        if self.health <= 0:
            self.kill() # kill o enemy quando a vida chegar em zero
            self.add_exp(self.exp)

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance # aplica knock back nos ataques

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()

    def enemy_update(self, player):
         self.get_status(player)
         self.actions(player)