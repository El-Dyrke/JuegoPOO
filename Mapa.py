import pygame
import Pared
import Jugador
pygame.init()

class Mapa:
    def __init__(self, paredes):
        self.paredes= paredes

    def dibujar(self, cuadro):
        for pared in self.paredes:
            pygame.draw.rect(cuadro, (255,0,0), pared.zona_impacto, 2)
    
    def chocar_paredes(self, p):
        for pared in self.paredes:
            pared.se_encuentra_con(p)
