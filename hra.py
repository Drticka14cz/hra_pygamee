#import pygamu
import pygame
from sys import exit



# pygame setup
pygame.init()


#ořezávání spritesheetu
def image_cut(sheet, frame_x, frame_y, width, height, scale):# sheet je obrazek, frame_x je pozice na x, frame_y je pozice na y, width je šířka obrázku, height je výška a scale je kolikrát ho pak chcem zvětšit. př:man_brownhair_run.png, 1, 2, 16,16, 1
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0,0), ((frame_x* width), (frame_y*height), width, height))#pokud chcem první obrázek tak to je 0,0 - protože 0*16 a 0*16 tak to začne řezat z pozice 0 a 0 a 16 px po x a po y. kdybych chtěl obrázek 3. řádek 2. sloupec tak frame_x chcem 1(začnem řezat od 16.px) a frame_y 2(32px)
    img = pygame.transform.scale(img, (width*scale, height*scale))#Scale obrázku danou hodnotou
    img.set_colorkey((0,0,0))#udělání průhlednosti, přepsat 255 na 0

    return img

def player_animation(direction):
    global player_img, player_index
    player_index +=0.1
    frame_count = 3
    if player_index > frame_count:#aby to neslo do nekonecna
        player_index = 0
    player_img = image_cut(player_spritesheet,int(player_index),direction, 15,16,5)

def player_animation_r(direction):
    global player_img, player_index
    player_index +=0.1
    frame_count = 4
    if player_index > frame_count:#aby to neslo do nekonecna
        player_index = 0
    player_img = image_cut(player_spritesheet,direction,int(player_index), 16,16,5)


def reset_game():
    global player_HP, game_stat
    player_HP = 3
    game_stat = "Playing"

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
screen_rect = screen.get_rect()

#vytvoří hodiny
clock = pygame.time.Clock()


running = True

font = pygame.font.Font("PixelifySans-Regular.ttf", 25)
font_velky = pygame.font.Font("PixelifySans-Regular.ttf", 100)

player_x = 100
player_y = 100
player_index = 0

player_spritesheet = pygame.image.load("walk.png").convert_alpha()
player_img = image_cut(player_spritesheet, 0, 0, 16,16, 5)
player_rect = player_img.get_rect(midbottom = (player_x, player_y))
#player = pygame.Rect((50,100,50,50))                    #pozice x, y, velikost x, y, || ty hodnoty v (()) tak jsou tupple - rychlejší než list
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

player_HP = 3
nesmrtelnost = False
čas_nesmrtelnosti = 0


restart_button_h = 60
restart_button_w = 200
restart_button = pygame.Rect( 0,0,restart_button_w,restart_button_h)
restart_button.center = (screen_rect.centerx, screen_rect.centery + 100)
restart_button_color = "#FF0000"
restart_button_color_hover = "#FF5959D3"
restart_button_text_color = "#FFFFFF"
restart_button_font =pygame.font.Font("PixelifySans-Regular.ttf", 30)
restart_button_text = restart_button_font.render("Restart", False, restart_button_text_color)

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

        if key[pygame.K_w]:
            player_animation_r(1)
            player_rect.move_ip(0,-player_speed)
        if key[pygame.K_s]:
            player_animation_r(0)
            player_rect.move_ip(0,player_speed)
        if key[pygame.K_a]:
            player_animation_r(2)
            player_rect.move_ip(-player_speed, 0)
        if key[pygame.K_d]:
            player_animation_r(3)
            player_rect.move_ip(player_speed,0)
        #obarví obrazovku
        screen.fill("purple")

        text_lives = font.render(f"Životy: {player_HP}", False, "#000000")#render
        screen.blit(text_lives, (SCREEN_HEIGHT-100, 10))

        monster_animation()
        monster_rect.right += monster_speed
        if monster_rect.right >= SCREEN_WIDTH:
            monster_speed *= -1
        elif monster_rect.left <= 0:
            monster_speed *=-1
        
        

        screen.blit(monster_surf, monster_rect)
        # pygame.draw.rect(screen, (255,0,0), player)
        screen.blit(player_img,player_rect )
        

        elapsed_time += clock.get_time()
        if nesmrtelnost == True and elapsed_time >= čas_nesmrtelnosti+500:
            nesmrtelnost = False
            print(f"Může zkapat")
            

        if player_rect.colliderect(monster_rect) and nesmrtelnost == False:
            player_HP -=1
            print(f"Hráč má {player_HP}")
            nesmrtelnost = True
            čas_nesmrtelnosti = elapsed_time
            
        if player_HP<= 0:
            game_stat = "Game_Over"
            
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
