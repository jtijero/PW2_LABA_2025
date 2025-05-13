from chessPictures import *
from interpreter import draw

black_square = Picture(SQUARE).negative()
white_square = Picture(SQUARE)

def crearFila(primeracasilla):
    fila = Picture([])
    color_actual = primeracasilla
    for _ in range(8):
        casilla = white_square if color_actual == 'white' else black_square
        fila = fila.join(casilla) if fila.img else casilla
        color_actual = 'black' if color_actual == 'white' else 'white'
    return fila


def chessboard():
    fila_blanca = crearFila('white')  # 8x60 = 480 caracteres
    fila_negra = crearFila('black')
    tablero_base = fila_blanca.up(fila_negra).verticalRepeat(4)  # 8 filas (4 pares)
    return tablero_base


tablero= chessboard()  

# Nuevo método para posicionar fichas en coordenadas
def colocar_ficha(tablero, ficha, x, y):
    # Tamaño de cada casilla
    ancho_casilla = 58
    alto_casilla = 58
    
    # Validar coordenadas
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        raise ValueError("Coordenadas fuera del tablero (0-7)")
    
    # Calcular posición inicial en píxeles
    inicio_x = x * ancho_casilla
    inicio_y = y * alto_casilla
    
    # Crear capa transparente
    capa = []
    for i, fila in enumerate(tablero.img):
        if inicio_y <= i < inicio_y + alto_casilla:
            # Insertar línea de la ficha en posición horizontal
            linea_ficha = ficha.img[i - inicio_y]
            nueva_linea = fila[:inicio_x] + linea_ficha + fila[inicio_x + ancho_casilla:]
            capa.append(nueva_linea)
        else:
            # Línea completamente transparente
            capa.append(' ' * len(fila))
    
    return tablero.under(Picture(capa))


# Crear piezas de 60x60 caracteres
caballo_negro = knight.negative()
peon_negro = pawn.negative()
# Colocar caballo en a1 (0,0) y peón en d4 (3,3)
tablero = colocar_ficha(tablero, caballo_negro, x=0, y=0)  # a1
tablero = colocar_ficha(tablero, peon_negro, x=3, y=3)     # d4 (3*60=180)


draw(tablero)

