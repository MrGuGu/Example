import pygame.font
from ship import Ship
from pygame.sprite import Group
class ScoreBoard():

    def __init__(self, ai_settings, screen, gameState):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.gameState = gameState

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        self.ships  = Group()
        for ship_number in range(self.gameState.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.gameState.level), True,
                  self.text_color, self.ai_settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()         
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.gameState.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
              self.text_color, self.ai_settings.bg_color)
          # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        rounded_score = int(round(self.gameState.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

