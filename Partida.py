import Jugador
import Mapa

class Partida:
    def __init__(self, rondas):
        self.jugador1 = Jugador("up","dwn","iz","der")
        self.jugador2 = Jugador("up","dwn","iz","der")
        #Los argumentos seran elementos de pygame correspondientes a las teclas de movimiento
        paredes = ("x1", "y1", "x2", "y2")
        self.Map = Mapa(paredes)
        self.rondas = rondas #Define el n° de rondas a jugar
