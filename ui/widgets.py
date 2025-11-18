import tkinter as tk
from core.utils import rgb_a_hex
from functools import partial

def crear_botones(frame, generar_paleta):
    botones = {
        "general_paleta": "Generar Paleta",
        "guardar": "Guardar",
        "modo_ia": "Modo IA"
    }

    for identificar, texto in botones.items():
        boton = tk.Button(frame, text=texto)

        if identificar == "general_paleta":
            boton.config(command=generar_paleta)

        boton.pack(side="left", padx=5)

def crear_paneles_colores(frame, colores=None):
    for widget in frame.winfo_children():
        widget.destroy()

    if colores is None:
        colores = [(255, 255, 255)] * 4  # blanco por defecto

    for color in colores:
        hex_color = rgb_a_hex(color)
        panel = tk.Frame(frame, bg=hex_color, width=100, height=100)
        panel.pack(side="left", padx=5)

import tkinter as tk

class ElementoVisual:
    def __init__(self, nombre, imagen, descripcion):
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion

    @staticmethod
    def mostrar_lista_elementos(frame_derecho, seleccionar_funcion, arrastre_funcion):
     elementos = [
        ElementoVisual("button", "img_boton.png", "Un botón clickeable"),
        ElementoVisual("frame", "img_frame.png", "Contenedor de elementos"),
        ElementoVisual("label", "img_label.png", "Elemento de texto")
     ]

     def manejar_presion(tipo):
        def handler(event):
            seleccionar_funcion(tipo)
            arrastre_funcion(event)
        return handler

     for elem in elementos:
        item_frame = tk.Frame(frame_derecho, bg="#eeeeee", pady=5)
        item_frame.pack(fill="x", padx=5)

        img_label = tk.Label(item_frame, bg="gray", width=4, height=2)
        img_label.pack(side="left", padx=5)

        texto = tk.Label(item_frame, text=f"{elem.nombre}\n{elem.descripcion}", justify="left")
        texto.pack(side="left", padx=5)

        for widget in [item_frame, img_label, texto]:
            widget.bind("<ButtonPress-1>", manejar_presion(elem.nombre))