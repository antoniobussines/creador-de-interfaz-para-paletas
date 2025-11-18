import random

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
