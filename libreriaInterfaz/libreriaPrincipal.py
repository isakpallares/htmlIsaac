from tkinter import *
from libreriaInterfaz import *

#CONFIGURACION DE PANTALLA
ventana = Tk()
ventana.title("CRUD Interfaz")
ventana.geometry("400x200+700+300")

#IMAGEN Y  CUSTOM
# Establecerlo como ícono de la ventana.
icono = PhotoImage(file="images.png")

ventana.iconphoto(True, icono)

barra_menu = Menu(ventana)

menuClientes = Menu(barra_menu, tearoff=0)

texto_grande = Label(ventana, text="LIBRERIA DÍA", font=("Arial", 24))
texto_grande.place(relx=0.5, rely=0.5, anchor="center")
texto_grande.pack()
texto_grande.configure(foreground='#ff7514')

def centrar_texto(event):
    texto_grande.place_configure(relx=0.5, rely=0.5, anchor="center")

# Vincular la función a un evento de cambio de tamaño de la ventana
ventana.bind("<Configure>", centrar_texto)


barra_menu.add_cascade(label="Clientes", menu=menuClientes)
menuClientes.add_command(label="Crear Cliente", command=ingresarCliente)
menuClientes.add_command(label="Lista Cliente", command=listaCliente)
menuClientes.add_command(label="Buscar Cliente", command=buscarCliente)
menuClientes.add_command(label="Actualizar Cliente", command=actualizarCliente)
menuClientes.add_command(label="Eliminar Cliente", command=borrarCliente)
menuClientes.add_separator()
menuClientes.add_command(label="Salir", command=ventana.quit)


menuLibros = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Libros", menu=menuLibros)
menuLibros.add_command(label="Crear Libro", command=ingresarLibro)
menuLibros.add_command(label="Lista Libros", command=listaLibros)
menuLibros.add_command(label="Buscar Libros", command=buscarLibro)
menuLibros.add_command(label="Actualizar Libros", command=actualizarLibro)
menuLibros.add_command(label="Eliminar Libros", command=borrarLibro)
menuLibros.add_separator()
menuLibros.add_command(label="Salir", command=ventana.quit)


menuVentas = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ventas", menu=menuVentas)
menuVentas.add_command(label="Crear Venta", command=ingresarVenta)
menuVentas.add_command(label="Lista Venta", command=listaVentas)
menuVentas.add_command(label="Buscar Ventas", command=buscarVenta)
menuVentas.add_command(label="Actualizar Ventas", command=actualizarVenta)
menuVentas.add_command(label="Eliminar Ventas", command=borrarVenta)
menuVentas.add_separator()
menuVentas.add_command(label="Salir", command=ventana.quit)


menuEstadisticas = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Estadisticas", menu=menuEstadisticas)
menuEstadisticas.add_command(label="Ventas totales Por Libro", command=totalesLibro)
menuEstadisticas.add_command(label="Mayor y Menor Vendido", command=masYmenos)
menuEstadisticas.add_command(label="Cantidad Total Vendida", command=ventaTotalLibreria)
menuEstadisticas.add_command(label="Cliente Mayor Venta", command=clienteMayorVenta)
menuEstadisticas.add_command(label="Cliente Mayor Volumen de Venta", command=clienteMayorVolumen)
menuEstadisticas.add_separator()
menuEstadisticas.add_command(label="Salir", command=ventana.quit)


ventana.config(menu=barra_menu)
ventana.mainloop()