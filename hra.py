#import pygamu
import pygame
from sys import exit



# pygame setup
pygame.init()

def monster_animation():
    global monster_surf, monster_index #import surfu indexu ktery meni animaci v listu images
    monster_index +=0.1 #0,1 pro nižší rychlost
    if monster_index > len(monster_images):#aby to neslo do nekonecna
        monster_index = 0
    monster_surf = monster_images[int(monster_index)]#vykreslení




#CAPS značí konstanty - proměnné co by se neměly měnit
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#rozlišení
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#vytvoří hodiny
clock = pygame.time.Clock()


running = True

player = pygame.Rect((50,100,50,50))#pozice x, y, velikost x, y, || ty hodnoty v (()) tak jsou tupple - rychlejší než list
player_speed = 5

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

player_HP = 100
nesmrtelnost = False
čas_nesmrtelnosti = 0

elapsed_time = 0 #počáteční hodnota časomíry


#herní smyčka
while running:
    # kontrola eventů - aby to kdyžtak vyplo hru
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()


    #proměnná key kde je co uživatel stiskl
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0,-player_speed)
    if key[pygame.K_s]:
        player.move_ip(0,player_speed)
    if key[pygame.K_a]:
        player.move_ip(-player_speed, 0)
    if key[pygame.K_d]:
        player.move_ip(player_speed,0)
    #obarví obrazovku
    screen.fill("purple")
    monster_animation()
    monster_rect.right += monster_speed
    if monster_rect.right >= SCREEN_WIDTH:
        monster_speed *= -1
    elif monster_rect.left <= 0:
        monster_speed *=-1
    
    

    screen.blit(monster_surf, monster_rect)
    pygame.draw.rect(screen, (255,0,0), player)


    elapsed_time += clock.get_time()
    if nesmrtelnost == True and elapsed_time >= čas_nesmrtelnosti+2000:
        nesmrtelnost = False
        print(f"Může zkapat")
        

    if player.colliderect(monster_rect) and nesmrtelnost == False:
        player_HP -=1
        print(f"Hráč má {player_HP}")
        nesmrtelnost = True
        čas_nesmrtelnosti = elapsed_time
        
    
    
    #vše updatuje
    pygame.display.update()
    #pygame.display.flip() - prý horší - idk proč

    clock.tick(60)  # limits FPS to 60
