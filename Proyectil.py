import pygame
import Jugador
pygame.init()

class Proyectil:
    def __init__(self, x, y, direccion, fuente):

        self.x = x
        self.y = y
        
        self.velocidad = 15 * direccion
        if direccion==1:
            self.imagen= pygame.image.load(fuente+"disparo1.png")
        if direccion==-1:
            self.imagen= pygame.image.load(fuente+"disparo2.png")
        self.ancho = self.imagen.get_width()//4
        self.alto = self.imagen.get_height()//4
        #pygame.transform.scale(imagen, (self.ancho,self.alto)

    #def se_encuentra_con(self, alguien):
	#    R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
	#    R1_ar = self.zona_impacto[1]
	#    R1_iz = self.zona_impacto[0]
	#    R1_de = self.zona_impacto[0] + self.zona_impacto[2]
	#    R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
	#    R2_ar = alguien.zona_impacto[1]
	 #   R2_iz = alguien.zona_impacto[0]
	#    R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]
	 #   return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar and True

    def dibujar(self, cuadro):

        cuadro.blit(pygame.transform.scale(self.imagen, (self.ancho,self.alto)), (self.x, self.y))
        self.zona_impacto = (self.x, self.y , self.ancho, self.alto)
        pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)
    
    def impacta_a(self, alguien):
        print("hit")

    
        