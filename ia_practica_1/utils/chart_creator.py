import matplotlib.pyplot as plt
from pathlib import Path
import os

# Crear las imágenes deseadas y luego subirlas a drive de forma publica para poner la url en el markdown

imgs_path = Path.cwd() / "ia_practica_1/imgs"

def create_byb_chart():
    # Datos de la tabla
    tableros = ["2x2", "3x3", "3x5", "5x5", "8x8"]
    tiempos = [0.004, 0.026, 1.770, 5*60, 5*60]
    # caballos = [4, 4, 5, 10, 24]

    # Crear la figura y los ejes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras para el tiempo
    ax1.bar(tableros, tiempos, color='skyblue', alpha=0.7, label="Tiempo (s)")
    # ax1.plot(tableros, tiempos, color='red', marker='o', label="Tiempo (s)")
    ax1.set_xlabel("Tablero")
    ax1.set_ylabel("Tiempo (s)")
    ax1.tick_params(axis='y')
    plt.ylim(0, 3)  # Límite máximo de 3 segundos en el eje Y

    # Crear un segundo eje para la cantidad de caballos
    # ax2 = ax1.twinx()
    # ax2.plot(tableros, caballos, color='red', marker='o', label="Caballos")
    # ax2.set_ylabel("Caballos", color='red')
    # ax2.tick_params(axis='y', labelcolor='red')

    # Títulos y leyenda
    plt.title("Tiempo de ejecución por tamaño de tablero B&B")
    fig.tight_layout()

    # Crear el directorio si no existe
    img_path = imgs_path / "grafico_tiempo_caballos_byb.png"
    os.makedirs(os.path.dirname(img_path), exist_ok=True)

    # Guardar el gráfico como archivo PNG en el directorio actual
    fig.savefig(img_path)

    plt.show()
    
def create_astar_chart():
    # Datos de la tabla
    tableros = ["2x2", "3x3", "3x5", "5x5", "8x8"]
    tiempos = [0.001, 0.003, 0.034, 0.229, 5*60]
    # caballos = [4, 4, 5, 10, 24]

    # Crear la figura y los ejes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras para el tiempo
    ax1.bar(tableros, tiempos, color='salmon', alpha=0.7, label="Tiempo (s)")
    # ax1.plot(tableros, tiempos, color='red', marker='o', label="Tiempo (s)")
    ax1.set_xlabel("Tablero")
    ax1.set_ylabel("Tiempo (s)")
    ax1.tick_params(axis='y')
    plt.ylim(0, 3)  # Límite máximo de 3 segundos en el eje Y

    # Crear un segundo eje para la cantidad de caballos
    # ax2 = ax1.twinx()
    # ax2.plot(tableros, caballos, color='red', marker='o', label="Caballos")
    # ax2.set_ylabel("Caballos", color='red')
    # ax2.tick_params(axis='y', labelcolor='red')

    # Títulos y leyenda
    plt.title("Tiempo de ejecución por tamaño de tablero A*")
    fig.tight_layout()

    # Crear el directorio si no existe
    img_path = imgs_path / "grafico_tiempo_caballos_astar.png"
    os.makedirs(os.path.dirname(img_path), exist_ok=True)

    # Guardar el gráfico como archivo PNG en el directorio actual
    fig.savefig(img_path)

    plt.show()


def create_comparative_chart():
    # Datos de la tabla
    tableros = ["2x2", "3x3", "3x5", "5x5", "8x8"]
    tiempos_bnb = [0.004, 0.026, 1.770, 5*60, 5*60]
    tiempos_astar = [0.001, 0.003, 0.034, 0.229, 5*60]

    # Crear gráfico de barras con límite de 60 segundos en el eje Y
    plt.figure(figsize=(10, 6))
    bar_width = 0.35  # Ancho de las barras
    index = range(len(tableros))

    # Barras para cada algoritmo
    plt.bar([i - bar_width/2 for i in index], tiempos_bnb, bar_width, label='Branch and Bound', color='skyblue')
    plt.bar([i + bar_width/2 for i in index], tiempos_astar, bar_width, label='A*', color='salmon')

    # Etiquetas y título
    plt.xlabel('Tamaño del tablero')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparativa del tiempo de ejecución entre Branch and Bound y A* (máx 3 segundos)')
    plt.xticks(index, tableros)
    plt.ylim(0, 3)  # Límite máximo de 3 segundos en el eje Y
    plt.legend()

    # Crear el directorio si no existe
    img_path = imgs_path / "grafico_tiempo_caballos_bnb_astar.png"
    os.makedirs(os.path.dirname(img_path), exist_ok=True)

    # Guardar el gráfico como archivo PNG en el directorio actual
    plt.savefig(img_path)

    # Mostrar gráfico
    plt.show()


create_byb_chart()
create_astar_chart()
create_comparative_chart()