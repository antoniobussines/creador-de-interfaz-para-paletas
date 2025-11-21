# 🎨 Generador de Paletas Cromáticas

Aplicación en **Python + Tkinter** que permite visualizar un círculo cromático, generar paletas de colores según distintos tipos de armonías (análoga, complementaria, tríada, cuadrado, etc.), y mostrar variaciones de intensidad y saturación. Incluye un menú lateral desplegable para seleccionar el tipo de paleta.

---

##  Características

- Visualización de **círculo cromático interactivo**.
- Generación de paletas en distintos esquemas:
  - Básica
  - Complementaria
  - Monocromática
  - Análoga
  - Tríada
  - Cuadrado
  - Separación complementaria
  - Compuesta
  - Tonos
- Cada color se muestra con su **código HEX**.
- **Marcadores en el círculo** para ubicar los colores de la paleta.
- Panel descriptivo con **variaciones de luminosidad y saturación**.
- Menú lateral desplegable estilo moderno.

---
## imagenes
<img width="1917" height="1026" alt="image" src="https://github.com/user-attachments/assets/f1df736a-33fe-4f76-900a-76098f20fc6c" />

<img width="1919" height="1031" alt="image" src="https://github.com/user-attachments/assets/b8c4eaf9-e9dd-4d4c-a821-75e1b07697ec" />

## 🔮 Mejoras futuras

El proyecto actualmente funciona como aplicación de escritorio en **Tkinter**, pero se planean las siguientes mejoras para hacerlo más sólido y accesible:

1. **Editor de interfaces integrado**  
   - Crear un editor visual que permita diseñar y modificar paletas y layouts directamente desde la aplicación.  
   - Implementar funciones de arrastrar y soltar (drag & drop) para organizar elementos.  
   - Exportar configuraciones de interfaz para reutilizarlas en otros proyectos.

2. **Migración a aplicación web**  
   - Reescribir la aplicación utilizando **Django**, por su compatibilidad con Python y facilidad de integración.  
   - Usar **HTML + CSS** para la interfaz, asegurando un diseño moderno y responsivo.  
   - Integrar **JavaScript** para interactividad avanzada en el navegador.  
   - Mantener la lógica de generación de paletas en Python, pero exponerla como servicios web (API REST).

3. **Comodidad general y escalabilidad**  
   - Permitir que los usuarios accedan desde cualquier dispositivo sin necesidad de instalar nada.  
   - Facilitar la colaboración y compartir paletas en línea.  
   - Preparar la base para futuras integraciones con librerías de diseño gráfico o frameworks frontend (ej: React, Vue).

---

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone (https://github.com/antoniobussines/creador-de-interfaz-para-paletas.git
   cd color_palets
   
