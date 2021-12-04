import pygame
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

    def dibujar(self, cuadro):

        cuadro.blit(pygame.transform.scale(self.imagen, (self.ancho,self.alto)), (self.x, self.y))
        self.zona_impacto = (self.x, self.y , self.ancho, self.alto)
        #pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)
    
    def impacta_a(self, otro):
        if otro.vida > 0:
            otro.vida -= 1
        

    
        