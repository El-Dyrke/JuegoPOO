#import Proyectil
import pygame
pygame.init()

class Jugador:
    def __init__(self, x, y, fuente, limite):#fuente Dr= img/Dr/ virus= img/Virus/

        #Movimiento
        self.camino = [100, limite]
        self.va_izquierda = False
        self.va_derecha = False
        self.va_arriba = False
        self.va_abajo = False

        #Sprites
        self.quieto = pygame.image.load(fuente+"arriba1.png")
        self.camina_derecha = [pygame.image.load(fuente + "derecha1.png"), pygame.image.load(fuente + "derecha2.png"), pygame.image.load(fuente + "derecha3.png")]

        self.camina_izquierda = [pygame.image.load(fuente + "izq1.png"), pygame.image.load(fuente + "izq2.png"), pygame.image.load(fuente + "izq3.png")]

        self.camina_arriba = [pygame.image.load(fuente + "arriba1.png"), pygame.image.load(fuente + "arriba2.png"), pygame.image.load(fuente + "arriba3.png")]

        self.camina_abajo = [pygame.image.load(fuente + "abajo1.png"), pygame.image.load(fuente + "abajo2.png"), pygame.image.load(fuente + "abajo3.png")]

        #Disparar
        #self.balas = 3
        #self.bala = Proyectil(5)

        #Atributos
        self.vida = 5
        self.x = x
        self.y = y
        self.velocidad = 15
        self.ancho = self.quieto.get_width()//2
        self.alto = self.quieto.get_height()//2

    def parche(self):
        if self.contador_pasos > 2:
            self.contador_pasos = 0

    def escalar(self, imagen, cuadro):
        cuadro.blit(pygame.transform.scale(imagen, (self.ancho,self.alto)),(self.x,self.y))
        
 
    def dibujar(self, cuadro):
        if self.va_izquierda:
            self.escalar(self.camina_izquierda[self.contador_pasos], cuadro)
            self.contador_pasos += 1
            #self.parche()
        elif self.va_derecha:
            self.escalar(self.camina_derecha[self.contador_pasos], cuadro)
            self.contador_pasos += 1
            #self.parche()
        elif self.va_arriba:
            self.escalar(self.camina_arriba[self.contador_pasos], cuadro)
            self.contador_pasos += 1
            #self.parche()
        elif self.va_abajo:
            self.escalar(self.camina_abajo[self.contador_pasos], cuadro)
            self.contador_pasos += 1
            #self.parche()
        else:
            self.escalar(self.quieto,cuadro)
            self.contador_pasos = 0
       
    def move(self, k, iz, de, u, dw, ventana_x, ventana_y):

        #Variables
        self.iz = iz
        self.de = de
        self.u = u
        self.dw = dw
    
        # Movimiento a izquierda
        if k[iz] and self.x > self.velocidad:
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
            self.contador_pasos = 0
        
        # Movimiento a arriba 
        if k[u] and self.y > self.velocidad:
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
            self.contador_pasos = 0


    def disparar(self):
        #A definir en el proximo avance pues requiere PyGame
        #Usa self.f para accionar el disparo
        pass