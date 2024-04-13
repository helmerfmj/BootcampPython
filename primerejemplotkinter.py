# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:01:03 2024

@author: soad_
"""

import tkinter as tk

def imprimir_mensaje():
    print("Hola desde Tkinter!")
    
ventana = tk.Tk()

ventana.title("Ejemplo de Tkinter")
ventana.geometry("400x300")
boton = tk.Button(ventana, text="Haz click", command=imprimir_mensaje)
boton.pack(pady=20)

ventana.mainloop()