
from config import *
import pygame

class Resources:
    def __init__(self):    
   
        self.textures = {"block": pygame.transform.scale(pygame.image.load("stone.png"), (BLOCK_SIZE, BLOCK_SIZE)),
                   "first_aid": pygame.transform.scale(pygame.image.load(RES_DIR + "first_aid.png"), (BLOCK_SIZE, BLOCK_SIZE)),
                   "card": pygame.transform.scale(pygame.image.load(RES_DIR + "card.png"), (BLOCK_SIZE, BLOCK_SIZE)),
                   "door": [pygame.transform.scale(pygame.image.load(RES_DIR + "door.png"), (BLOCK_SIZE, BLOCK_SIZE*2)),
                            pygame.transform.scale(pygame.image.load(RES_DIR + "door_closed.png"), (BLOCK_SIZE, BLOCK_SIZE*2))]}
        

        self.player_image_r = [pygame.transform.scale(pygame.image.load(RES_DIR + "hero/main.png"), PLAYER_SIZE),
                         pygame.transform.scale(pygame.image.load(RES_DIR + "hero/0.png"), PLAYER_SIZE),
                         pygame.transform.scale(pygame.image.load(RES_DIR + "hero/1.png"), PLAYER_SIZE),
                         pygame.transform.scale(pygame.image.load(RES_DIR + "hero/2.png"), PLAYER_SIZE),
                         pygame.transform.scale(pygame.image.load(RES_DIR + "hero/3.png"), PLAYER_SIZE)]
        

        self.player_image_l = [pygame.transform.flip(self.player_image_r[0], True, False),
                          pygame.transform.flip(self.player_image_r[1], True, False),
                          pygame.transform.flip(self.player_image_r[2], True, False),
                          pygame.transform.flip(self.player_image_r[3], True, False),
                          pygame.transform.flip(self.player_image_r[4], True, False)]
        
        
        self.texture_symbols = {"&": self.textures["block"],
                                "h": self.textures["first_aid"],
                                "k": self.textures["card"],
                                "d": self.textures["door"]}


                 
        self.bg_image = [pygame.transform.scale(pygame.image.load("bg.png"), RES)]


    
