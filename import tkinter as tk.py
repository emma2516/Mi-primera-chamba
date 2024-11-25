import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
    nom=nombre.get()
    messagebox.showinfo("Mensaje", f"Hola {nom} bienvenido al programa")
#crear la ventana principal

    ventana= tk.Tk()
    ventana.title( "Ejemplo de GUI")
    
#CREAR UNA ETIQUETA
    etiqueta= tk.Label(ventana, text="ingresa tu nombre:")
    etiqueta.grid(row=0,column=0,padx=5,pady=10)

#crear una caja de texto (ENTRY)
    nombre=tk.Entry(ventana, width=40)
    nombre.grid(row=0,column=1,padx=5,pady=10)

#crear un boton y asignarle una funcion
    boton=tk.Button(ventana, text="saludar", command=mostrar_mensaje)
    boton.grid(row=1,column=0,padx=2,pady=10)

#iniciar el blucle de eventos
    ventana.mainloop()