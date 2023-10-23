import pygame
import random
import time

pygame.init()
pygame.font.init()


#name
name = 'Bing Bong'
pygame.display.set_caption(name)


#window
window_width = 1280
window_heigth = 720
window = pygame.display.set_mode([window_width, window_heigth])
fps = 60
timer = pygame.time.Clock()


#colors
color_of_background = (205, 127, 50)
color_for_platforms = (69, 22, 28)
color_of_ball = (150, 0, 24)
color_of_top_menu = (121, 85, 61)
color_of_score_font = (255, 215, 0)
white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (52, 201, 36)


#fonts
britannic_bold_font_path = pygame.font.match_font('britannic bold')
arial_font_path = pygame.font.match_font('arial')
britannic_bold_font_100 = pygame.font.Font(britannic_bold_font_path, 100)
arial_font_200 = pygame.font.Font(arial_font_path, 200)
verdana_pro_semibold_path = pygame.font.match_font('verdana pro semibold')
verdana_pro_semibold_40 = pygame.font.Font(verdana_pro_semibold_path, 40)


#screen
def images_on_screen():
    window.fill(color_of_background)
    pygame.draw.rect(window, color_of_top_menu, top_menu_position)
    
    score_1 = britannic_bold_font_100.render(str(score_of_player_1), True, color_of_score_font)
    score_2 = britannic_bold_font_100.render(str(score_of_player_2), True, color_of_score_font)
    
    window.blit(score_1, [window_width // 2 - 340, top_menu_position.bottom + 20])
    window.blit(score_2, [window_width // 2 + 320, top_menu_position.bottom + 20])
    window.blit(top_menu_surface, [0, 0])
    

top_menu_height = 150
top_menu_position = pygame.rect.Rect(window_width // 2 - window_width // 2,
                                     window_heigth // 2 - window_heigth // 2,
                                     window_width,
                                     top_menu_height)


#menu
class Menu:
    def __init__(self):
        self._options = []
        self._callbacks = []
        self._option_index = 0
        
    _current_option_index = 0
    
    def append_option(self, option, callback):
        self._options.append(verdana_pro_semibold_40.render(option, True, black_color))
        self._callbacks.append(callback)
        
    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._options) - 1))
        
    def select(self):
        self._callbacks[self._current_option_index]()
        
    def draw(self, surf, x, y, option_y_padding, option_x_padding):
        for index, option in enumerate(self._options):
            option_position = option.get_rect()
            option_position.topleft = (x + index * option_x_padding, y + index * option_y_padding)
            if index == self._current_option_index:
                pygame.draw.rect(window, green_color, option_position)
            window.blit(option, option_position)

top_menu_surface = pygame.image.load('C:/Users/justt/OneDrive/Рабочий стол/top_menu.jpg')


#platforms
speed_of_left_platform = 6.5
speed_of_right_platform = 6.5

left_platform_width = 20
left_platform_heigth = 180

right_platform_width = 20
right_platform_heigth = 180

left_platform_position = pygame.rect.Rect(left_platform_width * 5,
                                          window_heigth // 2 - left_platform_heigth // 2 + 70,
                                          left_platform_width,
                                          left_platform_heigth)

right_platform_position = pygame.rect.Rect(window_width - right_platform_width * 6,
                                          window_heigth // 2 - right_platform_heigth // 2 + 70,
                                          left_platform_width,
                                          left_platform_heigth)


#ball
ball_radius = 15
ball_speed = 7
ball_x_speed = ball_speed
ball_y_speed = 0
ball_position = pygame.rect.Rect(window_width // 2,
                                 window_heigth // 2,
                                 ball_radius * 2,
                                 ball_radius * 2)


#matches
num_of_matches = 0
beginning_of_match = True

score_of_player_1 = 0
score_of_player_2 = 0

last_winner = ''

player_1_ready = 'not ready'
count_click_of_ready_p1 = 0
player_2_ready = 'not ready'
count_click_of_ready_p2 = 0


#game_mods
def l_green_1():
    global ball_speed
    ball_speed *= 1.5
    
def l_green_2():
    global left_platform_heigth
    left_platform_heigth *= 1.5
    
    
player1_menu = Menu()
player1_menu.append_option('1', l_green_1())
player1_menu.append_option('2', l_green_2())


#game
t = time.time()
game_is_running = True
lose = False
first_run = True
while game_is_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
            break
    
    
    images_on_screen()


    #collision, speed and control keys
    if not lose:
        
        keys = pygame.key.get_pressed()
        
            
        ball_position.x += ball_x_speed
        ball_position.y += ball_y_speed
        
        
        if beginning_of_match:
            if last_winner == 'player1':
                ball_x_speed = ball_speed
            elif last_winner == 'player2':
                ball_x_speed = -ball_speed
            
            if random.randint(0, 1) == 0:
                ball_y_speed = ball_speed
            else:
                ball_y_speed = -ball_speed
            
            beginning_of_match = False
            
        
        if left_platform_position.colliderect(ball_position):
            ball_x_speed = ball_speed
        elif right_platform_position.colliderect(ball_position):
            ball_x_speed = -ball_speed
        
        
        if keys[pygame.K_s] and left_platform_position.y <= window_heigth - left_platform_heigth:
            left_platform_position.y += speed_of_left_platform
        elif keys[pygame.K_w] and left_platform_position.y >= top_menu_height:
            left_platform_position.y -= speed_of_left_platform
        
        if keys[pygame.K_DOWN] and right_platform_position.y <= window_heigth - right_platform_heigth:
            right_platform_position.y += speed_of_right_platform
        elif keys[pygame.K_UP] and right_platform_position.y >= top_menu_height:
            right_platform_position.y -= speed_of_right_platform
        
        
        if ball_position.left <= 0:
            ball_x_speed = ball_speed
        elif ball_position.right >= window_width:
            ball_x_speed = -ball_speed
        elif ball_position.bottom >= window_heigth:
            ball_y_speed = -ball_speed
        elif ball_position.top <= top_menu_height:
            ball_y_speed = ball_speed
            
    
    #lose situation 
    if not lose:
        
        if ball_position.left >= window_width - right_platform_width * 6:
            score_of_player_1 += 1
            last_winner = 'player1'
            lose = True
        elif ball_position.right <= left_platform_width * 5:
            score_of_player_2 += 1
            last_winner = 'player2'
            lose = True
        
        
        pygame.draw.circle(window, color_of_ball, ball_position.center, ball_radius)
        pygame.draw.rect(window, color_for_platforms, left_platform_position)
        pygame.draw.rect(window, color_for_platforms, right_platform_position)    
    
    
    #pause after match
    else:
        
        keys = pygame.key.get_pressed()
        
        player1_menu.draw(window, 35, 25, 25, 0)
        
        if keys[pygame.K_r]:
            if count_click_of_ready_p1 % 2 == 0:
                pygame.time.delay(300)
                player_1_ready = 'ready'
            else:
                pygame.time.delay(300)
                player_1_ready = 'not ready'
            count_click_of_ready_p1 += 1
        
        if keys[pygame.K_l]:
            if count_click_of_ready_p2 % 2 == 0:
                pygame.time.delay(300)
                player_2_ready = 'ready'
            else:
                pygame.time.delay(300)
                player_2_ready = 'not ready'
            count_click_of_ready_p2 += 1
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_menu.switch(1)
                elif event.key == pygame.K_s:
                    player1_menu.switch(-1)
                elif event.key == pygame.K_x:
                    player1_menu.select()
           
            
        if player_1_ready == 'ready' and player_2_ready == 'ready':
            lose = False
            
            player_1_ready = 'not ready'
            player_2_ready = 'not ready'
            count_click_of_ready_p1 = 0
            count_click_of_ready_p2 = 0
            
            ball_position.center = [window_width // 2, window_heigth // 2]
            left_platform_position.centery = window_heigth // 2 + 70
            right_platform_position.centery = window_heigth // 2 + 70
            
            left_platform_heigth = 180
            right_platform_heigth = 180
            
            ball_speed = 7
            
            first_run = True
            
            
            pygame.draw.circle(window, color_of_ball, ball_position.center, ball_radius)
            pygame.draw.rect(window, color_for_platforms, left_platform_position)
            pygame.draw.rect(window, color_for_platforms, right_platform_position) 
              
        readillity_p1 = britannic_bold_font_100.render(player_1_ready, True, color_of_score_font)
        readillity_p2 = britannic_bold_font_100.render(player_2_ready, True, color_of_score_font)
        
        window.blit(readillity_p1, [window_width // 2 - 460, 450])
        window.blit(readillity_p2, [window_width // 2 + 200, 450])
    
    timer.tick(fps)
    
    pygame.display.flip()
    

pygame.quit()