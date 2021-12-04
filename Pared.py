import pygame
import Jugador
pygame.init()

class Pared:
    def __init__(self, x, y, ancho, alto):
        self.zona_impacto = (x, y , ancho, alto)

    def se_encuentra_con(self, alguien):
        alguien.zona_impacto = (alguien.x+15, alguien.y+15 , alguien.ancho-30, alguien.alto-30)

        R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
        R1_ar = self.zona_impacto[1]
        R1_iz = self.zona_impacto[0]
        R1_de = self.zona_impacto[0] + self.zona_impacto[2]
        R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
        R2_ar = alguien.zona_impacto[1]
        R2_iz = alguien.zona_impacto[0]
        R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]
        return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar