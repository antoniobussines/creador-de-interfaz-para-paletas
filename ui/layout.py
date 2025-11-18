import tkinter as tk
from ui.widgets import ElementoVisual

tipo_seleccionado = None  # Global para mantener el tipo actual

def seleccionar_tipo(tipo):
    global tipo_seleccionado
    tipo_seleccionado = str(tipo).lower()
    print(f"[DEBUG] Tipo seleccionado: {tipo_seleccionado}")

def crear_widget_en_canvas(canva, tipo, x, y):
    tipo = str(tipo).lower()

    if tipo == "button":
        widget = tk.Button(canva, text="Botón")
    elif tipo == "label":
        widget = tk.Label(canva, text="Etiqueta")
    elif tipo == "frame":
        widget = tk.Frame(canva, width=100, height=50, bg="#cccccc")
    else:
        print(f"[ERROR] Tipo desconocido: {tipo}")
        return

    canva.create_window(x, y, window=widget)

def crear_ventana():
    root = tk.Tk()
    root.geometry("500x250")
    root.title("Paleta de Colores")

    canva = tk.Canvas(root, bg="#f0f0f0")
    canva.pack(side="left", fill="both", expand=True)

    panel_derecho = tk.Frame(root)
    panel_derecho.pack(side="right", fill="y")

    frame_panel_derecho = tk.Frame(panel_derecho)
    frame_panel_derecho.pack(fill="x")
    tk.Label(frame_panel_derecho, text="panel derecho", font=("Arial", 12, "bold")).pack(fill="x")

    def iniciar_arrastre(event):
        canva.bind('<ButtonRelease-1>', soltar_elemento)

    def soltar_elemento(event):
        global tipo_seleccionado
        print(f"[DEBUG] Al soltar: tipo_seleccionado = {tipo_seleccionado}")
        x, y = event.x, event.y
        crear_widget_en_canvas(canva, tipo_seleccionado, x, y)
        canva.unbind("<ButtonRelease-1>")

    # ✅ Mostrar elementos en el panel derecho
    ElementoVisual.mostrar_lista_elementos(panel_derecho, seleccionar_tipo, iniciar_arrastre)

    root.mainloop()
