from tkinter import *
from tkinter import ttk
import mysql.connector # type: ignore


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Ignorancia"
    )


# FUNCION MOSTRAR

def mostrar_categorias():
    tabla.delete(*tabla.get_children())

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM categoria")

    datos = cursor.fetchall()

    for fila in datos:
        tabla.insert('', END, values=fila)


def guardar_categoria():
    txt_descripcion.delete(0, END)
    mostrar_categorias()


# VENTANA

ventana = Tk()
ventana.title("Categorías")
ventana.geometry("500x400")

Label(ventana, text="Descripción").pack(pady=5)


txt_descripcion = Entry(ventana, width=40)
txt_descripcion.pack()

Button(
    ventana,
    text="Guardar",
    command=guardar_categoria,
    bg="green",
    fg="white"
).pack(pady=10)


# TABLA

tabla = ttk.Treeview(
    ventana,
    columns=("ID", "DESCRIPCION"),
    show='headings'
)


tabla.heading("ID", text="ID")
tabla.heading("DESCRIPCION", text="DESCRIPCION")


tabla.pack(fill=BOTH, expand=True)

mostrar_categorias()

ventana.mainloop()