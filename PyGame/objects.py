from ast import Import
from os import close
from config import *
import pygame
from resources import Resources

class Block:
    def __init__(self, pos, texture, screen, collider, name):
        self.pos = pos
        self.texture = texture
        self.screen = screen
        self.collider = collider
        self.rect = pygame.Rect(0, 0, 0, 0) # прямоугольник, определяющий размеры и положение блока
        self.name = name
        
    def draw(self, scroll):
        self.rect = pygame.Rect = self.texture.get_rect() # определение размеров прямоугольника блока
        self.rect.topleft = self.pos # установка позиции прямоугольника блока
        self.screen.blit(self.texture, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))# отрисовка текстуры блока на экране с учетом прокрутки
        return self

class Removable:
    def __init__(self, pos, texture, screen, collider, name):
        self.pos = pos
        self.texture = texture
        self.screen = screen
        self.collider = True
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.removed = False
        self.name = name
        
        
    def draw(self, scroll):
        
        if not self.removed:
            self.rect = pygame.Rect = self.texture.get_rect()
            self.rect.topleft = self.pos
            self.screen.blit(self.texture, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        return self
     
    def remove(self):
        self.removed = True
        
class Door:
    def __init__(self, pos, texture, screen, collider, name):
        self.pos = pos
        self.texture_opened = texture[0]
        self.texture_closed = texture[1]
        self.screen = screen
        self.collider = True
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.opened = False
        self.name = name
        self.timer = 0
        self.used = False
        
    def draw(self, scroll):
        if not self.opened:
            self.rect = self.texture_closed.get_rect() # определение размеров прямоугольника двери
            self.rect.width = self.rect.width/5 # изменение ширины прямоугольника двери (для отображения закрытого состояния)
            self.rect.topleft = self.pos
            self.screen.blit(self.texture_closed, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        else:
            self.rect = self.texture_opened.get_rect()
            
            self.rect.topleft = self.pos
            self.screen.blit(self.texture_opened, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        return self
    
    def open(self):
        self.opened = True
        
    def close(self):
        self.opened = False


