import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import matplotlib.pylab as plt
import numpy as np
from propiedades import cargar_imagen_gris
from operaciones import cargar_imagen_gris_operaciones, operacion_aritmetica
from Transformaciones import cargar_imagen_gris_transformacion, mostrar_imagen, mostrar_imagen_exp, expocial, hist_loop
from Filtros import cargar_imagen_gris_filt, mostrar_imagen_filt, apply_filter, filtFreq
global pos
pos = '+20+20'
alpha = 0


## Operaciones Aritmeticas

def open_operaciones(modo):
    global alpha_anterior, alpha
    operaciones_gray_window.destroy()  # Cierra la ventana actual
    operaciones_window = tk.Tk()  # Crea una nueva ventana
    operaciones_window.title("Operaciones Aritmeticas")
    operaciones_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Aritmetica/operaciones.GIF")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    operaciones_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(operaciones_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        operaciones_window.destroy()  # Cierra la ventana gris
        main()

    def guardarcargarimagne():
        global imagen
        imagen = cargar_imagen_gris_operaciones(operaciones_window,modo)
        #print(imagen)
    
        # Función para actualizar el valor de alpha
    def update_alpha(value):
        alpha = alpha_slider.get()  # Escala el valor del deslizador al rango de 0 a 1
        # Actualiza el valor de alpha en algún lugar de la interfaz de usuario
        alpha_label.config(text=f"Alpha: {alpha:.2f}")
        #print(imagen,modo)
        operacion_aritmetica(operaciones_window,imagen,alpha,modo)


    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")

    # Botón para cargar la imagen
    cargar_button = tk.Button(operaciones_window, image=background_cargar,
                               command= lambda: guardarcargarimagne(), borderwidth=0)
    cargar_button.pack()
   
    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(operaciones_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    x_exit_button = 322
    y_exit_button = 642

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=48, y=250)  # Ajusta la posición según sea necesario

    # Rango para alpha
    if modo == 1 or modo == 2:
        alpha_min = 0.0
        alpha_max = 255.0
    elif modo == 3 or modo == 4:
        alpha_min = 0
        alpha_max = 5

    
    # Crear estilo ttk para el Scale
    style = ttk.Style()
    style.theme_use('clam')  # Puedes elegir otro tema si prefieres

    # Configurar un estilo personalizado para el Scale
    style.configure("Custom.Horizontal.TScale", troughcolor="#00C8FF", sliderthickness=20)

    # Crear el deslizador
    alpha_slider = ttk.Scale(operaciones_window, from_=alpha_min, to=alpha_max, orient=tk.HORIZONTAL,
                            length=300, style="Custom.Horizontal.TScale",command=update_alpha)
    alpha_slider.place(x=80, y=400)

    # Etiqueta para mostrar el valor de alpha
    # Mostrar las métricas en la ventana
    font_style = ("Barlow", 35)  # Cambia la fuente y el tamaño de letra según lo necesites
    alpha_label = tk.Label(operaciones_window, text="Alpha: 0.00", font=font_style, bg="#00C8FF")
    alpha_label.place(x=80, y=515)  # Ajusta la posición según sea necesario

    operaciones_window.mainloop()


def open_hist():
    transformaciones_gray_window.destroy()  # Cierra la ventana actual
    hist_window = tk.Tk()  # Crea una nueva ventana
    hist_window.title("Transformaciones")
    hist_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/Transformaciones.gif")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    hist_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(hist_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        hist_window.destroy()  # Cierra la ventana gris
        main()

    def guardarcargarimagne():
        global imagen
        imagen = cargar_imagen_gris_transformacion()
        hist_loop(imagen, hist_window)
        #hallar_operacion(image, window, modo)
        #print(imagen)


    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")

    # Botón para cargar la imagen
    cargar_button = tk.Button(hist_window, image=background_cargar,
                               command= lambda: guardarcargarimagne(), borderwidth=0)
    cargar_button.pack()
   
    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(hist_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    x_exit_button = 572
    y_exit_button = 655

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=92, y=655)  # Ajusta la posición según sea necesario

    hist_window.mainloop()


def open_neg_log(modo):
    transformaciones_gray_window.destroy()  # Cierra la ventana actual
    neg_log = tk.Tk()  # Crea una nueva ventana
    neg_log.title("Transformaciones")
    neg_log.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/TransformacionNeg.gif")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    neg_log.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(neg_log, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        neg_log.destroy()  # Cierra la ventana gris
        main()

    def guardarcargarimagne():
        global imagen
        imagen = cargar_imagen_gris_transformacion(modo)
        mostrar_imagen(imagen, neg_log)
        #hallar_operacion(image, window, modo)
        #print(imagen)


    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")

    # Botón para cargar la imagen
    cargar_button = tk.Button(neg_log, image=background_cargar,
                               command= lambda: guardarcargarimagne(), borderwidth=0)
    cargar_button.pack()
   
    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(neg_log, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    x_exit_button = 572
    y_exit_button = 655

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=92, y=655)  # Ajusta la posición según sea necesario

    neg_log.mainloop()


def open_exp():
    global alpha_anterior, alpha
    transformaciones_gray_window.destroy()  # Cierra la ventana actual
    exp_window = tk.Tk()  # Crea una nueva ventana
    exp_window.title("Transformacion Exp")
    exp_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Aritmetica/operaciones.GIF")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    exp_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(exp_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        exp_window.destroy()  # Cierra la ventana gris
        main()

    def guardarcargarimagne():
        global imagen
        imagen = cargar_imagen_gris_transformacion()
        mostrar_imagen_exp(imagen, exp_window)
        #print(imagen)
    
        # Función para actualizar el valor de alpha
    def update_alpha(value):
        alpha = alpha_slider.get()  # Escala el valor del deslizador al rango de 0 a 1
        # Actualiza el valor de alpha en algún lugar de la interfaz de usuario
        alpha_label.config(text=f"Alpha: {alpha:.2f}")
        s = expocial(imagen,alpha)
        mostrar_imagen_exp(s, exp_window)

    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")

    # Botón para cargar la imagen
    cargar_button = tk.Button(exp_window, image=background_cargar,
                               command= lambda: guardarcargarimagne(), borderwidth=0)
    cargar_button.pack()
   
    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(exp_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    x_exit_button = 322
    y_exit_button = 642

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=48, y=250)  # Ajusta la posición según sea necesario

    # Rango para alpha

    alpha_min = 0.0
    alpha_max = 30

    # Crear estilo ttk para el Scale
    style = ttk.Style()
    style.theme_use('clam')  # Puedes elegir otro tema si prefieres

    # Configurar un estilo personalizado para el Scale
    style.configure("Custom.Horizontal.TScale", troughcolor="#00C8FF", sliderthickness=20)

    # Crear el deslizador
    alpha_slider = ttk.Scale(exp_window, from_=alpha_min, to=alpha_max, orient=tk.HORIZONTAL,
                            length=300, style="Custom.Horizontal.TScale",command=update_alpha)
    alpha_slider.place(x=80, y=400)

    # Etiqueta para mostrar el valor de alpha
    # Mostrar las métricas en la ventana
    font_style = ("Barlow", 35)  # Cambia la fuente y el tamaño de letra según lo necesites
    alpha_label = tk.Label(exp_window, text="Alpha: 0.00", font=font_style, bg="#00C8FF")
    alpha_label.place(x=80, y=515)  # Ajusta la posición según sea necesario

    exp_window.mainloop()


def conv_gray():
    filtros_window.destroy()  # Cierra la ventana actual
    conv_window = tk.Tk()  # Crea una nueva ventana
    conv_window.title("Convolucion 2D")
    conv_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Filtros/Conv.gif")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    conv_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(conv_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        conv_window.destroy()  # Cierra la ventana gris
        main()

    def guardarcargarimagne():
        global imagen
        imagen = cargar_imagen_gris_filt(conv_window)
        mostrar_imagen_filt(imagen,conv_window)
        #print(imagen)

    def definirn(n):
        global entry_widgets, value
        value = int(n.get())
        # Crear cuadros de texto para el kernel
        entry_widgets = []
        for i in range(value):
            row = []
            for j in range(value):
                entry = ttk.Entry(conv_window, width=8)  # Aumentar el ancho para flotantes
                entry.place(x=90 + j * (280/value), y=365 + i * (150/value))  # Ajusta las coordenadas según sea necesario
                row.append(entry)
            entry_widgets.append(row)

    def aplicarfiltro():
        imagen_filtrada = apply_filter(value,entry_widgets,imagen)
        mostrar_imagen_filt(imagen_filtrada,conv_window)

    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")
    background_kernel = tk.PhotoImage(file='C:/InterfazGrafica/PARCIAL/Gris/Filtros/APLICARFILTRO.png')
    background_n = tk.PhotoImage(file='C:/InterfazGrafica/PARCIAL/Gris/Filtros/nkernel.png')

    # Botón para cargar la imagen
    cargar_button = tk.Button(conv_window, image=background_cargar, command=guardarcargarimagne, borderwidth=0)
    cargar_button.grid(row=0, column=0)

    # Aplicar kernel
    kernel_button = tk.Button(conv_window, image=background_kernel,command=lambda: aplicarfiltro(), borderwidth=0)
    kernel_button.grid(row=1, column=0)

    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(conv_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.grid(row=2, column=0)


    n = ttk.Entry(conv_window, width=8)
    n.place(x=80,y=672)

    # Boton "Elegir n"
    n_kernel_button = tk.Button(conv_window, image=background_n, command=lambda: definirn(n), borderwidth=0)
    n_kernel_button.grid(row=3, column=0)

    x_exit_button = 500
    y_exit_button = 642

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=48, y=230)  # Ajusta la posición según sea necesario
    kernel_button.place(x= 80, y=525)
    n_kernel_button.place(x=150,y=642)

    conv_window.mainloop()


def freq_gray():
    filtros_window.destroy()  # Cierra la ventana actual
    freq_window = tk.Tk()  # Crea una nueva ventana
    freq_window.title("Filtro en frecuencia")
    freq_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Filtros/Conv.gif")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    freq_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(freq_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        freq_window.destroy()  # Cierra la ventana gris
        main()

    def guardarcargarimagne():
        global imagen
        imagen = cargar_imagen_gris_filt(freq_window)
        mostrar_imagen_filt(imagen,freq_window)
        #print(imagen)

    def definirn(n):
        global D_0
        D_0 = float(n.get())
    
    def crearfiltro(tipo):
        global filter
        rows, cols = imagen.shape
        crow, ccol = rows//2 , cols//2     # center
        if tipo == 0: #HPF
            filter = np.ones((rows, cols, 2), np.float32)
            
        else:
            filter = np.zeros((rows, cols, 2), np.float32)
        
        center = [crow, ccol]
        x, y = np.ogrid[:rows, :cols]
        filter_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= D_0 * D_0
        if tipo == 0:
            filter[filter_area] = 0
        else:
            filter[filter_area] = 1

    def aplicarfiltro():
        img_back = filtFreq(imagen,filter)
        img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
        img_back = img_back.astype(np.uint8)
        mostrar_imagen_filt(img_back,freq_window)


    # Icones del boton
    background_HFP = tk.PhotoImage(file='C:/InterfazGrafica/PARCIAL/Gris/Filtros/HFP.png')
    background_LFP = tk.PhotoImage(file='C:/InterfazGrafica/PARCIAL/Gris/Filtros/LFP.png')
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")
    background_kernel = tk.PhotoImage(file='C:/InterfazGrafica/PARCIAL/Gris/Filtros/APLICARFILTRO.png')
    background_n = tk.PhotoImage(file='C:/InterfazGrafica/PARCIAL/Gris/Filtros/Radio.png')

    # Botón para cargar la imagen
    cargar_button = tk.Button(freq_window, image=background_cargar, command=guardarcargarimagne, borderwidth=0)
    cargar_button.grid(row=0, column=0)

    # Aplicar kernel
    kernel_button = tk.Button(freq_window, image=background_kernel,command=lambda: aplicarfiltro(), borderwidth=0)
    kernel_button.grid(row=1, column=0)

    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(freq_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.grid(row=2, column=0)

    # Botones para elegir filtro
    HFP_button = tk.Button(freq_window, image=background_HFP, command=lambda: crearfiltro(0), borderwidth=0)
    HFP_button.grid(row=3,column=0)
    LPF_button = tk.Button(freq_window, image=background_LFP, command=lambda: crearfiltro(1), borderwidth=0)
    LPF_button.grid(row=4, column=0)

    n = ttk.Entry(freq_window, width=8)
    n.place(x=80,y=672)

    # Boton "Elegir n"
    n_kernel_button = tk.Button(freq_window, image=background_n, command=lambda: definirn(n), borderwidth=0)
    n_kernel_button.grid(row=3, column=0)

    x_exit_button = 500
    y_exit_button = 642

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=48, y=230)  # Ajusta la posición según sea necesario
    kernel_button.place(x= 80, y=525)
    n_kernel_button.place(x=150,y=642)
    HFP_button.place(x=130,y=440)
    LPF_button.place(x=130,y=370)


    freq_window.mainloop()

## Funciones de imagenes grises

def open_gray_propiedades():
    gray_window.destroy()  # Cierra la ventana actual
    propiedades_gray_window = tk.Tk()  # Crea una nueva ventana
    propiedades_gray_window.title("Operaciones Aritmeticas")
    propiedades_gray_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Propiedades/propiedadesimagen.GIF")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    propiedades_gray_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(propiedades_gray_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        propiedades_gray_window.destroy()  # Cierra la ventana gris
        main()
    

    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_cargar = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Propiedades/Cargarimagen.png")

    # Botón para cargar la imagen
    cargar_button = tk.Button(propiedades_gray_window, image=background_cargar,
                               command=lambda: cargar_imagen_gris(propiedades_gray_window), borderwidth=0)
    cargar_button.pack()
   
    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(propiedades_gray_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    x_exit_button = 322
    y_exit_button = 642

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    cargar_button.place(x=48, y=250)  # Ajusta la posición según sea necesario


    propiedades_gray_window.mainloop()


def open_gray_operaciones():
    global operaciones_gray_window
    gray_window.destroy()  # Cierra la ventana actual
    operaciones_gray_window = tk.Tk()  # Crea una nueva ventana
    operaciones_gray_window.title("Operaciones Aritmeticas")
    operaciones_gray_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Aritmetica/Pantalla.GIF")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    operaciones_gray_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(operaciones_gray_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        operaciones_gray_window.destroy()  # Cierra la ventana gris
        main()
    
    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_adiccion = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Aritmetica/ADICCION.png")
    background_subtraccion = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Aritmetica/SUBTRACCION.png")
    background_producto = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Aritmetica/PRODUCTO.png")
    background_division = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/Aritmetica/DIVISION.png")


    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(operaciones_gray_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    # Botónes para usar funciones
    adiccion_button = tk.Button(operaciones_gray_window, image=background_adiccion, command=lambda: open_operaciones(1), borderwidth=0)
    adiccion_button.pack()
    subtraccion_button = tk.Button(operaciones_gray_window, image=background_subtraccion, command=lambda: open_operaciones(2), borderwidth=0)
    subtraccion_button.pack()
    producto_button = tk.Button(operaciones_gray_window, image=background_producto, command=lambda: open_operaciones(3), borderwidth=0)
    producto_button.pack()
    division_button = tk.Button(operaciones_gray_window, image=background_division, command=lambda: open_operaciones(4), borderwidth=0)
    division_button.pack()

    x_exit_button = 322
    y_exit_button = 642

    a_x = 560
    a_y = 420
    b_x = 80
    b_y = 300
    x_adiccion_button = b_x
    y_adiccion_button = b_y
    x_subtraccion_button = b_x
    y_subtraccion_button = a_y
    x_producto_button = a_x
    y_producto_button = b_y
    x_division_button = a_x
    y_division_button = a_y

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    adiccion_button.place(x=x_adiccion_button, y=y_adiccion_button)
    subtraccion_button.place(x=x_subtraccion_button,y=y_subtraccion_button)
    producto_button.place(x=x_producto_button,y=y_producto_button)
    division_button.place(x=x_division_button,y=y_division_button)


    operaciones_gray_window.mainloop()


def open_gray_transformaciones():
    global transformaciones_gray_window
    gray_window.destroy()  # Cierra la ventana actual
    transformaciones_gray_window = tk.Tk()  # Crea una nueva ventana
    transformaciones_gray_window.title("Transformaciones en grices")
    transformaciones_gray_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/Transformaciones.gif")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    transformaciones_gray_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(transformaciones_gray_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        transformaciones_gray_window.destroy()  # Cierra la ventana gris
        main()
    
    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_negativo = tk.PhotoImage(file="C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/Negativo.png")
    background_exp = tk.PhotoImage(file="C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/Exp.png")
    background_log = tk.PhotoImage(file="C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/Log.png")
    background_hist = tk.PhotoImage(file="C:/InterfazGrafica/PARCIAL/Gris/Transformaciones/Hist.png")


    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(transformaciones_gray_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    # Botónes para usar funciones
    negativo_button = tk.Button(transformaciones_gray_window, image=background_negativo, command=lambda: open_neg_log(1), borderwidth=0)
    negativo_button.pack()
    exp_button = tk.Button(transformaciones_gray_window, image=background_exp, command=lambda: open_exp(), borderwidth=0)
    exp_button.pack()
    log_button = tk.Button(transformaciones_gray_window, image=background_log, command=lambda: open_neg_log(2), borderwidth=0)
    log_button.pack()
    hist_button = tk.Button(transformaciones_gray_window, image=background_hist, command=lambda: open_hist(), borderwidth=0)
    hist_button.pack()

    x_exit_button = 322
    y_exit_button = 642

    a_x = 560
    a_y = 420
    b_x = 80
    b_y = 300
    x_adiccion_button = b_x
    y_adiccion_button = b_y
    x_subtraccion_button = b_x
    y_subtraccion_button = a_y
    x_producto_button = a_x
    y_producto_button = b_y
    x_division_button = a_x
    y_division_button = a_y

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    negativo_button.place(x=x_adiccion_button, y=y_adiccion_button)
    exp_button.place(x=x_subtraccion_button,y=y_subtraccion_button)
    log_button.place(x=x_producto_button,y=y_producto_button)
    hist_button.place(x=x_division_button,y=y_division_button)


    transformaciones_gray_window.mainloop()


def open_gray_filtros():
    global filtros_window
    gray_window.destroy()  # Cierra la ventana actual
    filtros_window = tk.Tk()  # Crea una nueva ventana
    filtros_window.title("Filtro de imagenes")
    filtros_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/Filtros/filtros.gif")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    filtros_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(filtros_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo

        # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        filtros_window.destroy()  # Cierra la ventana gris
        main()
    
    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_filt = tk.PhotoImage(file="C:/InterfazGrafica/PARCIAL/Gris/Filtros/CONVO.png")
    background_freq = tk.PhotoImage(file="C:/InterfazGrafica/PARCIAL/Gris/Filtros/FRECUENCIAL.png")


    # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(filtros_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    # Botónes para usar funciones
    filt_button = tk.Button(filtros_window, image=background_filt, command=lambda: conv_gray(), borderwidth=0)
    filt_button.pack()
    freq_button = tk.Button(filtros_window, image=background_freq, command=lambda: freq_gray(), borderwidth=0)
    freq_button.pack()

    x_exit_button = 322
    y_exit_button = 642

    a_x = 568
    b_x = 90
    b_y = 360

    x_adiccion_button = b_x
    y_adiccion_button = b_y
    x_producto_button = a_x
    y_producto_button = b_y

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    filt_button.place(x=x_adiccion_button, y=y_adiccion_button)
    freq_button.place(x=x_producto_button,y=y_producto_button)



    filtros_window.mainloop()


## Pantallas principales

def open_gray_window():
    global gray_window
    root.destroy()  # Cierra la ventana actual
    gray_window = tk.Tk()  # Crea una nueva ventana
    gray_window.title("Ventana Gris")
    gray_window.geometry(pos)  # Establece la posición en la pantalla
    
    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/Gris/PantallaGris.GIF")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    gray_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(gray_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo
    

    # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        gray_window.destroy()  # Cierra la ventana gris
        main()

    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")
    background_filtros = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/FILTROS.png")
    background_operaciones = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/OPERACIONES.png")
    background_propiedades = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/PROPIEDADES.png")
    background_transformaciones = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/TRANSFORMACIONES.png")


     # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(gray_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()
     # Botónes para usar funciones
    filtro_button = tk.Button(gray_window, image=background_filtros, command=open_gray_filtros, borderwidth=0)
    filtro_button.pack()
    operaciones_button = tk.Button(gray_window, image=background_operaciones, command=open_gray_operaciones, borderwidth=0)
    operaciones_button.pack()
    propiedades_button = tk.Button(gray_window, image=background_propiedades, command=open_gray_propiedades, borderwidth=0)
    propiedades_button.pack()
    transformaciones_button = tk.Button(gray_window, image=background_transformaciones, command=open_gray_transformaciones, borderwidth=0)
    transformaciones_button.pack()

    # Calcular coordenadas en porcentajes relativos al tamaño de la imagen
    x_exit_button = 322
    y_exit_button = 642
    
    a_x = 560
    a_y = 420
    b_x = 80
    b_y = 300
    x_filtro_button = a_x
    y_filtro_button = a_y
    x_operaciones_button = a_x
    y_operaciones_button = b_y
    x_propiedades_button = b_x
    y_propiedades_button = b_y
    x_transformaciones_button = b_x
    y_transformaciones_button = a_y

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    filtro_button.place(x=x_filtro_button, y=y_filtro_button)
    operaciones_button.place(x=x_operaciones_button,y=y_operaciones_button)
    propiedades_button.place(x=x_propiedades_button,y=y_propiedades_button)
    transformaciones_button.place(x=x_transformaciones_button,y=y_transformaciones_button)

    gray_window.mainloop()


def open_color_window():
    global color_window
    root.destroy()  # Cierra la ventana actual
    color_window = tk.Tk()  # Crea una nueva ventana
    color_window.title("Ventana de Color")
    color_window.geometry(pos)  # Establece la posición en la pantalla

    # Carga de la imagen de fondo
    bg_image = Image.open("C:/InterfazGrafica/PARCIAL/NOHABILITADO.GIF")  # Reemplaza "gray_background.jpg" con el nombre de tu imagen
    color_window.geometry(f"{1024}x{768}")  # Establece el tamaño de la ventana
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    
    # Coloca la imagen como fondo en la ventana
    bg_label = tk.Label(color_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo
    

    # Definir la función para cerrar la ventana gris y volver al main
    def return_to_main():
        color_window.destroy()  # Cierra la ventana gris
        main()
    # Icones del boton
    background_exit = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/Gris/BOTONES/EXIT.png")

     # Botón "Exit" para cerrar la ventana gris y volver al main
    exit_button = tk.Button(color_window, image=background_exit, command=return_to_main, borderwidth=0)
    exit_button.pack()

    # Calcular coordenadas en porcentajes relativos al tamaño de la imagen
    x_exit_button = 322
    y_exit_button = 642

    # Colocar el botón "Exit" en las coordenadas calculadas
    exit_button.place(x=x_exit_button, y=y_exit_button)
    
    color_window.mainloop()


def main():
    global root
    root = tk.Tk()
    root.title("Preprocesamiento de Imagenes Digitales")
    root.geometry(pos)

    imagepath = "C:/InterfazGrafica/PARCIAL/PantallaInicio/PantallaInicio.jpg"
    image = Image.open(imagepath)
    image = image.resize((1024, 768))
    photo_image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo_image)
    label.photo = photo_image  # Mantener una referencia a la imagen para evitar que se elimine
    label.pack()


    # Icones del boton
    background_image_gris = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/PantallaInicio/ImagenGris.png")
    background_image_color = tk.PhotoImage(file="C:/InterfazGrafica/Parcial/PantallaInicio/ImagenColor.png")
    # Crear botones con imagen de fondo
    gray_button = tk.Button(root, image=background_image_gris, command=open_gray_window, borderwidth=0)
    color_button = tk.Button(root, image=background_image_color, command=open_color_window, borderwidth=0)

    # Calcular coordenadas en píxeles
    x_gray_button = 110
    y_gray_button = 590
    x_color_button = 560
    y_color_button = 590

    # Colocar los botones en las coordenadas calculadas
    gray_button.place(x=x_gray_button, y=y_gray_button)
    color_button.place(x=x_color_button, y=y_color_button)

    root.mainloop()


if __name__ == "__main__":
    main()
