import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tensorflow as tf

global pos
pos = '+20+20'

def cargar_imagen_gris_filt(modo=0,canal=0):
    filename = filedialog.askopenfilename()  # Abre el explorador de archivos para que el usuario seleccione una imagen
    if filename:  # Verifica si se seleccionó un archivo
        image = cv2.imread(filename,canal)  # Lee la imagen con cv2
        return image


def convert_array_to_valid_dtype(image_array):
    # Asegurarse de que el tipo de datos sea compatible (por ejemplo, uint8)
    valid_image_array = np.array(image_array, dtype=np.uint8)
    return valid_image_array



def mostrar_imagen_filt(image, window):
    # Convierte la imagen de BGR a RGB
    #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convierte la imagen en formato PIL
    #valid_image_array = convert_array_to_valid_dtype(image)
    pil_image = Image.fromarray(image)
    # Escala la imagen para que se ajuste a la ventana
    pil_image = pil_image.resize((523, 460), Image.ANTIALIAS)
    # Convierte la imagen en formato compatible con Tkinter
    tk_image = ImageTk.PhotoImage(image=pil_image)
    
    # Muestra la imagen en un widget Label
    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image
    image_label.place(x=430, y=150)  # Ajusta la posición según sea necesario

def filtro_conv(imagen, kernel):
    # Convertir la imagen y el kernel a tensores de TensorFlow
    imagen_tensor = tf.convert_to_tensor(imagen, dtype=tf.float32)
    kernel_tensor = tf.convert_to_tensor(kernel, dtype=tf.float32)
    
    # Añadir dimensiones para el lote y el canal
    imagen_tensor = tf.expand_dims(tf.expand_dims(imagen_tensor, axis=0), axis=-1)
    kernel_tensor = tf.expand_dims(tf.expand_dims(kernel_tensor, axis=-1), axis=-1)
    
    # Aplicar el filtro convolucional
    salida = tf.nn.conv2d(input=imagen_tensor, filters=kernel_tensor, strides=1, padding='SAME')
    
    # Quitar las dimensiones del lote y el canal
    salida = tf.squeeze(salida, axis=[0, -1])
    
    # Obtener la imagen filtrada como un array NumPy
    imagen_filtrada = salida.numpy()
    
    return imagen_filtrada

def apply_filter(n,entry_widgets,imag):
    # Obtener los valores del kernel desde los cuadros de texto
    kernel_values = []
    for i in range(n):
        row = []
        for j in range(n):
            value = float(entry_widgets[i][j].get())  # Cambiar int a float
            row.append(value)
        kernel_values.append(row)
    
    # Convertir la lista de valores en una matriz NumPy
    kernel = np.array(kernel_values)
    
    # Aplicar el filtro
    imagen_filtrada = filtro_conv(imag, kernel)
    return imagen_filtrada

def filtFreq(img,filter):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift1 = np.fft.fftshift(dft)
    fshift = dft_shift1 * filter
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
    return img_back