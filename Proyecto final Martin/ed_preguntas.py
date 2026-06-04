from tkinter import *
from tkinter import ttk
import sqlite3

def conectar():
    return sqlite3.connect("preguntas.db")

def cargar_categorias():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT DESCRIPCION FROM categoria")

    datos = cursor.fetchall()

    lista = []

    for fila in datos:
        lista.append(fila[0])

    combo_categoria['values'] = lista


# ---------------- VENTANA ----------------

ventana = Tk()
ventana.title("Preguntas")
ventana.geometry("700x650")
ventana.config(bg="white")

# ---------------- PREGUNTA ----------------

Label(
    ventana,
    text="Pregunta",
    font=("Arial",14,"bold"),
    bg="white"
).pack(pady=5)

txt_pregunta = Entry(
    ventana,
    width=60,
    font=("Arial",12)
)

txt_pregunta.pack(pady=10)

# ---------------- OPCION 1 ----------------

Label(
    ventana,
    text="Opción 1",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=5)

txt_op1 = Entry(
    ventana,
    width=45,
    font=("Arial",12)
)

txt_op1.pack(pady=10)

# ---------------- OPCION 2 ----------------

Label(
    ventana,
    text="Opción 2",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=5)

txt_op2 = Entry(
    ventana,
    width=45,
    font=("Arial",12)
)

txt_op2.pack(pady=10)

# ---------------- OPCION 3 ----------------

Label(
    ventana,
    text="Opción 3",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=5)

txt_op3 = Entry(
    ventana,
    width=45,
    font=("Arial",12)
)

txt_op3.pack(pady=10)

# ---------------- OPCION 4 ----------------

Label(
    ventana,
    text="Opción 4",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=5)

txt_op4 = Entry(
    ventana,
    width=45,
    font=("Arial",12)
)

txt_op4.pack(pady=10)

# ---------------- RESPUESTA CORRECTA ----------------

Label(
    ventana,
    text="Respuesta correcta (1-4)",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=5)

txt_correcto = Entry(
    ventana,
    width=10,
    font=("Arial",12)
)

txt_correcto.pack(pady=10)

# ---------------- CATEGORIA ----------------

Label(
    ventana,
    text="Categoría",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=5)

combo_categoria = ttk.Combobox(
    ventana,
    font=("Arial",12),
    width=30
)

combo_categoria.pack(pady=10)

# ---------------- BOTONES CON SEPARACION ----------------

btn1 = Button(
    ventana,
    text="Opción 1",
    bg="blue",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

btn1.pack(pady=10)

btn2 = Button(
    ventana,
    text="Opción 2",
    bg="blue",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

btn2.pack(pady=10)

btn3 = Button(
    ventana,
    text="Opción 3",
    bg="blue",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

btn3.pack(pady=10)

btn4 = Button(
    ventana,
    text="Opción 4",
    bg="blue",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)

btn4.pack(pady=10)

# ---------------- GUARDAR ----------------

def guardar_pregunta():
    pass

Button(
    ventana,
    text="Guardar Pregunta",
    command=guardar_pregunta,
    bg="green",
    fg="white",
    font=("Arial",12,"bold")
).pack(pady=20)

# ---------------- CARGAR CATEGORIAS ----------------


cargar_categorias()

ventana.mainloop()