from tkinter import *

ventana_principal = Tk()
ventana_principal.title("Directorio de Contactos")
ventana_principal.minsize(width=300, height=300)
ventana_principal.config(padx=50, pady=35)

etiqueta1 = Label(text="Directorio de contactos", font=("Times New Roman", 16))
etiqueta1.grid(column=0, row=1)

imagen = Canvas(width=200, height=200)
logo_img = PhotoImage(file="descarga.png")
imagen.create_image(100, 100, image=logo_img)
imagen.grid(column=0, row=0)

boton1 = Button(text="Mostrar", font=("Times New Roman", 14))
boton1.grid(column=0, row=3)
boton2 = Button(text="Agregar", font=("Times New Roman", 14))
boton2.grid(column=0, row=4)
boton3 = Button(text="Buscar", font=("Times New Roman", 14))
boton3.grid(column=0, row=5)

ventana_principal.mainloop()