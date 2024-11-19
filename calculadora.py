import tkinter as tk
from tkinter import messagebox

# Función para agregar números y operaciones en la pantalla
def click(boton):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(boton))

# Función para limpiar la pantalla
def clear():
    entrada.delete(0, tk.END)

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())  # Evalúa la expresión ingresada
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except ZeroDivisionError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error: División entre 0")
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Aplicar colores y tamaño a la ventana
ventana.configure(bg="#2C3E50")  # Fondo oscuro
ventana.geometry("350x500")  # Tamaño de la ventana

# Crear el campo de entrada para mostrar los números y el resultado
entrada = tk.Entry(ventana, width=17, borderwidth=5, font=('Arial', 24), justify='right', bg="#ECF0F1")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Crear los botones de la calculadora
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Diccionario de colores
colores_botones = {
    'num': "#2980B9",  # Botones de números
    'op': "#E74C3C",   # Botones de operaciones
    'clear': "#F39C12", # Botón de clear
    'igual': "#27AE60"  # Botón de igual
}

# Crear un ciclo para posicionar los botones en una cuadrícula
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  bg=colores_botones['igual'], fg="white", command=calcular).grid(row=fila, column=columna)
    elif boton == 'C':
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  bg=colores_botones['clear'], fg="white", command=clear).grid(row=fila, column=columna)
    elif boton in ['+', '-', '*', '/']:
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  bg=colores_botones['op'], fg="white", command=lambda b=boton: click(b)).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  bg=colores_botones['num'], fg="white", command=lambda b=boton: click(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Iniciar el bucle principal de la ventana
ventana.mainloop()
