from colors import *

class Picture:
    def __init__(self, img):
        self.img = img if isinstance(img, list) else [str(img)]

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):  # Actual verticalMirror
      return Picture([fila[::-1] for fila in self.img])


    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = self.img[::-1]
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negativo = []
        for fila in self.img:
            nueva_fila = ''.join(self._invColor(c) for c in fila)
            negativo.append(nueva_fila)
        return Picture(negativo)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        nueva_imagen = []
        for fila1, fila2 in zip(self.img, p.img):
            nueva_imagen.append(fila1 + fila2)
        return Picture(nueva_imagen)

    def up(self, p):
        """Combina verticalmente con otra Picture o lista"""
        if isinstance(p, list):
            return Picture(self.img + p)
        return Picture(p.img + self.img)

    def under(self, other):
        """
        Superpone dos objetos Picture. La imagen 'other' se coloca sobre 'self'.
        Los píxeles transparentes (representados por espacio ' ') en 'other' permiten
        ver la imagen subyacente 'self'.

        Parámetros:
        other (Picture): Imagen a superponer
        Retorna:
        Picture: Nueva imagen combinada
        """
        # Validación 1: Misma cantidad de filas
        if len(self.img) != len(other.img):
            raise ValueError(
                f"Error en altura: {len(self.img)} vs {len(other.img)} filas"
            )
    
        # Validación 2: Mismo ancho en todas las filas
        for i, (fila_self, fila_other) in enumerate(zip(self.img, other.img)):
            if len(fila_self) != len(fila_other):
                raise ValueError(
                    f"Ancho incompatible en fila {i}: "
                    f"{len(fila_self)} vs {len(fila_other)} caracteres"
                )
    
        # Combinación pixel a pixel
        imagen_combinada = [
            ''.join(
            # Mantener pixel de 'other' excepto si es transparente
            pixel_other if pixel_other != ' ' else pixel_self
            for pixel_self, pixel_other in zip(fila_self, fila_other)
            )
            for fila_self, fila_other in zip(self.img, other.img)
        ]
    
        return Picture(imagen_combinada)

    
    def resize(self, width, height):
        """Redimensiona la imagen al tamaño especificado"""
        return Picture(
          [row[:width] for row in self.img[:height]]
        )


    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        repetida = []
        for fila in self.img:
            repetida.append(fila * n)
        return Picture(repetida)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
            la cantidad de veces que indique el valor de n """
        repetida = self.img * n
        return Picture(repetida)

    def rotate(self):
      """Devuelve una figura rotada 90 grados en sentido horario
          Caso imagen vacía
          Determinar el número de columnas (todas las filas deben tener igual longitud)
          Construir la imagen rotada
          Toma caracteres verticalmente desde abajo hacia arriba"""
      if not self.img:  
        return Picture([])
    
      columnas = len(self.img[0])
      
      imagen_rotada = [
          ''.join([fila[i] for fila in reversed(self.img)])  
          for i in range(columnas)
      ]
      return Picture(imagen_rotada)
