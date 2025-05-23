from code.Const import *
from code.DepositOre import DepositOre
from code.Enemy import Enemy
from code.Farm import Farm
from code.Tile import Tile
from code.Player import Player
from code.UI import UI, Menu
from code.import_archive import *
from code.Tool import Tool

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # tool_sprites
        self.current_tool = None
        self.tool_sprites = pygame.sprite.Group()
        self.interactable_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # user interface
        self.ui = UI()
        self.menu = Menu()
        self.active_menu = True

    def create_map(self):

        layouts = {
            'object': import_csv_layout('./Mapa/CSV/MapaPrincipal_Objects.csv'),
            'barrier': import_csv_layout('./Mapa/CSV/MapaPrincipal_Barrier.csv'),
            'farm': import_csv_layout('./Mapa/CSV/MapaPrincipal_Farm.csv'),
            'deposit_ore': import_csv_layout('./Mapa/CSV/MapaPrincipal_DepositOre.csv'),
            'entities': import_csv_layout('./Mapa/CSV/MapaPrincipal_Entities.csv'),
            'teste': import_csv_layout('./Mapa/CSV/MapaPrincipal_Teste.csv'),
        }
        graphics = {
            'objects': import_folder('./Mapa/Tilemap'),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        match style:
                            case 'object':
                                surf = graphics['objects'][
                                    int(col)]
                                surf = pygame.transform.scale_by(surf, 4)
                                if col == '80':
                                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'barn', surf)
                                else:
                                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                            case 'barrier':
                                Tile((x, y), [self.obstacle_sprites], 'barrier')
                            case 'deposit_ore':
                                if col == '12':
                                    DepositOre('stone', (x, y),
                                               [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites],
                                               self.obstacle_sprites, self.add_loot)
                                if col == '21':
                                    DepositOre('coal', (x, y),
                                               [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites],
                                               self.obstacle_sprites, self.add_loot)
                                if col == '29':
                                    DepositOre('iron', (x, y),
                                               [self.visible_sprites, self.obstacle_sprites, self.interactable_sprites],
                                               self.obstacle_sprites, self.add_loot)
                            case 'farm':
                                if col == '44':
                                    Farm('corn', (x, y), [self.visible_sprites, self.interactable_sprites],
                                         self.obstacle_sprites, self.add_loot)
                                if col == '36':
                                    Farm('tomato', (x, y), [self.visible_sprites, self.interactable_sprites],
                                         self.obstacle_sprites, self.add_loot)
                            case 'entities':
                                if col == '55':
                                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites,
                                                         self.summon_tool, self.destroy_summon_tool, self.menu)
                                else:
                                    if col == '66':
                                        monster_name = 'beast'
                                    else:
                                        monster_name = 'beast'
                                    Enemy(monster_name, (x, y), [self.visible_sprites, self.interactable_sprites],
                                          self.obstacle_sprites, self.damage_player, self.add_exp)

    def summon_tool(self):
        self.current_tool = Tool(self.player, [self.visible_sprites, self.tool_sprites])

    def destroy_summon_tool(self):
        if self.current_tool:
            self.current_tool.kill()
        self.current_tool = None

    def menu(self):
        if self.active_menu:
            self.menu.disable_menu()
            self.active_menu = False
        else:
            self.menu.activate_menu()
            self.active_menu = True

    def player_tool_logic(self):
        if self.tool_sprites:
            for tool_sprite in self.tool_sprites:
                collision_sprites = pygame.sprite.spritecollide(tool_sprite, self.interactable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'enemy':
                            target_sprite.get_damage(self.player, tool_sprite.sprite_type)
                        elif target_sprite.sprite_type == 'deposit_ore' and self.player.tool_index == 2:  # 2 == pickaxe
                            target_sprite.get_action(tool_sprite.sprite_type)
                            target_sprite.kill()
                        elif target_sprite.sprite_type == 'farm' and self.player.tool_index == 1:  # 1 == sickle
                            target_sprite.get_action(tool_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()

    def add_exp(self, amount):
        # add experience
        self.player.exp += amount

    def add_loot(self, name, amount):
        self.player.inventory[name] += amount

    def run(self):
        # update and drawn the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_tool_logic()
        self.ui.display(self.player)
        self.visible_sprites.farm_update()
        self.menu.info_menu()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('./Mapa/MapaPrincipal.png').convert()
        self.floor_surf = pygame.transform.scale_by(self.floor_surf, 4)
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # applies correct sprite overlays
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if
                         hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)

    def farm_update(self):
        farm_sprites = [sprite for sprite in self.sprites() if
                        hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'farm']
        for farm in farm_sprites:
            farm.farm_update()
