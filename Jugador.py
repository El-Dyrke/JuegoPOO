import pygame
from Proyectil import Proyectil
pygame.init()

class Jugador:
    def __init__(self, x, y, fuente, limite,timer):

        # Movimiento
        self.va_izquierda = False
        self.va_derecha = False
        self.va_arriba = False
        self.va_abajo = False
        self.contador_pasos= 0

        # Sprites
        self.fuente = fuente
        self.quieto = pygame.image.load(fuente+"derecha1.png")
        self.camina_derecha = [pygame.image.load(fuente + "derecha1.png"), pygame.image.load(fuente + "derecha2.png"), pygame.image.load(fuente + "derecha3.png")]
        self.camina_izquierda = [pygame.image.load(fuente + "izq1.png"), pygame.image.load(fuente + "izq2.png"), pygame.image.load(fuente + "izq3.png")]
        self.camina_arriba = [pygame.image.load(fuente + "arriba1.png"), pygame.image.load(fuente + "arriba2.png"), pygame.image.load(fuente + "arriba3.png")]
        self.camina_abajo = [pygame.image.load(fuente + "abajo1.png"), pygame.image.load(fuente + "abajo2.png"), pygame.image.load(fuente + "abajo3.png")]
        self.last = pygame.image.load(fuente+"derecha1.png")
        self.contador_pasos = 0
        self.HP = pygame.image.load(fuente+"vida.png")

        # Atributos
        self.vida = 5
        self.x = x
        self.y = y
        self.velocidad = 9
        self.ancho = self.quieto.get_width()//2
        self.alto = self.quieto.get_height()//2
        self.lx = self.x
        self.ly = self.y
        
        # Disparar
        self.ronda = 0
        self.max_disparos= 3
        self.balas = []
        self.zona_impacto=(self.x+15, self.y+15 , self.ancho-30, self.alto-30)

    def escalar(self, imagen, cuadro):
        cuadro.blit(pygame.transform.scale(imagen, (self.ancho,self.alto)),(self.x,self.y))
 
    def dibujar(self, cuadro):

        if self.contador_pasos + 1 > 15:
            self.contador_pasos = 3
        if self.va_izquierda:
            self.escalar(self.camina_izquierda[self.contador_pasos//5], cuadro)
            self.contador_pasos += 1
            self.last=self.camina_izquierda[0]
            
        elif self.va_derecha:
            self.escalar(self.camina_derecha[self.contador_pasos//5], cuadro)
            self.contador_pasos += 1
            self.last=self.camina_derecha[0]

        elif self.va_arriba:
            self.escalar(self.camina_arriba[self.contador_pasos//5], cuadro)
            self.contador_pasos += 1
            self.last=self.camina_arriba[0]

        elif self.va_abajo:
            self.escalar(self.camina_abajo[self.contador_pasos//5], cuadro)
            self.contador_pasos += 1
            self.last=self.camina_abajo[0]

        else:
            self.escalar(self.last,cuadro)
            self.contador_pasos = 0
        
        # "Barra" de vida
        if self.vida==5:
            cuadro.blit(pygame.transform.scale(self.HP, (self.ancho//5,self.alto//5)),(self.x+111,self.y-35))
        if self.vida>=4:
            cuadro.blit(pygame.transform.scale(self.HP, (self.ancho//5,self.alto//5)),(self.x+81,self.y-35))
        if self.vida>=3:
            cuadro.blit(pygame.transform.scale(self.HP, (self.ancho//5,self.alto//5)),(self.x+51,self.y-35))
        if self.vida>=2:
            cuadro.blit(pygame.transform.scale(self.HP, (self.ancho//5,self.alto//5)),(self.x+21,self.y-35))
        if self.vida>=1:
            cuadro.blit(pygame.transform.scale(self.HP, (self.ancho//5,self.alto//5)),(self.x-9,self.y-35))    
        
        self.zona_impacto = (self.x+15, self.y+15 , self.ancho-30, self.alto-30)

    def se_encuentra_con(self, alguien):

        R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
        R1_ar = self.zona_impacto[1]
        R1_iz = self.zona_impacto[0]
        R1_de = self.zona_impacto[0] + self.zona_impacto[2]
        R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
        R2_ar = alguien.zona_impacto[1]
        R2_iz = alguien.zona_impacto[0]
        R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]
        return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar and True

    def move(self, k, iz, de, u, dw, ventana_x, ventana_y, p):
        # Variables
        self.iz = iz
        self.de = de
        self.u = u
        self.dw = dw

        # Si es el jugador 1
        if p == 1:
            # Movimiento a izquierda
            if k[iz] and self.x > self.velocidad:
                self.x -= self.velocidad
                self.va_izquierda = True
                self.va_derecha = False
            # Movimiento a derecha
            elif k[de] and self.x < ventana_x//5*2 - self.ancho - self.velocidad:
                self.x += self.velocidad
                self.va_derecha = True
                self.va_izquierda = False
            # Detenerse horizontal
            else:			
                self.va_izquierda = False
                self.va_derecha = False

        # Si es el jugador 2
        if p == 2:
            # Movimiento a izquierda
            if k[iz] and self.x > ventana_x//5*3:
                self.x -= self.velocidad
                self.va_izquierda = True
                self.va_derecha = False
            # Movimiento a derecha
            elif k[de] and self.x < ventana_x - self.ancho - self.velocidad:
                self.x += self.velocidad
                self.va_derecha = True
                self.va_izquierda = False
            # Detenerse horizontal
            else:			
                self.va_izquierda = False
                self.va_derecha = False        
        
        # Movimiento a arriba 
        if k[u] and self.y > self.velocidad + self.alto//5 + 10:
            self.y -= self.velocidad
            self.va_arriba = True
            self.va_abajo = False
        # Movimiento a abajo
        elif k[dw] and self.y < ventana_y - self.alto - self.velocidad:
            self.y += self.velocidad
            self.va_abajo = True
            self.va_arriba = False
        # Detenerse vertical
        else:
            self.va_arriba = False
            self.va_abajo = False
        
    def disparar(k,f, self, otro, tanda, balas, default, maximo,ventana_x,timer,Par):
        # Manejo de los disparos
        if tanda > 0:
            tanda += 1
        if tanda > 3:
            tanda = 0
        # Contacto de proyectil con el enemigo
        for bala in balas:
            if otro.se_encuentra_con(bala):
                bala.impacta_a(otro)
                balas.pop(balas.index(bala)) # se elimina la bala del impacto

            if Par.se_encuentra_con(bala):
                balas.pop(balas.index(bala))

            # Limites movimiento bala
            if bala.x < ventana_x and bala.x > 0:
                bala.x += bala.velocidad
            else:
                balas.pop(balas.index(bala)) # Se elimina bala

        # capturar evento del disparo
        if k[f] and tanda == 0 and timer%4==0:
            direccion = default

            if len(balas) < maximo: # balas en pantalla
                balas.append(Proyectil(round(self.x + self.ancho // 2), round(self.y + self.alto // 2), direccion, self.fuente))
            tanda = 1
      
