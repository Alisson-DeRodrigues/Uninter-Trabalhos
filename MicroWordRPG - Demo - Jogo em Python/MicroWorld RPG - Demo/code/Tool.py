import pygame

class Tool(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'tool'
        direction = player.status.split('_')[0]

        # graphics
        full_path = f'./Mapa/Tool/{player.tool}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 4)

        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,0))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0, 0))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-4, -8))
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(4, 4))
        else:
            self.rect = self.image.get_rect(center = player.rect.center)