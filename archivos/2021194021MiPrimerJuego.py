import pygame
from pygame.locals import*
import random
import sys


winHori=800
winVert=600
fps=60 
white=(255,255,255)
negro=(0,0,0,)
class pelotaP:
    def __init__(self,fichero_imagen):
        self.imagen=pygame.image.load(fichero_imagen).convert_alpha()
        self.ancho,self.alto=self.imagen.get_size()
        self.x=winHori/2-self.ancho/2
        self.y=winVert/2-self.alto/2
        self.dir_x=random.choice([-5,5])
        self.dir_y=random.choice([-5,5])
        self.puntuacion=0 
        self.puntuacion_maqui=0
    def movimiento(self):
        self.x+=self.dir_x
        self.y+=self.dir_y
    def reiniciar(self):
        self.x=winHori/2-self.ancho/2
        self.y=winVert/2-self.alto/2
        self.dir_x=-self.dir_x
        self.dir_y=random.choice([-5,5])
    def rebotar(self):
        if self.x<=-self.ancho:
            self.reiniciar()
            self.puntuacion_maqui+=1
        if self.x>=winHori:
            self.reiniciar()
            self.puntuacion+=1
        if self.y<=0:
            self.dir_y=-self.dir_y
        if self.y+self.alto>=winVert:
            self.dir_y=-self.dir_y
class raqueta:
    def __init__(self):
        self.imagen=pygame.image.load("raqueta.png").convert_alpha()
        self.ancho,self.alto=self.imagen.get_size()
        self.x=0
        self.y=winVert/2-self.alto/2
        self.dir_y=0
    def movimiento(self):
        self.y+=self.dir_y
        if self.y<=0:
            self.y=0
        if self.y+self.alto>=winVert:
            self.y=winVert-self.alto
    def movimiento_maqui(self,pelota):
        if self.y>pelota.y:
            self.dir_y=-5
        elif self.y<pelota.y:
            self.dir_y=+5
        else:
            self.dir_y=0
        self.y+=self.dir_y
    def golpear(self,pelota):
        if (
            pelota.x<self.x+self.ancho 
            and pelota.x>self.x
            and pelota.y+pelota.alto>self.y
            and pelota.y<self.y+self.alto
        ):
            pelota.dir_x=-pelota.dir_x
            pelota.x=self.x+self.ancho
    def golpear_maqui(self,pelota):
        if (
            pelota.x+self.ancho >self.x
            and pelota.x<self.x+self.ancho
            and pelota.y+pelota.alto>self.y
            and pelota.y<self.y+self.alto
        ):
            pelota.dir_x=-pelota.dir_x
            pelota.x=self.x-self.ancho
    
    
def main(): 
   
    pygame.init()
    win=pygame.display.set_mode((winHori,winVert))
    pygame.display.set_caption("Mi Primer Juego de Pong")
    pelota=pelotaP("pong.png")
    fuente=pygame.font.Font(None,60)
    raqueta_1=raqueta()
    raqueta_1.x=60 
    raqueta_2=raqueta()
    raqueta_2.x=winHori-60-raqueta_2.ancho
    
    jugando=True
    pygame.mixer.music.load("summer.mp3")
    pygame.mixer.music.play()
    while jugando:
        pelota.movimiento()
        pelota.rebotar()
        raqueta_1.movimiento()
        raqueta_2.movimiento_maqui(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_maqui(pelota)

        win.fill(white)
        win.blit(pelota.imagen,(pelota.x,pelota.y))
        win.blit(raqueta_1.imagen,(raqueta_1.x,raqueta_1.y))
        win.blit(raqueta_2.imagen,(raqueta_2.x,raqueta_2.y))
        text=f"{pelota.puntuacion} : {pelota.puntuacion_maqui}"
        letre=fuente.render(text,False,negro)
        win.blit(letre,(winHori/2-fuente.size(text)[0]/2,50))
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando=False
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y=-5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y=5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y=0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y=0
        pygame.display.flip()
        pygame.time.Clock().tick(fps)
    pygame.quit()
if __name__ == '__main__':
    main()


     


    















