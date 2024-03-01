import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


global pos
pos = '+20+20'

# Función para cargar y mostrar la imagen seleccionada por el usuario
def cargar_imagen_gris_operaciones(window,modo,canal=0):
    filename = filedialog.askopenfilename()  # Abre el explorador de archivos para que el usuario seleccione una imagen
    if filename:  # Verifica si se seleccionó un archivo
        image = cv2.imread(filename,canal)  # Lee la imagen con cv2
        mostrar_imagen(image, window)
        #hallar_operacion(image, window, modo)
        return image


def suma(imag, a):
    suma = imag + a
    return suma

def resta(imag, a):
    resta = imag - a
    return resta

def multiplicacion(imag, a):
    mul = imag * a
    return mul

def division(imag, a):
    div = imag / a
    print(div)
    return div


def operacion_aritmetica(window,imagen,alpha,modo):
    operacion = imagen
    if modo == 1:
        operacion = suma(imagen, int(alpha))
    if modo == 2:
        operacion = resta(imagen, int(alpha))
    if modo == 3:
        operacion = multiplicacion(imagen, alpha)
    if modo == 4:
        operacion = division(imagen, alpha)
    mostrar_imagen(operacion, window)


# Función para mostrar la imagen en la ventana
def mostrar_imagen(image, window):
    # Convierte la imagen de BGR a RGB
    #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convierte la imagen en formato PIL
    pil_image = Image.fromarray(image)
    # Escala la imagen para que se ajuste a la ventana
    pil_image = pil_image.resize((523, 468), Image.ANTIALIAS)
    # Convierte la imagen en formato compatible con Tkinter
    tk_image = ImageTk.PhotoImage(pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=430, y=128)  # Ajusta la posición según sea necesario


def hallar_operacion(ima, window, modo):
    # Cálculo de las métricas (esto es un ejemplo, debes reemplazarlo con tu lógica)
    alpha = 3
    pos = 330
    # Mostrar las métricas en la ventana
    font_style = ("Bungee", 16)  # Cambia la fuente y el tamaño de letra según lo necesites

    # Mostrar en la ventana
    Operacion_label = tk.Label(window, text=f"alpha: {alpha:.3f}", font=font_style)
    Operacion_label.place(x=120, y=190+pos)