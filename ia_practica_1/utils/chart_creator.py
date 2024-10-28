import matplotlib.pyplot as plt
from pathlib import Path
import os

# Crear las imágenes deseadas y luego subirlas a drive de forma publica para poner la url en el markdown

imgs_path = Path.cwd() / "ia_practica_1/imgs"

def create_byb_chart():
    # Datos de la tabla
    tableros = ["2x2", "3x3", "3x5", "5x5", "8x8"]
    tiempos = [0.000, 0.008, 0.040, 0.315, 7.134]
    # caballos = [4, 4, 5, 10, 24]

    # Crear la figura y los ejes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras para el tiempo
    ax1.bar(tableros, tiempos, color='blue', alpha=0.7, label="Tiempo (s)")
    # ax1.plot(tableros, tiempos, color='red', marker='o', label="Tiempo (s)")
    ax1.set_xlabel("Tablero")
    ax1.set_ylabel("Tiempo (s)", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Crear un segundo eje para la cantidad de caballos
    # ax2 = ax1.twinx()
    # ax2.plot(tableros, caballos, color='red', marker='o', label="Caballos")
    # ax2.set_ylabel("Caballos", color='red')
    # ax2.tick_params(axis='y', labelcolor='red')

    # Títulos y leyenda
    plt.title("Tiempo de ejecución por tamaño de tablero")
    fig.tight_layout()

    # Crear el directorio si no existe
    img_path = imgs_path / "grafico_tiempo_caballos_byb.png"
    os.makedirs(os.path.dirname(img_path), exist_ok=True)

    # Guardar el gráfico como archivo PNG en el directorio actual
    fig.savefig(img_path)

    plt.show()

create_byb_chart()