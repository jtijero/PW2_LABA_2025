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


torre_negra = rock.negative()
caballo_negro = knight.negative()
alfil_negro = bishop.negative()
reina_negra = queen.negative()
rey_negro = king.negative()
peon_negro = pawn.negative()

# Blancas (versiones originales)
torre_blanca = rock.horizontalMirror()
caballo_blanco = knight.horizontalMirror()
alfil_blanco = bishop.horizontalMirror()
reina_blanca = queen.horizontalMirror()
rey_blanco = king.horizontalMirror()
peon_blanco = pawn.horizontalMirror()

def configurar_piezas_iniciales(tablero):
    """Coloca todas las piezas en posición inicial"""
    # Piezas negras (filas 0 y 1)
    piezas_negras = [torre_negra.rotate(), caballo_negro, alfil_negro, reina_negra, 
                    rey_negro, alfil_negro, caballo_negro.verticalMirror(), torre_negra.rotate()]
    
    for x in range(8):
        tablero = colocar_ficha(tablero, piezas_negras[x], x, 7)
        tablero = colocar_ficha(tablero, peon_negro, x, 6)    
    
    # Piezas blancas (filas 6 y 7)
    piezas_blancas = [torre_blanca.rotate(), caballo_blanco, alfil_blanco, reina_blanca,
                     rey_blanco, alfil_blanco, caballo_blanco.verticalMirror(), torre_blanca.rotate()]
    
    for x in range(8):
        tablero = colocar_ficha(tablero, piezas_blancas[x], x, 0) 
        tablero = colocar_ficha(tablero, peon_blanco, x, 1)        
    
    return tablero

tablero_vacio = chessboard()
tablero_completo = configurar_piezas_iniciales(tablero_vacio)
draw(tablero_completo)

