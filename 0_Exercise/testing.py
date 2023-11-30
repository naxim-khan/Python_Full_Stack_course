1
42 34
5678
from tkinter import * from tkinter import ttk import tkinter as tk import pymysql
from conexion import *
from tkinter import messagebox from PIL import Image, ImageTk from iniciar sesion import Login
def __init__(self):
self.root = Tk()
self.root.title("StockMaster")
9
10
class Aplicacion Inventario:
self.root.geometry("400x500") #Bloquear agrandar ventana self.root.resizable(0,0)
self.wtotal = self.root.winfo_screenwidth() self.htotal = self.root.winfo_screenheight()
# Guardamos el largo y alto de la ventana self.wventana = 400
self.hventana = 500
# # Aplicamos la siguiente formula para calcular donde debería posicionarse
self.pwidth = round(self.wtotal/2-self.wventana/2)
26
self.pheight
=
round(self.htotal/2-self.hventana/2)

# Se lo aplicamos a la geometría de la ventana
self.root.geometry(str(self.wventana)+"x"+str(self.hventana)+"+"+str(self.pwidth)+"+"+str(self.pheight))

self.imagen =
Image.open("src/logo.png")
self.imagen = self.imagen.resize((350, 100)) # Opcional: Redimensionar la imagen
self.imagen ImageTk. PhotoImage(self.imagen)
# Crear un widget Label con la imagen y colocarlo en la ventana
self.label_imagen = tk. Label(self.root, image=self.imagen)
self.label_imagen.pack(pady=20)

self.login1
=
Login(self)
38
39
40
41
#fetch_data_button = tk.Button(self.root, text="Obtener Datos", command=self.mostrar2) #fetch_data_button.pack()
23
42
43
44
45
self.root.mainloop()
46 AplicacionInventario()