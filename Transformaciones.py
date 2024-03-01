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

def cargar_imagen_gris_transformacion(modo=0,canal=0):
    filename = filedialog.askopenfilename()  # Abre el explorador de archivos para que el usuario seleccione una imagen
    if filename:  # Verifica si se seleccionó un archivo
        image = cv2.imread(filename,canal)  # Lee la imagen con cv2
        if modo == 1:
            image = negative(image)
        elif modo == 2:
            image = logaritmic(image)
        return image

def negative(r, L=255):
    s = L - 1 - r
    return s

def logaritmic(r, L=255):
    c = L/(np.log(1+L))
    s = c*np.log(1 + r)
    valid_image_array = convert_array_to_valid_dtype(s)
    return valid_image_array

def convert_array_to_valid_dtype(image_array):
    # Asegurarse de que el tipo de datos sea compatible (por ejemplo, uint8)
    valid_image_array = np.array(image_array, dtype=np.uint8)
    return valid_image_array

def mostrar_imagen(image, window):
    # Convierte la imagen de BGR a RGB
    #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convierte la imagen en formato PIL
    valid_image_array = convert_array_to_valid_dtype(image)
    pil_image = Image.fromarray(valid_image_array)
    # Escala la imagen para que se ajuste a la ventana
    pil_image = pil_image.resize((542, 482), Image.ANTIALIAS)
    # Convierte la imagen en formato compatible con Tkinter
    tk_image = ImageTk.PhotoImage(pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=275, y=135)  # Ajusta la posición según sea necesario


def mostrar_imagen_exp(image, window):
    # Convierte la imagen de BGR a RGB
    #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convierte la imagen en formato PIL
    #valid_image_array = convert_array_to_valid_dtype(image)
    pil_image = Image.fromarray(image)
    # Escala la imagen para que se ajuste a la ventana
    pil_image = pil_image.resize((523, 468), Image.ANTIALIAS)
    # Convierte la imagen en formato compatible con Tkinter
    tk_image = ImageTk.PhotoImage(pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=430, y=128)  # Ajusta la posición según sea necesario

def expocial(r,gamma,L=255):
    c = L/(np.log(1+L))
    s = c * (r**gamma)
    return s

def histogram_equalization(img):
    # Calcular el histograma de la imagen original
    hist, bins = np.histogram(img.flatten(), 256, [0,256])
    
    # Calcular la función de distribución acumulativa (CDF)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # Aplicar la ecualización del histograma
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    
    # Mapear los valores de píxeles originales a los valores ecualizados
    img_equalized = cdf[img]
    
    # Calcular el histograma de la imagen ecualizada
    hist_eq, _ = np.histogram(img_equalized.flatten(), 256, [0,256])
    
    return img_equalized, hist, hist_eq


def show_image(img, row, col, modo, window):
    # Crear una nueva figura
    fig = plt.figure(figsize=(5, 4))
    plt.imshow(img, cmap='gray')
    plt.title(f'Imagen {modo}')
    plt.axis('off')

    # Convertir la figura a formato compatible con Tkinter
    fig.tight_layout()
    fig.canvas.draw()
    img = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
    pil_image = img.resize((230, 230), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(image=pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=col, y=row)  # Ajusta la posición según sea necesario


def show_histogram(hist, row, col, modo, window):
    # Crear una nueva figura
    fig = plt.figure(figsize=(5, 4))
    plt.plot(hist, color='blue')
    plt.title(f'Histograma {modo}')
    plt.xlabel('Intensidad de Píxel')
    plt.ylabel('Frecuencia')
    
    # Convertir la figura a formato compatible con Tkinter
    fig.tight_layout()
    fig.canvas.draw()
    img = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
    pil_image = img.resize((230, 230), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(image=pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=col, y=row)  # Ajusta la posición según sea necesario


def hist_loop(img,window):
    posx = 120
    posy = 250
    # Crear un Canvas
    img_equalized, hist, hist_eq = histogram_equalization(img)
    # Mostrar la imagen original y ecualizada
    show_image(img, 50+posx, 50+posy, 'Original', window)
    show_image(img_equalized, 50+posx, 310+posy, 'Ecualizada', window)

    # Mostrar los histogramas original y ecualizado
    show_histogram(hist, 290+posx, 50+posy, 'Orignal', window)
    show_histogram(hist_eq, 290+posx, 310+posy, 'Ecualizada', window)