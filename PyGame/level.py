from tkinter import SE
import pygame
from config import *
from objects import *

class Level:
    def __init__(self, screen, textures, level_offset):
        self.screen = screen
        self.level = []
        with open("level", "r") as file:
            for line in file.readlines():
                line = line.replace("\n", "")
                self.level.append(line)
        
        self.ignored_collision = ["."]
        self.types = {"&": Block,
                      "h": Removable,
                      "k": Removable,
                      "d": Door,}
        self.textures = textures
        self.level_offset = level_offset
        self.level_blocks = []
        self.start()
        
    def start(self):
        # Начинает создание уровня на основе данных, считанных из файла
        for i, y in enumerate(self.level):
            for j, x in enumerate(y):
                if x != ".":
                    if x not in self.ignored_collision:
                        pos = [j*BLOCK_SIZE-self.level_offset[0], i*BLOCK_SIZE-self.level_offset[1]]
                        self.level_blocks.append(self.types[x](pos, self.textures[x], self.screen, True, x))

    def update(self, scroll):
        # Обновляет уровень и возвращает объекты, которые нужно отобразить на экране
        objects = []
        for i, y in enumerate(self.level_blocks):
            res = y.draw(scroll)
            objects.append(res)      
        return objects     
    

