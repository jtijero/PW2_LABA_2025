# chess.py
from chessPictures import *
from interpreter import draw

# Crear los caballos
white_knight = Picture(KNIGHT)  # Caballo blanco
black_knight = Picture(KNIGHT).negative()  # Caballo negro (negativo del blanco)

# Crear las filas de caballos
first_row = white_knight.horizontalRepeat(1).join(black_knight.horizontalRepeat(1)) 
second_row = first_row.verticalMirror() 

# Combinar las filas
fila1y2 = first_row.up(second_row)  # Colocar la fila de caballos negros sobre la de caballos blancos

# Dibujar la imagen combinada
draw(fila1y2)
