import pygame
pygame.init()

class Mapa:
    def __init__(self, paredes):
        self.paredes= paredes

    def dibujar(self, cuadro):
        for pared in self.paredes:
            pygame.draw.rect(cuadro, (255,0,0), pared, 2)
        #A definir en el proximo avance pues requiere PyGame
