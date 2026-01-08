from tkinter import (
    Tk,
    Frame,
    TOP,
    FLAT,
    Label,
    BOTTOM,
    LabelFrame,
    LEFT,
    RIGHT,
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
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación",
                        fg="azure4", font=("Dosis", 48),
                        bg="burlywood", width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side="left")

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas

panel_comidas = LabelFrame(panel_izquierdo, text="Comidas",
                           font=("Dosis", 19, "bold"), bd=1,
                           relief=FLAT, fg="azure4")

panel_comidas.pack(side=LEFT)

# panel bebidas

panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas",
                           font=("Dosis", 19, "bold"), bd=1,
                           relief=FLAT, fg="azure4")

panel_bebidas.pack(side=LEFT)

# panel postres

panel_postres = LabelFrame(panel_izquierdo, text="Postres",
                           font=("Dosis", 19, "bold"), bd=1,
                           relief=FLAT, fg="azure4")

panel_postres.pack(side=LEFT)

# Panel Derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT,
                          bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT,
                     bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT,
                      bg='burlywood')
panel_botones.pack()

# evitar que se cierre la pantalla
aplicacion.mainloop()
