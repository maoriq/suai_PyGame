import pygame
from config import *
class Scores():
    def __init__(self, screen):
        self.image_hp = pygame.transform.scale(pygame.image.load(RES_DIR + "hp.png"), (50, 50))
        self.image_card = pygame.transform.scale(pygame.image.load(RES_DIR + "card.png"), (50, 50))
        self.screen = screen
        self.amount_card = 0
        

    def show_health(self, player):
        x = 10
        for hp in range(player.hp):
            self.screen.blit(self.image_hp, (x, 20))
            x += 50
            
    def show_card(self, player):
        x = 10
        for card in range(player.card):
            self.screen.blit(self.image_card, (x, 20))
            x += 50