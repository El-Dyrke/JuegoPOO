from Jugador import Jugador
from Mapa import Mapa
from Partida import Partida
from Proyectil import Proyectil

if __name__ == "__main__":
    Doctor=Jugador
    print("\nLos movimientos del jugador son:\na: Izquierda\nd: Derecha\nw: Arriba\ns: Abajo\nc: Disparo\nPresione cualquier otra tecla para salir.")
    while True:
        Mov=input()
        if Mov=="a" or Mov=="A":
            print("El jugador se mueve a la izquierda")
        elif Mov=="d" or Mov=="D":
            print("El jugador se mueve a la derecha ")
        elif Mov=="w" or Mov=="W":
            print("El jugador se mueve hacia arriba")
        elif Mov=="s" or Mov=="S":
            print("El jugador se mueve hacia abajo")
        elif Mov=="c" or Mov=="C":
            print("El jugador dispara")
        else:
            break