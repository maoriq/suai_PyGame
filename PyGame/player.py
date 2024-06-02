import pygame
from other import *
from config import GRAVITY
from objects import *
class Player:
    def __init__(self, screen, player_image_r, player_image_l, run_sound, font):
        self.run_s = run_sound
        
        self.dir = "left"
        self.pos = [400, 250]
        self.screen = screen
        self.image_r = player_image_r
        self.image_l = player_image_l
        self.movement = [0, 0]
        self.rect = self.image_l[0].get_rect()
        self.rect.topleft = [50, 3150]
        self.old_dir = [0, 0]
        self.anim_count = 0
        self.is_run = False
        self.delta_time = 0
        self.scroll_x = 0
        self.scroll_y = 0

        # физика
        self.air_time = 0
        self.is_ground = False
        # other
        self.hp = 3
        self.collected_card = 0
        self.font = font
        self.return_to_main_data = {}

    def draw(self):
        self.anim_count %= 500

        if self.is_run:
            if self.movement[0] > 0:
                self.screen.blit(self.image_r[int(self.anim_count * 0.002 * 5)],
                                (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
            if self.movement[0] < 0:
                self.screen.blit(self.image_l[int(self.anim_count * 0.002 * 5)],
                                (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
        else:
            if self.old_dir[0] > 0:
                self.screen.blit(self.image_r[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
            elif self.old_dir[0] < 0:
                self.screen.blit(self.image_l[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))  
        
    def update(self, delta_time, blocks, scroll):
        self.return_to_main_data = {}
        self.scroll_x = scroll[0]
        self.scroll_y = scroll[1]
        self.delta_time = delta_time
        if self.hp > 0:
            self.change_dir()
        self.anim_count += delta_time
        
        self.physics(blocks)
        if self.is_run and self.is_ground:
            self.run_s.play(-1)
        return self.return_to_main_data

    def change_dir(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.movement[0] = -0.5    
        elif keys[pygame.K_d]:

            self.movement[0] = 0.5
        else:
            if self.movement[0] != 0:
                self.old_dir[0] = self.movement[0]
            if self.is_run:
                self.run_s.stop()
            self.is_run = False
            self.movement[0] = 0
        if self.movement[0] != 0:
            if not self.is_run and round(self.air_time, 1) == 0:
                self.run_s.play(-1)
            self.is_run = True
            
    def get_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.hp > 0:
            return True
        return False
    
    def physics(self, blocks):
        self.air_time += -self.delta_time * 0.001
        self.movement[1] = GRAVITY * self.air_time
        self.rect.x += self.movement[0] * self.delta_time
        collide = self.get_collision(blocks)
        for col in collide:
            if self.movement[0] > 0:
                self.rect.right = col.left
            elif self.movement[0] < 0:
                self.rect.left = col.right
                
        self.rect.y += self.movement[1] * self.delta_time
        collide = self.get_collision(blocks)
        for col in collide:
            if self.movement[1] > 0:
                self.rect.bottom = col.top
                self.is_ground = True
            elif self.movement[1] < 0:
                self.rect.top = col.bottom
        if self.is_ground:
            self.air_time = 0
            if self.get_jump():
                self.air_time = 0.2
        self.is_ground = False
                     
    def get_collision(self, blocks):   
        collide = []
        for col in blocks:
            if col.collider:
                if self.rect.colliderect(col.rect):
                    if isinstance(col, Removable):
                        if not col.removed:
                            if col.name == "h":
                                self.hp += 1
                            elif col.name == "k":
                                self.collected_card += 1
                            col.remove()
                    elif isinstance(col, Door):
                        if not col.opened:
                            if self.collected_card >= 1 and not col.used:
                                self.collected_card -= 1
                                col.used = True
                                col.open()
                            else:
                                if col.used:
                                    self.return_to_main_data = {"message":[5, "You Win!"]}
                                else:   
                                    self.return_to_main_data = {"message": [2, "Collect all the cards to open this door"]}                               
                                collide.append(col.rect)
                        elif self.rect.left+9 > col.rect.right:
                            col.close()         
                    else:
                        collide.append(col.rect)
        return collide
