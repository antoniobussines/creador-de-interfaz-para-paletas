import random
import colorsys

class Paleta:
    def __init__(self, base_rgb=None):
        self.base = base_rgb or self.generar_color_aleatorio()
        self.colores = self.generar_colores()

    def generar_color_aleatorio(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def generar_colores(self):
        r, g, b = self.base
        return [
            self.base,
            ((r + 30) % 256, (g + 30) % 256, (b + 30) % 256),
            ((r - 30) % 256, (g - 30) % 256, (b - 30) % 256),
            (255 - r, 255 - g, 255 - b)
        ]
    
    def generar_variante(self):

        return[self.generar_colores() for _ in range(4)]
class ArmoniaColor:
    def __init__(self, base_rgb):
        self.base = base_rgb
        self.h, self.l, self.s = self.rgb_a_hls(base_rgb)

    def rgb_a_hls(self, rgb):
        r, g, b = [x / 255.0 for x in rgb]
        return colorsys.rgb_to_hls(r, g, b)

    def hls_a_rgb(self, h, l, s):
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return (int(r * 255), int(g * 255), int(b * 255))

    def generar(self, tipo):
        angulos = {
            "triada": [0, 120, 240],
            "cuadrado": [0, 90, 180, 270],
            "complementaria": [0, 180],
            "analogica": [-30, 0, 30],
            "separacion": [-150, 0, 150],
            "compuesta": [0, 150, -30],
            "monocromatica": [0],
            "tonos": [0],
        }
        hs = [(self.h + a / 360.0) % 1.0 for a in angulos.get(tipo, [0])]
        return [self.hls_a_rgb(h, self.l, self.s) for h in hs]