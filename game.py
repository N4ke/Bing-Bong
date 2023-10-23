import pygame
import random

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
clock = pygame.time.Clock()


#funcs
def standart_left_platform():
    global left_platform_width
    global left_platform_heigth
    global left_platform_position
    global speed_of_left_platform
    global score_of_player_1
    
    left_platform_heigth = 150
    if score_of_player_1 > 6:
        left_platform_heigth /= 1.5
    
    speed_of_left_platform = 6.5
    left_platform_position = pygame.rect.Rect(left_platform_width * 5,
                                          window_heigth // 2 - left_platform_heigth // 2 + 70,
                                          left_platform_width,
                                          left_platform_heigth)

def standart_right_platform():
    global right_platform_width
    global right_platform_heigth
    global right_platform_position
    global speed_of_right_platform
    global score_of_player_2
    
    right_platform_heigth = 150
    if score_of_player_2 > 6:
        right_platform_heigth /= 1.5
    
    speed_of_right_platform = 6.5
    right_platform_position = pygame.rect.Rect(window_width - right_platform_width * 6,
                                          window_heigth // 2 - right_platform_heigth // 2 + 70,
                                          right_platform_width,
                                          right_platform_heigth)
   

#colors
color_of_background = (205, 127, 50)
color_for_platforms = (69, 22, 28)
color_of_ball = (150, 0, 24)
color_of_top_menu = (121, 85, 61)
color_of_score_font = (255, 215, 0)
white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 255, 0)
red_color = (255, 43, 43)


#fonts
britannic_bold_font_path = pygame.font.match_font('britannic bold')
arial_font_path = pygame.font.match_font('arial')
britannic_bold_font_100 = pygame.font.Font(britannic_bold_font_path, 100)
arial_font_200 = pygame.font.Font(arial_font_path, 200)
verdana_pro_semibold_path = pygame.font.match_font('verdana pro semibold')
verdana_pro_semibold_40 = pygame.font.Font(verdana_pro_semibold_path, 40)


#screen
def images_on_screen():
    
    score_1 = britannic_bold_font_100.render(str(score_of_player_1 // 10) + str(score_of_player_1 % 10), True, color_of_score_font)
    score_2 = britannic_bold_font_100.render(str(score_of_player_2 // 10) + str(score_of_player_2 % 10), True, color_of_score_font)
    
    window.blit(background, [0, 0])
    window.blit(score_1, [window_width // 2 - 320, top_menu_height + 20])
    window.blit(score_2, [window_width // 2 + 250, top_menu_height + 20])
    
    pygame.draw.circle(window, color_of_ball, ball_position.center, ball_radius)
    pygame.draw.rect(window, color_for_platforms, left_platform_position)
    pygame.draw.rect(window, color_for_platforms, right_platform_position)


background = pygame.image.load('C:/Users/justt/OneDrive/Рабочий стол/Peng Pong/background.png')
top_menu_height = 80

#platforms
speed_of_left_platform = 6.5
speed_of_right_platform = 6.5

left_platform_width = 20
left_platform_heigth = 150

right_platform_width = 20
right_platform_heigth = 150

left_platform_position = pygame.rect.Rect(left_platform_width * 5,
                                          window_heigth // 2 - left_platform_heigth // 2 + 70,
                                          left_platform_width,
                                          left_platform_heigth)

right_platform_position = pygame.rect.Rect(window_width - right_platform_width * 6,
                                          window_heigth // 2 - right_platform_heigth // 2 + 70,
                                          left_platform_width,
                                          left_platform_heigth)


#ball
ball_radius = 12
ball_speed = 5
ball_x_speed = ball_speed
ball_y_speed = 0
ball_position = pygame.rect.Rect(window_width // 2 - 12,
                                 window_heigth // 2 + 22,
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


#game
game_is_running = True
lose = True
while game_is_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
            break
    
    images_on_screen()

    #match
    if not lose:
        
        keys = pygame.key.get_pressed()
        
        current_time = pygame.time.get_ticks()
        
        
        #timer
        if current_time - timer_before_match <= 1000:
            number_3 = britannic_bold_font_100.render('3', True, color_of_score_font)
            window.blit(number_3, (window_width / 2 - 20, window_heigth / 2 - 100))
        
        elif 1000 < current_time - timer_before_match <= 2000:
            number_2 = britannic_bold_font_100.render('2', True, color_of_score_font)
            window.blit(number_2, (window_width / 2 - 20, window_heigth / 2 - 100))
            
        elif 2000 < current_time - timer_before_match <= 3000:
            number_1 = britannic_bold_font_100.render('1', True, color_of_score_font)
            window.blit(number_1, (window_width / 2 - 20, window_heigth / 2 - 100))
        
        elif current_time - timer_before_match > 3000:  
            ball_position.x += ball_x_speed
            ball_position.y += ball_y_speed
        
        
        #мяч в следующем матче летит в сторону проигравшего
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
            
        
        #collision with platforms
        if left_platform_position.colliderect(ball_position):
            ball_x_speed = ball_speed
            ball_speed += 1
        elif right_platform_position.colliderect(ball_position):
            ball_x_speed = -ball_speed
            ball_speed += 1
            
            
        #reflect from top and bottom
        if ball_position.bottom >= window_heigth:
            ball_y_speed = -ball_speed
        elif ball_position.top <= top_menu_height:
            ball_y_speed = ball_speed
        
        
        #control
        if keys[pygame.K_s] and left_platform_position.y <= window_heigth - left_platform_heigth:
            left_platform_position.y += speed_of_left_platform
        elif keys[pygame.K_w] and left_platform_position.y >= top_menu_height:
            left_platform_position.y -= speed_of_left_platform
        
        if keys[pygame.K_DOWN] and right_platform_position.y <= window_heigth - right_platform_heigth:
            right_platform_position.y += speed_of_right_platform
        elif keys[pygame.K_UP] and right_platform_position.y >= top_menu_height:
            right_platform_position.y -= speed_of_right_platform
        
        
        #lose
        if ball_position.left >= window_width - right_platform_width * 6:
            score_of_player_1 += 1
            last_winner = 'player1'
            lose = True
            ball_speed = 5
            timer_before_match = None
        elif ball_position.right <= left_platform_width * 5:
            score_of_player_2 += 1
            last_winner = 'player2'
            lose = True
            ball_speed = 5
            timer_before_match = None
               
    
    #pause after match
    else:
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            if count_click_of_ready_p1 % 2 == 0:
                pygame.time.delay(250)
                player_1_ready = 'ready'
            else:
                pygame.time.delay(250)
                player_1_ready = 'not ready'
            count_click_of_ready_p1 += 1
        
        if keys[pygame.K_l]:
            if count_click_of_ready_p2 % 2 == 0:
                pygame.time.delay(250)
                player_2_ready = 'ready'
            else:
                pygame.time.delay(250)
                player_2_ready = 'not ready'
            count_click_of_ready_p2 += 1
        
            
        if player_1_ready == 'ready' and player_2_ready == 'ready':
            timer_before_match = pygame.time.get_ticks()
            
            lose = False
            
            player_1_ready = 'not ready'
            player_2_ready = 'not ready'
            count_click_of_ready_p1 = 0
            count_click_of_ready_p2 = 0
            
            ball_position.center = [window_width / 2, window_heigth / 2 + 35]
            left_platform_position.centery = window_heigth // 2 + 70
            right_platform_position.centery = window_heigth // 2 + 70
            
            standart_left_platform()
            standart_right_platform()
            
            
            ball_speed = 5
            ball_x_speed = ball_speed
            ball_y_speed = ball_speed
            
            beginning_of_match = True
            
            pygame.draw.circle(window, color_of_ball, ball_position.center, ball_radius)
            pygame.draw.rect(window, color_for_platforms, left_platform_position)
            pygame.draw.rect(window, color_for_platforms, right_platform_position)
            
              
        if count_click_of_ready_p1 % 2 == 0:
            readillity_p1 = britannic_bold_font_100.render(player_1_ready, True, red_color)    
        else:
            readillity_p1 = britannic_bold_font_100.render(player_1_ready, True, green_color)
        
        if count_click_of_ready_p2 % 2 == 0:
            readillity_p2 = britannic_bold_font_100.render(player_2_ready, True, red_color)
        else:
            readillity_p2 = britannic_bold_font_100.render(player_2_ready, True, green_color)
        
        window.blit(readillity_p1, [window_width // 2 - 460, 600])
        window.blit(readillity_p2, [window_width // 2 + 150, 600])
    
    clock.tick(fps)
    
    pygame.display.flip()
    

pygame.quit()