from tkinter import Tk

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

# evitar que se cierre la pantalla
aplicacion.mainloop()
