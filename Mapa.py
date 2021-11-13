class Mapa:
    def __init__(self, paredes):
        self.paredes= paredes()

    """paredes es una lista de pares de coordenadas de donde se van a ubicar las paredes en el mapa,
    estos datos seran usados para definir las hitbox de las mismas"""

    def colision(self):
        pass
        #A definir en el proximo avance pues requiere PyGame
