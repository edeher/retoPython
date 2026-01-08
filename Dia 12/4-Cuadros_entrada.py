from tkinter import (
    Checkbutton,
    Entry,
    Tk,
    Frame,
    TOP,
    FLAT,
    Label,
    BOTTOM,
    LabelFrame,
    LEFT,
    RIGHT,
    IntVar,
)
# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry("1020x630+0+0")

# evitar maximar
aplicacion.resizable(0, 0)

# titulo d ela ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# color de fondo de la ventana
aplicacion.config(bg="burlywood")

# panel superiro
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(
    panel_superior,
    text="Sistema de Facturación",
    fg="azure4",
    font=("Dosis", 48),
    bg="burlywood",
    width=27,
)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side="left")

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas

panel_comidas = LabelFrame(
    panel_izquierdo,
    text="Comidas",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)

panel_comidas.pack(side=LEFT)

# panel bebidas

panel_bebidas = LabelFrame(
    panel_izquierdo,
    text="Bebidas",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)

panel_bebidas.pack(side=LEFT)

# panel postres

panel_postres = LabelFrame(
    panel_izquierdo,
    text="Postres",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)

panel_postres.pack(side=LEFT)

# Panel Derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(
    panel_derecho,
    bd=1,
    relief=FLAT,
    bg='burlywood',
)
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(
    panel_derecho,
    bd=1,
    relief=FLAT,
    bg='burlywood',
)
panel_recibo.pack()

# Panel botones
panel_botones = Frame(
    panel_derecho,
    bd=1,
    relief=FLAT,
    bg='burlywood',
)
panel_botones.pack()

# lista de productos
lista_comidas = [
    "Pollo",
    "Carne",
    "Pescado",
    "Ensalada",
    "Arroz",
    "Pasta",
    "Sopa",
    "Pan",
]
lista_bebidas = [
    "Agua",
    "Refresco",
    "Cerveza",
    "Vino",
    "Zumo",
    "Café",
    "Té",
    "Leche",
]
lista_postres = [
    "Helado",
    "Tarta",
    "Fruta",
    "Yogur",
    "Flan",
    "Natillas",
    "Galletas",
    "Chocolate",
]

# Generar items comida
variables_comida = []
cuadros_comida = []
textos_comida = []
contador = 0
for comida in lista_comidas:

    # crear checkButton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=("Dosis", 16, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_comida[contador],
    )
    comida.grid(row=contador, column=0, sticky='w')

    # crear los cuadros de entrada
    cuadros_comida.append('')
    textos_comida.append('')
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state="disabled",
        textvariable=textos_comida[contador],
    )
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items bebida
variables_bebida = []
cuadros_bebida = []
textos_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(
        panel_bebidas,
        text=bebida.title(),
        font=("Dosis", 16, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_bebida[contador],
    )
    bebida.grid(row=contador, column=0, sticky='w')

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    textos_bebida.append('')
    cuadros_bebida[contador] = Entry(
        panel_bebidas,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state="disabled",
        textvariable=textos_bebida[contador],
    )
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items postre
variables_postre = []
cuadros_postre = []
textos_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(
        panel_postres,
        text=postre.title(),
        font=("Dosis", 16, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_postre[contador],
    )
    postre.grid(row=contador, column=0, sticky='w')

    # crear los cuadros de entrada
    cuadros_postre.append('')
    textos_postre.append('')
    cuadros_postre[contador] = Entry(
        panel_postres,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state="disabled",
        textvariable=textos_postre[contador],
    )
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1

# evitar que se cierre la pantalla
aplicacion.mainloop()
