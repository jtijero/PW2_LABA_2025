# chess.py
from chessPictures import *
from interpreter import draw


# Crear una casilla blanca y una casilla negra
black_square = Picture(SQUARE).negative()
white_square = Picture(SQUARE)

# Crear una fila del tablero
def crearFila(primeracasilla):
    fila = Picture([])
    color_actual = primeracasilla
    for _ in range(8):
        casilla = white_square if color_actual == 'white' else black_square
        fila = fila.join(casilla) if fila.img else casilla
        color_actual = 'black' if color_actual == 'white' else 'white'
    return fila


# Crear los caballos y peones
knight = Picture(KNIGHT)
pawn = Picture(PAWN) 

# Crear filas de las piezas
fila8 = knight.horizontalRepeat(2)  # fila del rey negro
fila7 = pawn.horizontalRepeat(2)  # fila de peones negros

# Combinar las filas
fichasnegras = fila7.up(fila8).negative()  # fichas negras

# Crear el tablero de 8 filas
def chessboard():
    # Construcción modular del tablero
    tablero_base = Picture([])
    for i in range(8):
        fila = crearFila('white' if i%2==0 else 'black')
        tablero_base = tablero_base.up(fila.img)
    return tablero_base

    
    # Crear y dibujar el tablero
chessboardbase = chessboard()
new_chessboard = chessboard().under(fichasnegras)

draw(new_chessboard)
