# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:13:16 2024

@author: soad_
"""

import tkinter as tk

def presionar_tecla(tecla):
    texto_actual = pantalla.get()
    if texto_actual == "0":
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, tecla)
    else:
        pantalla.insert(tk.END, tecla)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

ventana = tk.Tk()
ventana.title("Calculadora Básica")

pantalla = tk.Entry(ventana, width=20, font=("Arial", 20), justify="right")
pantalla.grid(row=0, column=0, columnspan=4)

botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (texto, fila, columna) in botones:
    boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 12),
                      command=lambda t=texto: presionar_tecla(t))
    boton.grid(row=fila, column=columna)
    
boton_calcular = tk.Button(ventana, text="Calcular", width=9, height=2, font=("Arial", 12), command=calcular)
boton_calcular.grid(row=5, column=0, columnspan=4)

ventana.mainloop() 