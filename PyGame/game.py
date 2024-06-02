
import pygame, sys
from scores import Scores
from button import ImageButton
from player import Player
from config import *
from level import Level
from resources import Resources
from other import *
# Инициализация pygame
pygame.init()

# Параметры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" game ")


pygame.mouse.set_visible(False) # Скрываем указатель мыши
clock = pygame.time.Clock() # Создаем экземпляр объекта для отслеживания времени
                   
main_background = pygame.image.load("background.png") # Загружаем изображение для главного фона
texture_symbols = {} # Создаем словарь для хранения текстурных символов
cursor = pygame.image.load(RES_DIR +"cursor.png") # Загружаем изображение для курсора
text_surface = pygame.image.load("surface.png") # Загружаем изображение для плаща поверхности
run_sound = pygame.mixer.Sound(AUD_DIR + "run.mp3") # Загружаем звуковой эффект для звука бега
pygame.mixer.music.load(AUD_DIR + "background.mp3") # Загружаем фоновую музыку

# Создание кнопок в меню
def main_menu():
    # Создаем кнопки
    begin_button = ImageButton(WIDTH/2-(252/2), 250, 252, 55, "", "begin_button.png", "begin_button_hover.png", "click.mp3" )

    setting_button = ImageButton(WIDTH/2-(252/2), 350, 252, 55, "", "setting_button.png", "setting_button_hover.png", "click.mp3" )

    exit_button = ImageButton(WIDTH/2-(252/2), 450, 252, 55, "", "exit_button.png", "exit_button_hover.png", "click.mp3" )
  
    running = True
    
    while running:
        
        screen.fill((0, 0, 0)) # Заполняем экран черным цветом
        screen.blit(text_surface,(280, 20)) # Отображаем текст
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Если пользователь закрывает окно
                running = False # Останавливаем цикл
                pygame.quit() # Выходим из игры
                sys.exit() # Завершаем программу
            
            if event.type == pygame.USEREVENT and event.button == begin_button:
                print("Game! start")
                fade() # Проигрываем анимацию затухания
                new_game() # Запускаем новую игру
                

            if event.type == pygame.USEREVENT and event.button == setting_button:
                print("Settings! start")
                fade()
                setting_menu() # Запускаем меню настроек
                
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()
            
            for btn in[begin_button, setting_button, exit_button]:
                btn.handle_event(event)
                
        for btn in [begin_button, setting_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos()) # Проверяем, находится ли курсор над кнопкой
            btn.draw(screen) # Отображаем кнопки
         
        x, y = pygame.mouse.get_pos() # Отображение курсора в текущей позиции мыши
        screen.blit(cursor, (x-2, y-2))   
        pygame.display.flip()   
        
def setting_menu():
    # Создаем кнопки
    audio_button = ImageButton(WIDTH/2-(252/2), 150, 252, 55, "", "audio_button.png", "audio_button_hover.png", "click.mp3" )

    video_button = ImageButton(WIDTH/2-(252/2), 250, 252, 55, "", "video_button.png", "video_button_hover.png", "click.mp3" )

    back_button = ImageButton(WIDTH/2-(252/2), 350, 252, 55, "", "back_button.png", "back_button_hover.png", "click.mp3" )
    
    running = True
    while running:
        screen.fill((0, 0, 0))

        
        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255)) # Отображение текста "settings" в центре экрана
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button: # Возврат в меню при нажатии кнопки back_button
                fade()
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))
        
        pygame.display.flip()
    
def new_game():
    rsc = Resources()
    main_font = pygame.font.SysFont("robo", 30)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))        
    clock = pygame.time.Clock()
    player = Player(screen, rsc.player_image_r, rsc.player_image_l, run_sound, main_font )
    block_image = pygame.transform.scale(pygame.image.load("stone.png"), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.mixer.music.play(-1)
    scores = Scores(screen) # Создание объекта для отображения счёта
    
    # Установка начальных координат камеры
    scroll_x = 0
    scroll_y = 0
    
    UI_textures = {"card": pygame.transform.scale(pygame.image.load(RES_DIR + "card.png"), (50, 50))}
    message_manager = Message(main_font, [WIDTH//2, HEIGHT - 100], screen)   # Создание объекта для отображения сообщений
    
    # Создание уровня игры
    level = Level(screen, rsc.texture_symbols, [100, -400])
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(rsc.bg_image[0], (-scroll_x, 0))
        screen.blit(rsc.bg_image[0], (WIDTH-scroll_x, 0))
        delta_time = clock.tick(MAX_FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()  
               
       
        # Слежение за игроком при движении камеры
        if player.rect.x - scroll_x != 0:
            scroll_x += (player.rect.x - scroll_x - (WIDTH/2 - PLAYER_SIZE[0]/2))/10
        if player.rect.y - scroll_y != 0:
            scroll_y += (player.rect.y - scroll_y - (HEIGHT/2 - PLAYER_SIZE[1]/2))/10
        # Обновление данных и отображение игрока
        player_data: dict = player.update(delta_time, level.update(scroll=[scroll_x, scroll_y]), (scroll_x, scroll_y))
        player.draw()
        scores.show_health(player)
         # Отображение карт и счёта
        screen.blit(UI_textures["card"], (20, HEIGHT - 500))
        screen.blit(main_font.render(str(int(player.collected_card)), True, (255,255,255)), (100, HEIGHT-480))
        # Обновление и отображение сообщений
        message_manager.update(delta_time)
        if "message" in player_data:
            message_manager.show_message(player_data["message"][0], player_data["message"][1])
        pygame.display.update() # Обновление экрана
        
    
def fade():
    running = True  # переменная для контроля работы анимации
    fade_alpha = 0  # уровень прозрачности для анимации

    while running:
        for event in pygame.event.get():  # обработка событий
            if event.type == pygame.quit:  # если событие - выход из игры
                running = False  # останавливаем анимацию

        fade_surface = pygame.Surface((WIDTH, HEIGHT))  # создание поверхности для затемнения экрана
        fade_surface.fill((0, 0, 0))  # заполнение поверхности черным цветом
        fade_surface.set_alpha(fade_alpha)  # установка уровня прозрачности для поверхности
        screen.blit(fade_surface, (0, 0))  # отрисовка поверхности на экране

        fade_alpha += 5  # увеличиваем уровень прозрачности на 5
        if fade_alpha >= 105:  # если достигнуто максимальное значение прозрачности
            fade_alpha = 255  # устанавливаем максимальное значение прозрачности
            running = False  # останавливаем анимацию

        pygame.display.flip()  # обновление экрана
        clock.tick(MAX_FPS)  # ограничение fps

if __name__ == "__main__":
    main_menu()
