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

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for valor in self.img:
            vertical.append(valor[::-1])
        return Picture(vertical)

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

    def under(self, p):
        """Superposición inteligente a nivel de píxel"""
        return Picture([
            ''.join([pc if pc != ' ' else bc for bc, pc in zip(base_row, overlay_row)])
            for base_row, overlay_row in zip(self.img, p.img)
        ])

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
        """ Devuelve una figura rotada en 90 grados en sentido horario """
