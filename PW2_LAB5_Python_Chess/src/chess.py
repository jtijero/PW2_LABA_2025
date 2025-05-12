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
        casillaDerecha = white_square
    
    for i in range(8):  # Bucle del 0 al 7
        if (primeracasilla == 'black' and i % 2 == 0) or (primeracasilla == 'white' and i % 2 != 0):
            casillaDerecha = casillaDerecha.join(black_square)  # Añade casilla negra
        else:
            casillaDerecha = casillaDerecha.join(white_square)  # Añade casilla blanca
    
    return casillaDerecha  # Retorna la fila completa

# Crear el tablero de 8 filas
def chessboard():
    filas = []
    for i in range(8):
        if i % 2 == 0:
            filas.append(crearFila('white'))
        else:
            filas.append(crearFila('black'))
    
    chessboard = filas[0]
    for fila in filas[1:]:
        chessboard = chessboard.up(fila)
    
    # Colocar las fichas negras dentro del tablero
    return chessboard.under(fichasnegras)
    # Crear los caballos
    knight = Picture(KNIGHT)
    pawn = Picture(PAWN) 

# Crear las filas de caballos
fila8 = knight.horizontalRepeat(2)  # fila del rey negro
fila7 = pawn.horizontalRepeat(2)  # fila de peones negros

# Combinar las filas
fichasnegras = fila7.up(fila8).negative()  # fichas negras
# Crear y dibujar el tablero
chessboard = chessboard()
draw(chessboard)
