from pygame.constants import K_x
from Jugador import Jugador
from Mapa import Mapa
#from Partida import Partida
from Proyectil import Proyectil
import pygame

pygame.init()

if __name__ == "__main__":
    
        # ----------- Declarar constantes -------------------------
    ventana_x = 1050
    ventana_y = 650
    ventana = pygame.display.set_mode((ventana_x,ventana_y))
    pygame.display.set_caption("POO")
    reloj = pygame.time.Clock()
    negro = (0,0,0)
    fuente=pygame.font.SysFont("segoe print", 22)
    puntaje = 0
    timer = 0 #Para la velocidad de disparo

    def disparar(k,f, self, otro, tanda, balas, default, maximo):
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

            # Limites movimiento bala
            if bala.x < ventana_x and bala.x > 0:
                bala.x += bala.velocidad
            else:
                balas.pop(balas.index(bala)) # Se elimina bala

        # capturar evento del disparo
        if k[f] and tanda == 0 and timer%4==0:
            if self.last==self.camina_izquierda[0]:
                direccion = -1
            elif self.last==self.camina_derecha[0]:
                direccion = 1
            else:
                direccion = default

            if len(balas) < maximo: # balas en pantalla
                balas.append(Proyectil(round(self.x + self.ancho // 2), round(self.y + self.alto // 2), direccion, self.fuente))
            tanda = 1

        

    # ----------------  Función para repintar el cuadro de juego -----------------
    def refresh():
        ventana.fill((107,171,242))
        Dr.dibujar(ventana)
        Virus.dibujar(ventana)
        for bala in balas_Dr:
            bala.dibujar(ventana)
        for bala in balas_Virus:
            bala.dibujar(ventana)
        pygame.display.update()

    # Variable que controla la repeticion del juego completo con todas sus pantallas
    repetir = True 

    # ------------------------- Ciclo de repeticion de todo el juego ---------------------------
    while repetir:
        
	    # Inicializacion de elementos del juego
        Dr = Jugador(int(0), int(0), "img/Dr/", ventana_x)
        Virus = Jugador(int(600), int(300), "img/Virus/", ventana_x)

        # Variables para disparos
        tanda_Dr = 0
        balas_Dr=[]
        
        tanda_Virus = 0
        balas_Virus = []

        esta_jugando=True
        while esta_jugando:

            timer+=1
            if timer==16: #Evita que el timer se salga de control LOL
                timer=0
            ventana.fill((0,0,0))
            # Control de velocidad del juego
            reloj.tick(30)

            # Evento de boton de cierre de ventana
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()

            #Detectar teclas presionadas
            k = pygame.key.get_pressed()
            #Movimiento jugadores
            Virus.move(k, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, ventana_x, ventana_y)
            Dr.move(k, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, ventana_x, ventana_y)
            
            # Cerrar el jugo con "esc"
            if k[pygame.K_ESCAPE]:
                quit() 

            #Disparar
            disparar(k, pygame.K_x , Dr, Virus, tanda_Dr, balas_Dr, 1, 3)
            disparar(k,pygame.K_RCTRL, Virus, Dr, tanda_Virus, balas_Virus, -1, 3)

            #if Dr.se_encuentra_con(Virus)==True:
            #    print("1")

            # Repintar
            refresh()
            

