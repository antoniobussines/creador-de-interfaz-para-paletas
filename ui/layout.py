import tkinter as tk
from tkinter import ttk
import colorsys
import math
from core.palete import Paleta, ArmoniaColor
from core.utils import rgb_a_hex

# --- Dibujar círculo cromático ---
def dibujar_circulo_cromatico(canvas, radio=100):
    for i in range(360):
        h = i / 360.0
        r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
        color = "#%02x%02x%02x" % (int(r*255), int(g*255), int(b*255))
        canvas.create_arc(
            10, 10, 10 + 2*radio, 10 + 2*radio,
            start=i, extent=1,
            fill=color, outline=color
        )

# --- Marcar colores de la paleta en el círculo ---
def marcar_colores_en_circulo(canvas, colores, radio=100):
    cx, cy = 10 + radio, 10 + radio
    for c in colores:
        hex_color = rgb_a_hex(c)
        r, g, b = c[0]/255.0, c[1]/255.0, c[2]/255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        angulo = h * 2 * math.pi
        x = cx + radio * math.cos(angulo)
        y = cy - radio * math.sin(angulo)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill=hex_color, outline="black", width=1)

# --- Mostrar paleta y variaciones ---
def mostrar_paleta(panel, canvas, panel_desc, tipo="basica"):
    for widget in panel.winfo_children():
        widget.destroy()
    for widget in panel_desc.winfo_children():
        widget.destroy()
    canvas.delete("all")

    dibujar_circulo_cromatico(canvas, radio=100)

    tk.Label(panel, text=f"Paleta {tipo}", font=("Segoe UI", 12, "bold"), bg="#ffffff").pack(pady=5)
    frame_colores = tk.Frame(panel, bg="#ffffff")
    frame_colores.pack(pady=10)

    base = Paleta().base
    colores = ArmoniaColor(base).generar(tipo)

    for i, c in enumerate(colores):
        hex_color = rgb_a_hex(c)
        contenedor = tk.Frame(frame_colores, bg="#ffffff")
        contenedor.grid(row=0, column=i, padx=5, pady=5)
        tk.Label(contenedor, text=hex_color, font=("Segoe UI", 8), bg="#ffffff").pack()
        tk.Label(contenedor, bg=hex_color, width=10, height=2).pack()

    marcar_colores_en_circulo(canvas, colores, radio=100)

    tk.Label(panel_desc, text="Variaciones posibles", font=("Segoe UI", 12, "bold"), bg="#ffffff").pack(pady=5)
    for c in colores:
        r, g, b = c[0]/255.0, c[1]/255.0, c[2]/255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        variantes = [
            colorsys.hls_to_rgb(h, min(1, l*1.2), s),
            colorsys.hls_to_rgb(h, max(0, l*0.8), s),
            colorsys.hls_to_rgb(h, l, min(1, s*1.2)),
            colorsys.hls_to_rgb(h, l, max(0, s*0.8))
        ]

        frame_var = tk.Frame(panel_desc, bg="#ffffff")
        frame_var.pack(pady=5)
        tk.Label(frame_var, text=f"Base {rgb_a_hex(c)}:", font=("Segoe UI", 9, "bold"), bg="#ffffff").pack(side="left", padx=5)
        for v in variantes:
            hex_v = "#%02x%02x%02x" % (int(v[0]*255), int(v[1]*255), int(v[2]*255))
            tk.Label(frame_var, bg=hex_v, width=6, height=2).pack(side="left", padx=3)
            tk.Label(frame_var, text=hex_v, font=("Segoe UI", 7), bg="#ffffff").pack(side="left", padx=3)

# --- Ventana principal ---
def crear_ventana():
    root = tk.Tk()
    root.geometry("800x850")
    root.title("🎨 Generador de Paletas")
    root.configure(bg="#fafafa")

    # Estilo ttk para botones claros
    style = ttk.Style()
    style.configure("TButton",
        font=("Segoe UI", 10),
        padding=6,
        relief="flat",
        background="#f0f0f0",
        foreground="#000000"
    )
    style.map("TButton",
        background=[("active", "#dcdcdc")],
        foreground=[("active", "#000000")]
    )

    # Header
    header = tk.Frame(root, bg="#4a90e2", height=50)
    header.pack(fill="x")
    tk.Label(header, text="Generador de Paletas", font=("Segoe UI", 14, "bold"), fg="white", bg="#4a90e2").pack(pady=10)

    # Canvas cromático
    canvas = tk.Canvas(root, width=300, height=300, bg="#fafafa", highlightthickness=0)
    canvas.pack(pady=20)

    # Panel paleta
    panel_paleta = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
    panel_paleta.pack(fill="x", padx=20, pady=10)

    # Panel descriptivo
    panel_desc = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
    panel_desc.pack(fill="x", padx=20, pady=10)

    # Menú lateral (más abajo, debajo del header)
    menu_frame = tk.Frame(root, bg="#eaeaea", width=180, height=800)
    menu_frame.place(x=-180, y=50)  # ahora empieza en y=50

    tipos = ["basica", "complementaria", "monocromatica", "analogica", "triada", "cuadrado", "separacion", "compuesta", "tonos"]
    for t in tipos:
        ttk.Button(menu_frame, text=t.capitalize(),
                   command=lambda tipo=t: mostrar_paleta(panel_paleta, canvas, panel_desc, tipo)).pack(fill="x", pady=4)

    # Botón hamburguesa
    def toggle_menu():
        x = menu_frame.winfo_x()
        if x < 0:
            menu_frame.place(x=0, y=50)   # mostrar debajo del header
        else:
            menu_frame.place(x=-180, y=50)  # ocultar

    btn_menu = tk.Button(header, text="≡", command=toggle_menu, bg="#4a90e2", fg="white", bd=0, font=("Segoe UI", 14))
    btn_menu.place(x=10, y=10)

    # Paleta inicial
    mostrar_paleta(panel_paleta, canvas, panel_desc, "basica")

    root.mainloop()

if __name__ == "__main__":
    crear_ventana()
