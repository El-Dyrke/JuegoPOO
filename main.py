from pygame import time
from pygame.constants import TIMER_RESOLUTION
from Jugador import Jugador
from Mapa import Mapa
from Pared import Pared

import pygame
pygame.init()

if __name__ == "__main__":
    
    # Variables ventan
    ventana_x = 1050
    ventana_y = 650
    ventana = pygame.display.set_mode((ventana_x,ventana_y))

    # Caption
    pygame.display.set_caption("POO")
    # Reloj
    reloj = pygame.time.Clock()

    timer = 0 #Para la velocidad de disparo

    # Mapeado
    paredes1 = [Pared(ventana_x//5, 0, ventana_x//11, ventana_y//3), Pared(ventana_x//3*2, ventana_y//3*2, ventana_x//11, ventana_y//3 )]

    # ----------------  Función para repintar el cuadro de juego -----------------
    def refresh():
        # Fondo
        ventana.fill((107,171,242))

        # Mapa
        Map.dibujar(ventana)

        # Jugadores
        Dr.dibujar(ventana)
        Virus.dibujar(ventana)

        # Proyectiles
        for bala in balas_Dr:
            bala.dibujar(ventana)

        for bala in balas_Virus:
            bala.dibujar(ventana)

        # Refrescar
        pygame.display.update()

    # Variable que controla la repeticion del juego completo con todas sus pantallas
    repetir = True 

    # ------------------------- Ciclo de redefinicion de variables ---------------------------
    while repetir:
        
	    # Inicializar jugadores
        Dr = Jugador(int(5), int(5), "img/Dr/", ventana_x)
        Virus = Jugador(int(ventana_x-128), int(ventana_y-130), "img/Virus/", ventana_x)

        # Inicializar mapa
        Map = Mapa(paredes1)

        # Variables para disparos
        tanda_Dr = 0
        balas_Dr=[]
        
        tanda_Virus = 0
        balas_Virus = []

        # Fuentes texto
        texto_intro = pygame.font.SysFont('Times New Roman', 40, True)
        texto_instrucciones = pygame.font.SysFont('console', 25, True)
        texto_resultado = pygame.font.SysFont('Times New Roman', 30, True)

        #Variables fases de juego
        intro = True
        fin = False

        # Resultado
        ganaVirus = False
        ganaDr = False

        # -------------------- Introduccion------------------
        while intro:

            # Control de velocidad del juego
            reloj.tick(30)

            # Cierre ventana
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
            
            ventana.fill((19, 36, 117))

            titulo = texto_intro.render('INOCULACION', 1, (226, 228, 238))
            instrucciones = texto_instrucciones.render('Presione ENTER para jugar', 1, (2, 5, 15))
            instrucciones2 = texto_instrucciones.render('Presione ESC en cualquier momento para salir', 1, (2, 5, 15))
            
            ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 50))
            ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, 300))
            ventana.blit(instrucciones2, ((ventana_x//2)-instrucciones2.get_width()//2, 340))

            k = pygame.key.get_pressed()

            if k[pygame.K_RETURN]:
                intro=False
                esta_jugando = True
            if k[pygame.K_ESCAPE]:
                quit()
            
            # Dev codeslol
            if k[pygame.K_LCTRL] and k[pygame.K_f] and k[pygame.K_c]:
                fin = True
                ganaDr = True
                intro = False
                esta_jugando = False
            if k[pygame.K_LCTRL] and k[pygame.K_f] and k[pygame.K_v]:
                fin = True
                ganaVirus = True
                intro = False
                esta_jugando = False
                

            pygame.display.update()
        
        #--------------------- Ciclo de Juego ---------------------------
        while esta_jugando:

            timer+=1
            if timer==16: # Evita que el timer se salga de control LOL
                timer=0
            ventana.fill((0,0,0))

            # Control de velocidad del juego
            reloj.tick(30)

            # Cierre ventana
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()

            # Detectar teclas presionadas
            k = pygame.key.get_pressed()
            # Movimiento jugadores
            Virus.move(k, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, ventana_x, ventana_y, Map)
            Dr.move(k, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, ventana_x, ventana_y, Map)
            
            # Cerrar el jugo con "esc"
            if k[pygame.K_ESCAPE]:
                quit() 

            # Disparar
            Jugador.disparar(k, pygame.K_x , Dr, Virus, tanda_Dr, balas_Dr, 1, 3,ventana_x,timer)
            Jugador.disparar(k,pygame.K_RCTRL, Virus, Dr, tanda_Virus, balas_Virus, -1, 3,ventana_x,timer)

            # Chocar con las paredes
            Map.chocar_paredes(Dr)

            # Terminar juego
            if Virus.vida < 1:
                esta_jugando = False
                ganaDr = True
            if Dr.vida < 1:
                esta_jugando = False
                ganaVirus = True

            # Dev codeslol
            if k[pygame.K_LCTRL] and k[pygame.K_f] and k[pygame.K_c]:
                fin = True
                ganaDr = True
                intro = False
                esta_jugando = False
            if k[pygame.K_LCTRL] and k[pygame.K_f] and k[pygame.K_v]:
                fin = True
                ganaVirus = True
                intro = False
                esta_jugando = False
            # Repintar
            refresh()
        # ------------------- Final ----------------------
        fin = True
        while fin:

            # Cierre ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # Fondo
            ventana.fill((15, 6, 23)) 
            # Textos
            titulo = texto_intro.render('JUEGO TERMINADO', 1, (230, 226, 235))
            if ganaDr:
                resultado = texto_resultado.render("Ha Ganado el doctor, la pandemia se acabo", 1, (230, 226, 235))
            if ganaVirus:
                resultado = texto_resultado.render("El fin del hombre ha llegado, RIP", 1, (230, 226, 235))
            instrucciones = texto_instrucciones.render('Presione "r" para volver a jugar', 1, (230, 226, 235))
            instrucciones2 = texto_instrucciones.render("Presione ENTER para salir", 1, (230, 226, 235))

            # Dibujar textos
            ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 50))
            ventana.blit(resultado, ((ventana_x//2)-resultado.get_width()//2, 300))
            ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, ventana_y//5*3.5))
            ventana.blit(instrucciones2, ((ventana_x//2)-instrucciones2.get_width()//2, ventana_y//5*4))

            k = pygame.key.get_pressed()

            if k[pygame.K_ESCAPE] or k[pygame.K_RETURN]:
                quit()

            if k[pygame.K_r]:
                repetir = True
                fin=False
                # Asegurar reinicio de jugadores
                del(Dr)
                del(Virus)
                
            
            pygame.display.update()
            

