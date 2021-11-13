import Proyectil
class Jugador:
    def __init__(self, u, dw, iz, de, f):
        self.vida = 5
        self.balas = 3
        self.u = u
        self.dw = dw
        self.iz = iz
        self.de = de
        self.f = f
        self.bala = Proyectil(5)

       
    def move(self):
        pass
        #A definir en el proximo avance pues requiere PyGame
        #Toma las variables introducidas en el init y las usa para el movimiento del personaje

    def disparar(self):
        pass
        #A definir en el proximo avance pues requiere PyGame
        #Usa self.f para accionar el disparo

