from Jugador import Jugador
from Mapa import Mapa
from Partida import Partida
#from Proyectil import Proyectil
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

    # ----------------  Función para repintar el cuadro de juego -----------------
    def refresh():
        ventana.fill((107,171,242))
        Dr.dibujar(ventana)
        pygame.display.update()

    # Variable que controla la repeticion del juego completo con todas sus pantallas
    repetir = True 

    # ------------------------- Ciclo de repeticion de todo el juego ---------------------------
    while repetir:

	    # Inicializacion de elementos del juego
        Dr = Jugador(int(0), int(0), "Juego POO/img/Dr/", ventana_x)
        
       
        

        esta_jugando=True
        while esta_jugando:

            ventana.fill((0,0,0))

            # Control de velocidad del juego
            reloj.tick(27)

            # Evento de boton de cierre de ventana
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()

            #Detectar teclas presionadas
            k = pygame.key.get_pressed()
            #Movimiento jugador(es)
            Dr.move(k, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, ventana_x, ventana_y)
            
            
            refresh()