'''import numpy as np
import tensorflow as tf
import cv2 as cv
import matplotlib.pyplot as plt

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

# Ejemplo de uso
# Suponiendo que tienes una imagen y un kernel definidos previamente
imagen = cv.imread('Clases/Tiger.jpg', 0)
kernel_bordes = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

# Llamar a la función filtro_conv
imagen_filtrada = filtro_conv(imagen, kernel_bordes)

plt.imshow(imagen_filtrada, cmap='gray')
plt.show()'''



import numpy as np
import tkinter as tk
from tkinter import ttk
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import tensorflow as tf

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

def apply_filter():
    # Obtener los valores del kernel desde los cuadros de texto
    kernel_values = []
    for i in range(3):
        row = []
        for j in range(3):
            value = float(entry_widgets[i][j].get())  # Cambiar int a float
            row.append(value)
        kernel_values.append(row)
    
    # Convertir la lista de valores en una matriz NumPy
    kernel = np.array(kernel_values)
    
    # Aplicar el filtro
    imagen_filtrada = filtro_conv(imagen, kernel)
    
    # Mostrar la imagen filtrada en la ventana
    img = Image.fromarray(imagen_filtrada)
    img_tk = ImageTk.PhotoImage(image=img)
    label_image.config(image=img_tk)
    label_image.image = img_tk

# Cargar la imagen
imagen = cv.imread('Clases/Tiger.jpg', 0)

# Crear la ventana
window = tk.Tk()
window.title("Filtro Convolucional")

# Crear cuadros de texto para el kernel
entry_widgets = []
for i in range(3):
    row = []
    for j in range(3):
        entry = ttk.Entry(window, width=8)  # Aumentar el ancho para flotantes
        entry.grid(row=i, column=j)
        row.append(entry)
    entry_widgets.append(row)
    

# Botón para aplicar el filtro
apply_button = ttk.Button(window, text="Aplicar Filtro", command=apply_filter)
apply_button.grid(row=3, columnspan=3)

# Etiqueta para mostrar la imagen filtrada
label_image = ttk.Label(window)
label_image.grid(row=4, columnspan=3)

window.mainloop()
