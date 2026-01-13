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
    Button,
    END,
)
import random
import datetime

# operador

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, 'end')
    visor_calculadora.insert('end', operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, 'end')


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, 'end')
    visor_calculadora.insert('end', resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state="normal")
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, 'end')
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state="disabled")
            textos_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state="normal")
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, 'end')
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state="disabled")
            textos_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state="normal")
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, 'end')
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state="disabled")
            textos_postre[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in textos_comida:
        pc = precios_comida[p]
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * pc)
        p += 1
    print(sub_total_comida)

    sub_total_bebida = 0
    p = 0
    for cantidad in textos_bebida:
        bc = precios_bebida[p]
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * bc)
        p += 1
    print(sub_total_bebida)

    sub_total_postre = 0
    p = 0
    for cantidad in textos_postre:
        poc = precios_postres[p]
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * poc)
        p += 1
    print(sub_total_postre)

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos
    var_costo_comida.set(f"${sub_total_comida:.2f}")
    var_costo_bebida.set(f"${sub_total_bebida:.2f}")
    var_costo_postre.set(f"${sub_total_postre:.2f}")
    var_subtotal.set(f"${sub_total:.2f}")
    var_impuestos.set(f"${impuestos:.2f}")
    var_total.set(f"${total:.2f}")


def recibo():
    texto_recibo.delete(1.0, 'end')
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = fecha.strftime("%d/%m/%Y - %H:%M:%S")
    texto_recibo.insert(END, f"Recibo:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, "*" * 54 + "\n")
    texto_recibo.insert('end', "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert('end', "-" * 54 + "\n")

    X = 0
    for comida in lista_comidas:
        if textos_comida[X].get() != '0':
            texto_recibo.insert('end',
                                f"{comida}\t\t{textos_comida[X].get()}\t"
                                f"${float(textos_comida[X].get()) * precios_comida[X]:.2f}\n")
        X += 1
    X = 0
    for bebida in lista_bebidas:
        if textos_bebida[X].get() != '0':
            texto_recibo.insert('end',
                                f"{bebida}\t\t{textos_bebida[X].get()}\t"
                                       f"${float(textos_bebida[X].get()) * precios_bebida[X]:.2f}\n")
        X += 1
    X = 0
    for postre in lista_postres:
        if textos_postre[X].get() != '0':
            texto_recibo.insert('end',
                                f"{postre}\t\t{textos_postre[X].get()}\t"
                                       f"${float(textos_postre[X].get()) * precios_postres[X]:.2f}\n")
        X += 1


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry("1110x630+0+0")

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
    font=("Dosis", 58),
    bg="burlywood",
    width=27,
)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side="left")

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50)
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
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_comida[contador],
        command=revisar_check
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
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_bebida[contador],
        command=revisar_check
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
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_postre[contador],
        command=revisar_check
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
    font=("Dosis", 12, "bold"),
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
    font=("Dosis", 12, "bold"),
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
    font=("Dosis", 12, "bold"),
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
    font=("Dosis", 12, "bold"),
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
    font=("Dosis", 12, "bold"),
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
    font=("Dosis", 12, "bold"),
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
botones_creados = []
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
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)

# area de recibo
texto_recibo = Text(
    panel_recibo,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=42,
    height=10,
)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_calculadora = Entry(
    panel_calculadora,
    font=("Dosis", 16, "bold"),
    bd=1,
    width=32,
)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# botones de la calculadora
botones_calculadora = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', 'x',
    'R', 'B', '0', '/',
]

botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(
        panel_calculadora,
        text=boton.title(),
        font=("Dosis", 16, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=8,
    )
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))


# evitar que se cierre la pantalla
aplicacion.mainloop()
