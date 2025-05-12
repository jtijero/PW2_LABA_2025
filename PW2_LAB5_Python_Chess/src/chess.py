# chess.py
from chessPictures import *
from interpreter import draw

# Crear los caballos
white_knight = Picture(KNIGHT)  # Caballo blanco
black_knight = Picture(KNIGHT).negative()  # Caballo negro (negativo del blanco)

# Crear las filas de caballos
first_row = white_knight.horizontalRepeat(2)  # 2 caballos blancos en la primera fila
second_row = black_knight.horizontalRepeat(2)  # 2 caballos negros en la segunda fila

# Combinar las filas
combined_picture = first_row.up(second_row)  # Colocar la fila de caballos negros sobre la de caballos blancos

# Dibujar la imagen combinada
draw(combined_picture)
