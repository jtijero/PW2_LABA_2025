# chess.py
from chessPictures import *
from interpreter import draw

# Crear una casilla blanca y una casilla negra
black_square = Picture(SQUARE).negative()
white_square = Picture(SQUARE)

# Crear una fila del tablero
def crearFila(primeracasilla):
    if (primeracasilla == 'white'):
      casillaDerecha = black_square
    else:
      casillaDerecha = white_square # Inicializa la fila vacía
    
    for i in range(7):  # Bucle del 0 al 6
        if (primeracasilla == 'black' and i % 2 == 0) or (primeracasilla == 'white' and i % 2 != 0):
            casillaDerecha = casillaDerecha.join(black_square)  # Añade casilla blanca
        else:
            casillaDerecha = casillaDerecha.join(white_square)  # Añade casilla negra
    
    return casillaDerecha  # Retorna la fila completa


# Crear el tablero de 2 filas
def chessboard():
    first_row = crearFila('white')  # Fila con blanco a la izquierda
    second_row = crearFila('black')  # Fila con negro a la izquierda
    
    # Combinar las filas para formar el tablero
    fila1y2 = first_row.up(second_row)
    fila3y4 = fila1y2
    mitadTablero = fila1y2.up(fila3y4)
    chessboard = mitadTablero.up(mitadTablero)
    return chessboard

# Crear y dibujar el tablero
chessboard = chessboard()
draw(chessboard)
