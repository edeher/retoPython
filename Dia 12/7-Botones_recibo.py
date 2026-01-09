from tkinter import (
    Checkbutton,
    Entry,
    Text,
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
    Button
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
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=40)
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
    textos_comida[contador] = IntVar()
    textos_comida[contador].set('0')
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
    textos_bebida[contador] = IntVar()
    textos_bebida[contador].set('0')
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
    textos_postre[contador] = IntVar()
    textos_postre[contador].set('0')
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

# variables
var_costo_comida = IntVar()
var_costo_bebida = IntVar()
var_costo_postre = IntVar()
var_subtotal = IntVar()
var_impuestos = IntVar()
var_total = IntVar()

# Etiquetas de costo y campos de entradas
etiqueta_costo_comida = Label(
    panel_costos,
    text="Costo Comida",
    font=("Dosis", 16, "bold"),
    bg="azure4",
    fg="white",
)

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_comida
)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(
    panel_costos,
    text="Costo Bebida",
    font=("Dosis", 16, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_bebida
)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(
    panel_costos,
    text="Costo Postre",
    font=("Dosis", 16, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_postre
)
texto_costo_postre.grid(row=2, column=1, padx=41)


etiqueta_subtotal = Label(
    panel_costos,
    text="Subtotal",
    font=("Dosis", 16, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_subtotal
)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(
    panel_costos,
    text="Impuestos",
    font=("Dosis", 16, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_impuestos
)
texto_impuestos.grid(row=1, column=3, padx=41)


etiqueta_total = Label(
    panel_costos,
    text="Total",
    font=("Dosis", 16, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_total
)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0
for boton in botones:
    boton = Button(
        panel_botones,
        text=boton.title(),
        font=("Dosis", 14, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=9,
    )
    boton.grid(row=0, column=columnas)
    columnas += 1

# area de recibo
text_recibo = Text(
    panel_recibo,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=42,
    height=10,
)
text_recibo.grid(row=0, column=0)


# evitar que se cierre la pantalla
aplicacion.mainloop()
