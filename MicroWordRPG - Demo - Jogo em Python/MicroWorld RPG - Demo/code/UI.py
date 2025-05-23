import pygame
from code.Const import *
from code.Entity import Entity


class UI:
    def __init__(self):

        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.font_inv = pygame.font.Font(UI_FONT, UI_FONT_SIZE - 8)

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)

        # convert tool dictionary
        self.tool_graphics = []
        for tool in tool_data.values():
            path = tool['graphic']
            tool = pygame.image.load(path).convert_alpha()
            self.tool_graphics.append(tool)

        self.farm_graphics = []
        for farm in farm_data.values():
            path = farm['graphic']
            farm = pygame.image.load(path).convert_alpha()
            self.farm_graphics.append(farm)

        self.ore_graphics = []
        for ore in deposit_data.values():
            path = ore['graphic']
            ore = pygame.image.load(path).convert_alpha()
            self.ore_graphics.append(ore)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 40
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 10))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(50, 10), 3)

    def show_inventory(self, player):
        x = self.display_surface.get_size()[0]
        y = self.display_surface.get_size()[1]

        # corn
        bg_rect = pygame.Rect(x - 60, y - 440, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        image_surf = self.farm_graphics[0]
        image_surf = pygame.transform.scale_by(image_surf, 3.5)
        image_rect = image_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(image_surf, image_rect)

        text_surf = self.font_inv.render(str(int(player['corn'])), False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright=(x - 25, y - 400))
        self.display_surface.blit(text_surf, text_rect)

        # tomato
        bg_rect = pygame.Rect(x - 60, y - 400, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        image_surf = self.farm_graphics[1]
        image_surf = pygame.transform.scale_by(image_surf, 3.5)
        image_rect = image_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(image_surf, image_rect)

        text_surf = self.font_inv.render(str(int(player['tomato'])), False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright=(x - 25, y - 360))
        self.display_surface.blit(text_surf, text_rect)

        # stone
        bg_rect = pygame.Rect(x - 60, y - 360, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        image_surf = self.ore_graphics[0]
        image_surf = pygame.transform.scale_by(image_surf, 3.5)
        image_rect = image_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(image_surf, image_rect)

        text_surf = self.font_inv.render(str(int(player['stone'])), False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright=(x - 25, y - 320))
        self.display_surface.blit(text_surf, text_rect)

        # coal
        bg_rect = pygame.Rect(x - 60, y - 320, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        image_surf = self.ore_graphics[1]
        image_surf = pygame.transform.scale_by(image_surf, 3.5)
        image_rect = image_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(image_surf, image_rect)

        text_surf = self.font_inv.render(str(int(player['coal'])), False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright=(x - 25, y - 280))
        self.display_surface.blit(text_surf, text_rect)

        # iron
        bg_rect = pygame.Rect(x - 60, y - 280, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        image_surf = self.ore_graphics[2]
        image_surf = pygame.transform.scale_by(image_surf, 3.5)
        image_rect = image_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(image_surf, image_rect)

        text_surf = self.font_inv.render(str(int(player['iron'])), False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright=(x - 25, y - 240))
        self.display_surface.blit(text_surf, text_rect)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    def tool_overlay(self, tool_index, has_switched):
        bg_rect = self.selection_box(10, 400, has_switched)  # weapon
        tool_surf = self.tool_graphics[tool_index]
        tool_surf = pygame.transform.scale_by(tool_surf, 3.5)
        tool_rect = tool_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(tool_surf, tool_rect)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_exp(player.exp)
        self.show_inventory(player.inventory)
        self.tool_overlay(player.tool_index, player.can_switch_tool)


class Menu:
    def __init__(self):
        self.UI_INFO = UI_INFO
        self.UI_INFO_POS = UI_INFO_POS
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.font_inv = pygame.font.Font(UI_FONT, UI_FONT_SIZE - 8)
        self.rect = pygame.Rect(54, 100, 400, 200)

        self.line1_surf = self.font.render(UI_INFO[0], False, TEXT_COLOR)
        self.line1_rect = self.line1_surf.get_rect(topleft=UI_INFO_POS[0])

        self.line2_surf = self.font.render(UI_INFO[1], False, TEXT_COLOR)
        self.line2_rect = self.line2_surf.get_rect(topleft=UI_INFO_POS[1])

        self.line3_surf = self.font.render(UI_INFO[2], False, TEXT_COLOR)
        self.line3_rect = self.line3_surf.get_rect(topleft=UI_INFO_POS[2])

        self.line4_surf = self.font.render(UI_INFO[3], False, TEXT_COLOR)
        self.line4_rect = self.line4_surf.get_rect(topleft=UI_INFO_POS[3])

        self.line5_surf = self.font.render(UI_INFO[4], False, TEXT_COLOR)
        self.line5_rect = self.line5_surf.get_rect(topleft=UI_INFO_POS[4])

        self.line6_surf = self.font.render(UI_INFO[5], False, TEXT_COLOR)
        self.line6_rect = self.line6_surf.get_rect(topleft=UI_INFO_POS[5])

        self.line7_surf = self.font.render(UI_INFO[6], False, TEXT_COLOR)
        self.line7_rect = self.line7_surf.get_rect(topleft=UI_INFO_POS[6])

        self.line8_surf = self.font.render(UI_INFO[7], False, TEXT_COLOR)
        self.line8_rect = self.line8_surf.get_rect(topleft=UI_INFO_POS[7])

    def info_menu(self):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.rect)
        self.display_surface.blit(self.line1_surf, self.line1_rect)
        self.display_surface.blit(self.line2_surf, self.line2_rect)
        self.display_surface.blit(self.line3_surf, self.line3_rect)
        self.display_surface.blit(self.line4_surf, self.line4_rect)
        self.display_surface.blit(self.line5_surf, self.line5_rect)
        self.display_surface.blit(self.line6_surf, self.line6_rect)
        self.display_surface.blit(self.line7_surf, self.line7_rect)
        self.display_surface.blit(self.line8_surf, self.line8_rect)

    def disable_menu(self):
        pos = (-100, -100)
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.line1_surf = self.font.render(UI_INFO[0], False, TEXT_COLOR)
        self.line1_rect = self.line1_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line1_surf, self.line1_rect)

        self.line2_surf = self.font.render(UI_INFO[1], False, TEXT_COLOR)
        self.line2_rect = self.line2_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line2_surf, self.line2_rect)

        self.line3_surf = self.font.render(UI_INFO[2], False, TEXT_COLOR)
        self.line3_rect = self.line3_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line3_surf, self.line3_rect)

        self.line4_surf = self.font.render(UI_INFO[3], False, TEXT_COLOR)
        self.line4_rect = self.line4_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line4_surf, self.line4_rect)

        self.line5_surf = self.font.render(UI_INFO[4], False, TEXT_COLOR)
        self.line5_rect = self.line5_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line5_surf, self.line5_rect)

        self.line6_surf = self.font.render(UI_INFO[5], False, TEXT_COLOR)
        self.line6_rect = self.line6_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line6_surf, self.line6_rect)

        self.line7_surf = self.font.render(UI_INFO[6], False, TEXT_COLOR)
        self.line7_rect = self.line7_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line7_surf, self.line7_rect)

        self.line8_surf = self.font.render(UI_INFO[7], False, TEXT_COLOR)
        self.line8_rect = self.line8_surf.get_rect(topleft=pos)
        self.display_surface.blit(self.line8_surf, self.line8_rect)

    def activate_menu(self):
        self.rect = pygame.Rect(54, 100, 400, 200)
        self.line1_surf = self.font.render(UI_INFO[0], False, TEXT_COLOR)
        self.line1_rect = self.line1_surf.get_rect(topleft=UI_INFO_POS[0])

        self.line2_surf = self.font.render(UI_INFO[1], False, TEXT_COLOR)
        self.line2_rect = self.line2_surf.get_rect(topleft=UI_INFO_POS[1])

        self.line3_surf = self.font.render(UI_INFO[2], False, TEXT_COLOR)
        self.line3_rect = self.line3_surf.get_rect(topleft=UI_INFO_POS[2])

        self.line4_surf = self.font.render(UI_INFO[3], False, TEXT_COLOR)
        self.line4_rect = self.line4_surf.get_rect(topleft=UI_INFO_POS[3])

        self.line5_surf = self.font.render(UI_INFO[4], False, TEXT_COLOR)
        self.line5_rect = self.line5_surf.get_rect(topleft=UI_INFO_POS[4])

        self.line6_surf = self.font.render(UI_INFO[5], False, TEXT_COLOR)
        self.line6_rect = self.line6_surf.get_rect(topleft=UI_INFO_POS[5])

        self.line7_surf = self.font.render(UI_INFO[6], False, TEXT_COLOR)
        self.line7_rect = self.line7_surf.get_rect(topleft=UI_INFO_POS[6])

        self.line8_surf = self.font.render(UI_INFO[7], False, TEXT_COLOR)
        self.line8_rect = self.line8_surf.get_rect(topleft=UI_INFO_POS[7])
