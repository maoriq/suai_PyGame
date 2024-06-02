
class Message:
    def __init__(self, font, pos, screen):
        self.pos = pos
        self.font = font
        self.timer = 0
        self.message = ""
        self.duration = 0
        self.screen = screen

        
    def update(self, delta_time):
        if self.message:
            self.timer += delta_time * 0.001
            if self.timer > self.duration:
                self.message = ""
            msg = self.font.render(self.message, True, (255, 255, 255))
            rect = msg.get_rect()
            rect.center = self.pos
            self.screen.blit(msg, rect)
        
        
    def show_message(self, duration, text):
        self.message = text
        self.timer = 0
        self.duration = duration
    
