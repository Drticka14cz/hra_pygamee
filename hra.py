#import pygamu
import pygame
from sys import exit
from settings import *
from utility import *
from player import *

# pygame setup
pygame.init()


#ořezávání spritesheetu

# def player_animation(direction):
#     global player_img, player_index
#     player_index +=0.1
#     frame_count = 3
#     if player_index > frame_count:#aby to neslo do nekonecna
#         player_index = 0
#     player_img = image_cut(player_spritesheet,int(player_index),direction, 15,16,5)



def reset_game():
    global game_stat
    player.sprite.lives = 3
    player.sprite.rect.topleft = (50,100)
    game_stat = "Playing"

def monster_animation():
    global monster_surf, monster_index #import surfu indexu ktery meni animaci v listu images
    monster_index +=0.1 #0,1 pro nižší rychlost
    if monster_index > len(monster_images):#aby to neslo do nekonecna
        monster_index = 0
    monster_surf = monster_images[int(monster_index)]#vykreslení




#CAPS značí konstanty - proměnné co by se neměly měnit


#rozlišení
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

#vytvoří hodiny
clock = pygame.time.Clock()


running = True

font = pygame.font.Font("PixelifySans-Regular.ttf", 25)
font_velky = pygame.font.Font("PixelifySans-Regular.ttf", 100)




 

#player = pygame.Rect((50,100,50,50))                    #pozice x, y, velikost x, y, || ty hodnoty v (()) tak jsou tupple - rychlejší než list


monster_idle = pygame.image.load("monsta.png").convert_alpha()
monster_idle = pygame.transform.rotozoom(monster_idle,0,4)
monster_surf_run_1 = pygame.image.load("monsta_run1.png").convert_alpha()
monster_surf_run_1 = pygame.transform.rotozoom(monster_surf_run_1,0,4)
monster_surf_run_2 = pygame.image.load("monsta_run2.png").convert_alpha()
monster_surf_run_2 = pygame.transform.rotozoom(monster_surf_run_2,0,4)
monster_images = [monster_idle, monster_surf_run_1, monster_surf_run_2]
monster_index = 0
monster_surf = monster_images[monster_index]


monster_x = 300 
monster_y = 450
monster_rect = monster_idle.get_rect(midbottom=(monster_x,monster_y))
monster_speed= 1





restart_button_h = 60
restart_button_w = 200
restart_button = pygame.Rect( 0,0,restart_button_w,restart_button_h)
restart_button.center = (screen_rect.centerx, screen_rect.centery + 100)
restart_button_color = "#FF0000"
restart_button_color_hover = "#FF5959D3"
restart_button_text_color = "#FFFFFF"
restart_button_font =pygame.font.Font("PixelifySans-Regular.ttf", 30)
restart_button_text = restart_button_font.render("Restart", False, restart_button_text_color)

player = pygame.sprite.GroupSingle()
player.add(Player())

elapsed_time = 0 #počáteční hodnota časomíry

game_stat = "Playing"

###############################################_________HERNÍ_SMYČKA_________################################################################################################
while running:

    # kontrola eventů - aby to kdyžtak vyplo hru
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if game_stat == "Game_Over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    reset_game()

    #proměnná key kde je co uživatel stiskl
    key = pygame.key.get_pressed()

    if game_stat == "Playing":

       
        #obarví obrazovku
        screen.fill("purple")

        text_lives = font.render(f"Životy: {player.sprite.lives}", False, "#000000")#render
        screen.blit(text_lives, (SCREEN_HEIGHT-100, 10))

        monster_animation()
        monster_rect.right += monster_speed
        if monster_rect.right >= SCREEN_WIDTH:
            monster_speed *= -1
        elif monster_rect.left <= 0:
            monster_speed *=-1
        
        

        screen.blit(monster_surf, monster_rect)
        # pygame.draw.rect(screen, (255,0,0), player)
        player.draw(screen)
        player.update()
      
        

        # elapsed_time += clock.get_time()
        # if player.sprite.nesmrtelnost == True and elapsed_time >= player.sprite.čas_nesmrtelnosti+500:
        #     player.sprite.nesmrtelnost = False
        #     print(f"Může zkapat")
            

        # if player_rect.colliderect(monster_rect) and nesmrtelnost == False:
        #     player_HP -=1
        #     print(f"Hráč má {player_HP}")
        #     nesmrtelnost = True
        #     čas_nesmrtelnosti = elapsed_time
            
        # if player.sprite.lives<= 0:
        #     game_stat = "Game_Over"
            
    elif game_stat == "Game_Over":

        mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")
        go_text = font_velky.render(f"GAME OVER", False, "white")
        go_text_rect = go_text.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 ))
        screen.blit(go_text, go_text_rect)
        
       

        if restart_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, restart_button_color_hover, restart_button, border_radius=15)

        else:
            pygame.draw.rect(screen, restart_button_color, restart_button, border_radius= 15)
        screen.blit(restart_button_text, (restart_button.centerx -restart_button_text.get_width() / 2, restart_button.centery - restart_button_text.get_height() /2))
    #vše updatuje
    pygame.display.update()
    #pygame.display.flip() - prý horší - idk proč

    clock.tick(60)  # limits FPS to 60
