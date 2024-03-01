import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global pos
pos = '+900+100'

def sharpness(I):
    N, M = I.shape
    gradient = np.gradient(I)
    sharpness_metric = np.sum(np.abs(gradient)) / (N * M)
    return sharpness_metric

def brightness(I):
    N, M = I.shape
    total_sum = np.sum(I)
    brightness_metric = total_sum / (N * M)
    return brightness_metric

def contrast(I):
    N, M = I.shape
    B = brightness(I)
    contrast_metric = np.sum((I - B) ** 2) / (N * M)
    return contrast_metric
    
def histograma_gris(ima):
    global histogram_window
    # Crear ventana de Tkinter
    histogram_window = tk.Tk()
    histogram_window.title("Histograma")
    histogram_window.geometry(pos)

    histogram_window.geometry(f"{616}x{488}")
    
    # Calcular el histograma de la imagen en escala de grises
    hist_values = cv2.calcHist([ima], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

    # Visualizar el histograma
    fig = plt.figure(figsize=(612/96,484/96))
    plt.plot(hist_values, "k")  # "k" para color negro
    plt.title("Histograma de la imagen en escala de grises", fontsize=15)
    plt.xlabel("Niveles de intensidad", fontsize=15)
    plt.ylabel("Frecuencia", fontsize=15)

    # Convertir el gráfico en un widget de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=histogram_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Iniciar el bucle principal de Tkinter
    histogram_window.mainloop()

# Función para cargar y mostrar la imagen seleccionada por el usuario
def cargar_imagen_gris(window,canal=0):
    filename = filedialog.askopenfilename()  # Abre el explorador de archivos para que el usuario seleccione una imagen
    if filename:  # Verifica si se seleccionó un archivo
        image = cv2.imread(filename,canal)  # Lee la imagen con cv2
        mostrar_imagen(image, window)
        histograma_gris(image)

# Función para mostrar la imagen en la ventana
def mostrar_imagen(image, window):
    # Convierte la imagen de BGR a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convierte la imagen en formato PIL
    pil_image = Image.fromarray(image_rgb)
    # Escala la imagen para que se ajuste a la ventana
    pil_image = pil_image.resize((523, 468), Image.ANTIALIAS)
    # Convierte la imagen en formato compatible con Tkinter
    tk_image = ImageTk.PhotoImage(pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=430, y=128)  # Ajusta la posición según sea necesario
    hallar_metricas_gray(image, window)


def hallar_metricas_gray(ima, window):
    # Cálculo de las métricas (esto es un ejemplo, debes reemplazarlo con tu lógica)
    N, M = ima.shape
    contraste = contrast(ima)
    brillo = brightness(ima)
    sharpress = sharpness(ima)
    pos = 330
    # Mostrar las métricas en la ventana
    font_style = ("Barlow", 12)  # Cambia la fuente y el tamaño de letra según lo necesites

    # Mostrar las métricas en la ventana
    contraste_label = tk.Label(window, text=f"Dimensiones: {M} x {N} px", font=font_style)
    contraste_label.place(x=60, y=50+pos)

    contraste_label = tk.Label(window, text=f"Contraste: {contraste:.3f}", font=font_style)
    contraste_label.place(x=60, y=100+pos)

    brillo_label = tk.Label(window, text=f"Brillo: {brillo:.3f} (cd/m²)", font=font_style)
    brillo_label.place(x=60, y=150+pos)

    sharpress_label = tk.Label(window, text=f"Sharpress: {sharpress:.3f}", font=font_style)
    sharpress_label.place(x=60, y=200+pos)