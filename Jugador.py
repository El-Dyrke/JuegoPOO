import pygame
pygame.init()

class Jugador:
    def __init__(self, x, y, fuente, limite):

        # Movimiento
        #self.camino = [100, limite]
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

        # Atributos
        self.vida = 5
        self.x = x
        self.y = y
        self.velocidad = 9
        self.ancho = self.quieto.get_width()//2
        self.alto = self.quieto.get_height()//2

        # Disparar
        self.ronda = 0
        self.max_disparos= 3
        self.balas = []

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
        
        # Hitbox
        self.zona_impacto = (self.x+15, self.y+15 , self.ancho-30, self.alto-30)
        #pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)

    def move(self, k, iz, de, u, dw, ventana_x, ventana_y):

        # Variables
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

    
