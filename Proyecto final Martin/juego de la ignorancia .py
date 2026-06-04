from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# ---------------- CONEXION MYSQL ----------------

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ignorancia"
)

cursor = conexion.cursor()

# ---------------- VENTANA ----------------

ventana = Tk()
ventana.title("Juego de la Ignorancia")
ventana.geometry("1200x700")
ventana.config(bg="black")

# ---------------- VARIABLES ----------------

turno = 1

x1 = 20
x2 = 20
x3 = 20
x4 = 20

correcta = 0

preguntas_usadas = []

# ---------------- PUNTOS ----------------

puntos1 = 0
puntos2 = 0
puntos3 = 0
puntos4 = 0

victorias1 = 0
victorias2 = 0
victorias3 = 0
victorias4 = 0

ronda = 1
tiempo = 20
cronometro_activo = False

# ---------------- CARGAR PREGUNTA ----------------

cronometro_id = None

def actualizar_cronometro():
    global tiempo
    global cronometro_id

    lbl_tiempo.config(text=f"Tiempo: {tiempo}")

    if tiempo > 0:
        tiempo -= 1
        cronometro_id = ventana.after(1000, actualizar_cronometro)
    else:
        cronometro_id = None
        messagebox.showerror(
            "TIEMPO AGOTADO",
            "Se acabó el tiempo"
        )
        verificar_tiempo()

def cargar_pregunta(event=None):
    global tiempo
    global cronometro_activo
    global cronometro_id
    global correcta
    global preguntas_usadas

    if cronometro_id:
        ventana.after_cancel(cronometro_id)

    tiempo = 20
    cronometro_activo = True

    categoria = combo.get()

    categorias = {
        "Geografía": 1,
        "Historia": 2,
        "Matemáticas": 3,
        "Ciencia": 4,
        "Literatura": 5,
        "Deportes": 6,
        "Tecnología": 7,
        "Arte": 8,
        "Música": 9,
        "Cultura General": 10
    }

    id_categoria = categorias[categoria]

    consulta = """
    SELECT
    ID_PREGUNTA,
    PREGUNTA,
    OPCION1,
    OPCION2,
    OPCION3,
    OPCION4,
    CORRECTO
    FROM pregunta
    WHERE ID_CATEGORIA = %s
    """

    if preguntas_usadas:

        ids = ",".join(str(x) for x in preguntas_usadas)

        consulta += f" AND ID_PREGUNTA NOT IN ({ids})"

    consulta += " ORDER BY RAND() LIMIT 1"

    cursor.execute(consulta, (id_categoria,))

    fila = cursor.fetchone()

    if fila:

        preguntas_usadas.append(fila[0])

        lbl_pregunta.config(text=fila[1])

        botones[0].config(text=fila[2])
        botones[1].config(text=fila[3])
        botones[2].config(text=fila[4])
        botones[3].config(text=fila[5])

        correcta = fila[6] - 1

    else:

        messagebox.showinfo(
            "FIN",
            "Ya no hay más preguntas de esta categoría"
        )

    actualizar_cronometro()



def seleccionar_categoria(event):

    preguntas_usadas.clear()

    cargar_pregunta()

# ---------------- SIGUIENTE TURNO ----------------

def siguiente_turno():

    global turno

    turno += 1

    if turno > 3:
        turno = 1

    lbl_turno.config(
        text="Jugador " + str(turno)
    )

    cargar_pregunta()

# ---------------- MOVER MOTOS ----------------

def mover_moto():

    global turno
    global x1, x2, x3, x4
    global puntos1, puntos2, puntos3, puntos4
    global victorias1, victorias2, victorias3, victorias4
    global ronda

    if turno == 1:

        x1 += 80
        puntos1 += 10

        moto1.place(x=x1, y=250)

        lbl_p1.config(
            text=f"J1 Puntos: {puntos1} | Victorias: {victorias1}"
        )

        if x1 >= 1000:

            victorias1 += 1

            lbl_p1.config(
                text=f"J1 Puntos: {puntos1} | Victorias: {victorias1}"
            )

            messagebox.showinfo(
                "GANADOR",
                "Jugador 1 gana la ronda"
            )

            ronda += 1
            lbl_ronda.config(text=str(ronda))

            reiniciar()

    elif turno == 2:

        x2 += 80
        puntos2 += 10

        moto2.place(x=x2, y=350)

        lbl_p2.config(
            text=f"J2 Puntos: {puntos2} | Victorias: {victorias2}"
        )

        if x2 >= 1000:

            victorias2 += 1

            lbl_p2.config(
                text=f"J2 Puntos: {puntos2} | Victorias: {victorias2}"
            )

            messagebox.showinfo(
                "GANADOR",
                "Jugador 2 gana la ronda"
            )

            ronda += 1
            lbl_ronda.config(text=str(ronda))

            reiniciar()

    elif turno == 3:

        x3 += 80
        puntos3 += 10

        moto3.place(x=x3, y=450)

        lbl_p3.config(
            text=f"J3 Puntos: {puntos3} | Victorias: {victorias3}"
        )

        if x3 >= 1000:

            victorias3 += 1

            lbl_p3.config(
                text=f"J3 Puntos: {puntos3} | Victorias: {victorias3}"
            )

            messagebox.showinfo(
                "GANADOR",
                "Jugador 3 gana la ronda"
            )

            ronda += 1
            lbl_ronda.config(text=str(ronda))

            reiniciar()

    elif turno == 4:

        x4 += 80
        puntos4 += 10

        moto4.place(x=x4, y=550)

        lbl_p4.config(
            text=f"J4 Puntos: {puntos4} | Victorias: {victorias4}"
        )

        if x4 >= 1000:

            victorias4 += 1

            lbl_p4.config(
                text=f"J4 Puntos: {puntos4} | Victorias: {victorias4}"
            )

            messagebox.showinfo(
                "GANADOR",
                "Jugador 4 gana la ronda"
            )

            ronda += 1
            lbl_ronda.config(text=str(ronda))

            reiniciar()

    siguiente_turno()

# ---------------- VERIFICAR ----------------

def verificar(indice):

    global x4
    global puntos4
    global victorias4
    global ronda

    respuestas = [
        botones[0]["text"],
        botones[1]["text"],
        botones[2]["text"],
        botones[3]["text"]
    ]

    if indice == correcta:

        mensaje = Label(
            ventana,
            text="✅ RESPUESTA CORRECTA",
            bg="green",
            fg="white",
            font=("Arial",20,"bold")
        )

        mensaje.place(x=420, y=300)

        ventana.after(1000, mensaje.destroy)

        mover_moto()

    else:

        respuesta_correcta = respuestas[correcta]

        messagebox.showerror(
            "INCORRECTO",
            "Respuesta incorrecta\n\n"
            + "La respuesta correcta era:\n\n"
            + respuesta_correcta
        )

        # AVANZA LA IGNORANCIA

        x4 += 80
        puntos4 += 10

        moto4.place(x=x4, y=550)

        lbl_p4.config(
            text=f"Ignorancia: {puntos4} | Victorias: {victorias4}"
        )

        if x4 >= 1000:

            victorias4 += 1

            lbl_p4.config(
                text=f"Ignorancia: {puntos4} | Victorias: {victorias4}"
            )

            messagebox.showinfo(
                "DERROTA",
                "La Ignorancia ganó la ronda"
            )

            ronda += 1

            lbl_ronda.config(text=str(ronda))

            reiniciar()

        siguiente_turno()

# ---------------- REINICIAR ----------------

def reiniciar():

    global x1, x2, x3, x4
    global turno

    preguntas_usadas.clear()

    x1 = 20
    x2 = 20
    x3 = 20
    x4 = 20

    turno = 1

    moto1.place(x=20, y=250)
    moto2.place(x=20, y=350)
    moto3.place(x=20, y=450)
    moto4.place(x=20, y=550)

    lbl_turno.config(text="Jugador 1")

    lbl_pregunta.config(
        text="Selecciona una categoría para comenzar"
    )

    for boton in botones:
        boton.config(text="")

# ---------------- TITULOS ----------------

Label(
    ventana,
    text="Categorias",
    fg="yellow",
    bg="black",
    font=("Arial",20,"bold")
).place(x=30,y=30)

from tkinter import ttk

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground="white",
    background="white",
    foreground="black",
    arrowsize=25
)

ventana.option_add("*TCombobox*Listbox.font", ("Arial", 22))
ventana.option_add("*TCombobox*Listbox.selectBackground", "blue")
ventana.option_add("*TCombobox*Listbox.selectForeground", "white")

combo = ttk.Combobox(
    ventana,
    values=[
        "Geografía",
        "Historia",
        "Matemáticas",
        "Ciencia",
        "Literatura",
        "Deportes",
        "Tecnología",
        "Arte",
        "Música",
        "Cultura General"
    ],
    font=("Arial",22),
    state="readonly"
)

combo.place(x=190, y=30, width=350, height=45)
combo.bind("<<ComboboxSelected>>", seleccionar_categoria)
# ---------------- TURNO ----------------

lbl_turno = Label(
    ventana,
    text="Jugador 1",
    fg="cyan",
    bg="black",
    font=("Arial",25,"bold")
)

lbl_turno.place(x=700,y=20)

# ---------------- BOTON REINICIAR ----------------

print("Cronómetro ejecutándose")


def verificar_tiempo():

    global x4
    global puntos4

    x4 += 80
    puntos4 += 10

    moto4.place(x=x4, y=550)

    lbl_p4.config(
        text=f"Ignorancia: {puntos4} | Victorias: {victorias4}"
    )

    siguiente_turno()

Button(
    ventana,
    text="REINICIAR",
    bg="red",
    fg="white",
    font=("Arial",18,"bold"),
    command=reiniciar
).place(x=1010,y=20)

# ---------------- PREGUNTA ----------------



Label(
    ventana,
    text="Pregunta",
    fg="white",
    bg="black",
    font=("Arial",25,"bold")
).place(x=20,y=100)

lbl_pregunta = Label(
    ventana,
    text="Selecciona una categoría para comenzar",
    bg="lightgray",
    fg="black",
    font=("Arial",30,"bold"),
    width=65,
    anchor="w"
)

lbl_pregunta.place(x=170,y=100)

# ---------------- RESPUESTAS ----------------

botones = []

# POSICIONES CON MAS SEPARACION
posiciones_x = [40, 330, 620, 910]

for i in range(4):

    boton = Button(
        ventana,
        text="",
        bg="blue",
        fg="white",
        font=("Arial",16,"bold"),
        width=15,
        height=1,
        relief="raised",
        bd=5,
        command=lambda i=i: verificar(i)
    )

    boton.place(
        x=posiciones_x[i],
        y=160
    )

    botones.append(boton)
# ---------------- TABLERO ----------------

Label(
    ventana,
    text="RONDA",
    bg="black",
    fg="yellow",
    font=("Arial",16,"bold")
).place(x=20,y=210)

lbl_ronda = Label(
    ventana,
    text="1",
    bg="black",
    fg="white",
    font=("Arial",14,"bold")
)

lbl_ronda.place(x=120,y=210)

lbl_tiempo = Label(
    ventana,
    text="20",
    bg="black",
    fg="white",
    font=("Arial",20,"bold")
)

lbl_tiempo.place(x=200, y=210)

lbl_tiempo.config(text="20")

lbl_p1 = Label(
    ventana,
    text="J1 Puntos: 0 | Victorias: 0",
    bg="black",
    fg="cyan",
    font=("Arial",14,"bold")
)

lbl_p1.place(x=20,y=640)

lbl_p2 = Label(
    ventana,
    text="J2 Puntos: 0 | Victorias: 0",
    bg="black",
    fg="orange",
    font=("Arial",14,"bold")
)

lbl_p2.place(x=320,y=640)

lbl_p3 = Label(
    ventana,
    text="J3 Puntos: 0 | Victorias: 0",
    bg="black",
    fg="lime",
    font=("Arial",14,"bold")
)

lbl_p3.place(x=620,y=640)

lbl_p4 = Label(
    ventana,
    text="Ignorancia: 0 | Victorias: 0",
    bg="black",
    fg="red",
    font=("Arial",14,"bold")
)

lbl_p4.place(x=900,y=640)

# ---------------- META ----------------

Label(
    ventana,
    text="🏁 META 🏁",
    bg="yellow",
    fg="black",
    font=("Arial",22,"bold")
).place(x=1040,y=220)

# ---------------- PISTAS ----------------

Frame(ventana,bg="white",width=1050,height=5).place(x=120,y=330)
Frame(ventana,bg="white",width=1050,height=5).place(x=120,y=430)
Frame(ventana,bg="white",width=1050,height=5).place(x=120,y=530)
Frame(ventana,bg="white",width=1050,height=5).place(x=120,y=630)

# ---------------- IMAGENES MOTOS ----------------

img1 = Image.open("im/1.GIF")
img1 = img1.resize((90,90))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("im/2.GIF")
img2 = img2.resize((90,90))
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("im/3.GIF")
img3 = img3.resize((90,90))
img3 = ImageTk.PhotoImage(img3)

img4 = Image.open("im/4.GIF")
img4 = img4.resize((90,90))
img4 = ImageTk.PhotoImage(img4)

# ---------------- MOTOS ----------------

moto1 = Label(
    ventana,
    image=img1,
    bg="black"
)

moto2 = Label(
    ventana,
    image=img2,
    bg="black"
)

moto3 = Label(
    ventana,
    image=img3,
    bg="black"
)

moto4 = Label(
    ventana,
    image=img4,
    bg="black"
)

moto1.place(x=20,y=250)
moto2.place(x=20,y=350)
moto3.place(x=20,y=450)
moto4.place(x=20,y=550)

# ---------------- INICIO ----------------

ventana.mainloop()