import pygame
def image_cut(sheet, frame_x, frame_y, width, height, scale):# sheet je obrazek, frame_x je pozice na x, frame_y je pozice na y, width je šířka obrázku, height je výška a scale je kolikrát ho pak chcem zvětšit. př:man_brownhair_run.png, 1, 2, 16,16, 1
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0,0), ((frame_x* width), (frame_y*height), width, height))#pokud chcem první obrázek tak to je 0,0 - protože 0*16 a 0*16 tak to začne řezat z pozice 0 a 0 a 16 px po x a po y. kdybych chtěl obrázek 3. řádek 2. sloupec tak frame_x chcem 1(začnem řezat od 16.px) a frame_y 2(32px)
    img = pygame.transform.scale(img, (width*scale, height*scale))#Scale obrázku danou hodnotou
    img.set_colorkey((0,0,0))#udělání průhlednosti, přepsat 255 na 0

    return img
 