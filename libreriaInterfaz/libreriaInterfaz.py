from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from sqlLibreria import conectar_db, desconectar_db
from prettytable import PrettyTable
from libreriaGestion import *


def ingresarCliente():
    ventana_agregar_usuario = Toplevel()
    ventana_agregar_usuario.title("Agregar Usuario")
    ventana_agregar_usuario.geometry("600x400")
    


    lblNombre = Label(ventana_agregar_usuario, text="Nombre:")
    lblNombre.pack()
    nombre_entry = Entry(ventana_agregar_usuario)
    nombre_entry.pack()

    lblId = Label(ventana_agregar_usuario, text="ID:")
    lblId.pack()
    id_entry = Entry(ventana_agregar_usuario)
    id_entry.pack()
    
    def guardar():
        nombre = nombre_entry.get()
        id = id_entry.get()
        if nombre != "" and id != "":
            if validarIDClientes(id):
                messagebox.showerror("Error","Ya hay un cliente con el mismo id.")
            else:
                ingresar_cliente(nombre,id)
                cargar_usuarios()
                messagebox.showinfo("Agregado","Cliente agregado correctamente.")
        else:
            messagebox.showerror("Error","ingrese todos los campos correspondientes.")
     
    def cargar_usuarios():
        usuarios = obtener_Clientes()
        tabla_usuarios.delete(*tabla_usuarios.get_children())
        for usuario in usuarios:
            tabla_usuarios.insert("", index='end', values=(usuario[0], usuario[1])) 
    
    def cargar_usuario(event):
        selected_row = tabla_usuarios.focus()
        if selected_row:
            values = tabla_usuarios.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
            id_entry.config(state="disabled")
            nombre_entry.delete(0, END)
            nombre_entry.insert(END, values[1])
     
    def limpiar_campos():
        id_entry.config(state="normal")
        id_entry.delete(0,END)
        nombre_entry.delete(0,END)
        
        
    guardar_boton = Button(ventana_agregar_usuario, text="Guardar", command=guardar)
    guardar_boton.pack(pady=10)
    tabla_frame = Frame(ventana_agregar_usuario)

    limpiar_button = Button(ventana_agregar_usuario, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack()        
        
        
    tabla_frame.pack(pady=10)

    tabla_usuarios = ttk.Treeview(tabla_frame, columns=("id", "nombre"), show="headings")
    tabla_usuarios.heading("id", text="ID")
    tabla_usuarios.heading("nombre", text="Nombre")
    tabla_usuarios.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_usuarios.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_usuarios.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_usuarios.yview)

    tabla_usuarios.bind("<ButtonRelease-1>", cargar_usuario)

    cargar_usuarios()
    
def actualizarCliente():
    ventana_actualizar_usuario = Toplevel()
    ventana_actualizar_usuario.title("Actualizar Usuario")
    ventana_actualizar_usuario.geometry("700x500")
   
    
    def cargar_clientes():
        usuarios = obtener_Clientes()
        tabla_cliente.delete(*tabla_cliente.get_children())
        for usuario in usuarios:
            tabla_cliente.insert("", index='end', values=(usuario[0], usuario[1]))
    
    def cargar_cliente(event):
        selected_row = tabla_cliente.focus()
        if selected_row:
            values = tabla_cliente.item(selected_row)["values"]
            idActual_entry.config(state="normal")
            idActual_entry.delete(0, END)
            idActual_entry.insert(END, values[0])
            nombre_entry.delete(0, END)
            nombre_entry.insert(END, values[1])
            
    def guardar_actualizacion():
        id = id_entry.get()
        nombre = nombre_entry.get()
        anterior = idActual_entry.get()
        if anterior != "":
            if validarIDClientes(anterior):
                if id == "" and nombre != "":
                    actualizar_nombre(anterior,nombre)
                    cargar_clientes()
                    messagebox.showinfo("Realizado","El cliente ha sido actualizado")
                else:
                    if id != "" and nombre == "" or id != "" and nombre != "":
                        if validarIDClientes(id):
                            messagebox.showerror("Error","El ID ya existe.")
                        else:
                            actualizar_Cliente(id,nombre,anterior)
                            cargar_clientes()
                            messagebox.showinfo("Realizado","El cliente ha sido actualizado")
            else:
                messagebox.showerror("Error","El ID no existe.")
        else:
            messagebox.showerror("Error","Debe de haber un Id")
            cargar_clientes()
    
    def limpiar_campos():
        id_entry.config(state="normal")
        id_entry.delete(0,END)
        nombre_entry.delete(0,END)
        idActual_entry.delete(0,END)
        
    tabla_frame = Frame(ventana_actualizar_usuario)
    tabla_frame.pack(pady=10)
    
    tabla_cliente = ttk.Treeview(tabla_frame, columns=("id", "nombre", "edad"), show="headings")
    tabla_cliente.heading("id", text="ID")
    tabla_cliente.heading("nombre", text="Nombre")
    tabla_cliente.pack(side=LEFT, fill=Y)

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_cliente.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_cliente.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_cliente.yview)
    
    tabla_cliente.bind("<ButtonRelease-1>", cargar_cliente)
    
    cargar_clientes()
    
    
    id_label = Label(ventana_actualizar_usuario, text="ID Nueva:")
    id_label.pack()
    id_entry = Entry(ventana_actualizar_usuario)
    id_entry.pack()
    
    idActual_label = Label(ventana_actualizar_usuario, text="ID Actual:")
    idActual_label.pack()
    idActual_entry = Entry(ventana_actualizar_usuario)
    idActual_entry.pack()
    
    nombre_label = Label(ventana_actualizar_usuario, text="Nombre:")
    nombre_label.pack()
    nombre_entry = Entry(ventana_actualizar_usuario)
    nombre_entry.pack()    

    guardar_button = Button(ventana_actualizar_usuario, text="Guardar", command=guardar_actualizacion)
    guardar_button.pack(pady=10)

    limpiar_button = Button(ventana_actualizar_usuario, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack()

def borrarCliente():
    ventana_eliminar_usuario = Toplevel()
    ventana_eliminar_usuario.title("Eliminar Usuario")
    ventana_eliminar_usuario.geometry("700x400")
    
    def cargar_clientes():
        usuarios = obtener_Clientes()
        tabla_cliente.delete(*tabla_cliente.get_children())
        for usuario in usuarios:
            tabla_cliente.insert("", index='end', values=(usuario[0], usuario[1]))
    
    def cargar_cliente(event):
        selected_row = tabla_cliente.focus()
        if selected_row:
            values = tabla_cliente.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
    
    def eliminar_clientes():
        id = id_entry.get()
        if id != "":
            if validarIDClientes(id):
                if validadIDClientesVentas(id):
                    messagebox.showerror("En venta", "El usuario ya tiene ventas registradas.")
                else:
                    eliminar_Cliente(id)
                    cargar_clientes()
                    messagebox.showinfo("Eliminado","El cliente ha sido Eliminado")
            else:
                messagebox.showerror("Error","No hay un cliente con ese Id.")
        else:
            messagebox.showerror("Error","Debe de haber un Id")
            cargar_clientes()
    
    def limpiar_campos():
            id_entry.config(state="normal")
            id_entry.delete(0,END)
            
    tabla_frame = Frame(ventana_eliminar_usuario)
    tabla_frame.pack(pady=10)
        
    tabla_cliente = ttk.Treeview(tabla_frame, columns=("id", "nombre", "edad"), show="headings")
    tabla_cliente.heading("id", text="ID")
    tabla_cliente.heading("nombre", text="Nombre")
    tabla_cliente.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_cliente.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    tabla_cliente.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_cliente.yview)
        
    tabla_cliente.bind("<ButtonRelease-1>", cargar_cliente)
        
    cargar_clientes()

        
    id_label = Label(ventana_eliminar_usuario, text="ID A Eliminar:")
    id_label.pack()
    id_entry = Entry(ventana_eliminar_usuario)
    id_entry.pack()
        
    borrar_button = Button(ventana_eliminar_usuario, text="Borrar", command=eliminar_clientes)
    borrar_button.pack(pady=10)
    
    limpiar_button = Button(ventana_eliminar_usuario, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack()

def buscarCliente():
    ventana_buscar_Clientes = Toplevel()
    ventana_buscar_Clientes.title("LISTA DE CLIENTES")
    ventana_buscar_Clientes.geometry("600x450")  
 
    def buscar():
        id = id_entry.get()
        if id != "":
            conexion, cursor = conectar_db("libreria.db")
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
            resultado = cursor.fetchone()
            conexion.close()
            if resultado is not None:
                mensaje = (f"Nombre: {resultado[1]} ID: {id}")
                messagebox.showinfo("Se ha encontrado el Cliente: ", mensaje)      
        else:
            messagebox.showerror("Error", "No se encuentra el ID")
                
    def cargar_usuarios():
        
        usuarios = obtener_Clientes()
        tabla_usuarios.delete(*tabla_usuarios.get_children())
        for usuario in usuarios:
            tabla_usuarios.insert("", index='end', values=(usuario[0], usuario[1])) 

    def cargar_usuario(event):
        selected_row = tabla_usuarios.focus()
        if selected_row:
            values = tabla_usuarios.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
            id_entry.config(state="disabled")

    def limpiar_campos():
            id_entry.config(state="normal")
            id_entry.delete(0,END)
            

    tabla_frame = Frame(ventana_buscar_Clientes)
        
    tabla_frame.pack(pady=10)

    tabla_usuarios = ttk.Treeview(tabla_frame, columns=("id", "nombre"), show="headings")
    tabla_usuarios.heading("id", text="ID")
    tabla_usuarios.heading("nombre", text="Nombre")
    tabla_usuarios.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_usuarios.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_usuarios.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_usuarios.yview)

    tabla_usuarios.bind("<ButtonRelease-1>", cargar_usuario)
    
    cargar_usuarios()   

    id_label = Label(ventana_buscar_Clientes, text="Digite el ID a buscar: ")
    id_label.pack(pady=20)
    id_entry = Entry(ventana_buscar_Clientes)
    id_entry.pack()
    
    guardar_button = Button(ventana_buscar_Clientes, text="Buscar", command=buscar)
    guardar_button.pack(pady=10)

    limpiar_button = Button(ventana_buscar_Clientes, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack()  

def listaCliente():
    
    ventana_Lista_Clientes = Toplevel()
    ventana_Lista_Clientes.title("LISTA DE CLIENTES")
    ventana_Lista_Clientes.geometry("600x400")
    
    def cargar_usuarios():
        
        usuarios = obtener_Clientes()
        tabla_usuarios.delete(*tabla_usuarios.get_children())
        for usuario in usuarios:
            tabla_usuarios.insert("", index='end', values=(usuario[0], usuario[1])) 

    tabla_frame = Frame(ventana_Lista_Clientes)
        
    tabla_frame.pack(pady=10)

    tabla_usuarios = ttk.Treeview(tabla_frame, columns=("id", "nombre"), show="headings")
    tabla_usuarios.heading("id", text="ID")
    tabla_usuarios.heading("nombre", text="Nombre")
    tabla_usuarios.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_usuarios.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_usuarios.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_usuarios.yview)

    tabla_usuarios.bind("<ButtonRelease-1>")
    
    cargar_usuarios()
#Archivo Clientes

def ingresarLibro():
    ventana_agregar_libro = Toplevel()
    ventana_agregar_libro.title("Agregar Libro")
    ventana_agregar_libro.geometry("900x400")
  
    
    lblIsbn = Label(ventana_agregar_libro, text="ISBN:")
    lblIsbn.pack()
    isbn_entry = Entry(ventana_agregar_libro)
    isbn_entry.pack()

    lblTitulo = Label(ventana_agregar_libro, text="Titulo:")
    lblTitulo.pack()
    titulo_entry = Entry(ventana_agregar_libro)
    titulo_entry.pack()
    
    lblPrecio = Label(ventana_agregar_libro, text="Precio:")
    lblPrecio.pack()
    precio_entry = Entry(ventana_agregar_libro)
    precio_entry.pack()
    
    lblInventario = Label(ventana_agregar_libro, text="Inventario:")
    lblInventario.pack()
    inventario_entry = Entry(ventana_agregar_libro)
    inventario_entry.pack()
    
    
    def guardar():
        nombre = titulo_entry.get()
        isbn = isbn_entry.get()
        precio = precio_entry.get()
        inventario = inventario_entry.get()
        
        if nombre != "" and isbn != "" and precio != "" and inventario != "":
            if validarLibros(isbn):
                messagebox.showerror("Error","Ya hay un Libro con el mismo isbn.")
            else:
                ingresar_Libros(isbn,nombre,precio,inventario)
                cargar_usuarios()
                messagebox.showinfo("Agregado","Libro agregado correctamente.")
        else:
            messagebox.showerror("Error","ingrese todos los campos correspondientes.")
     
    def cargar_usuarios():
        libros = obtener_Libros()
        tabla_libros.delete(*tabla_libros.get_children())
        for usuario in libros:
            tabla_libros.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3])) 
    
    def cargar_usuario(event):
        selected_row = tabla_libros.focus()
        if selected_row:
            values = tabla_libros.item(selected_row)["values"]
            isbn_entry.config(state="normal")
            isbn_entry.delete(0, END)
            isbn_entry.insert(END, values[0])
            isbn_entry.config(state="disabled")
            titulo_entry.delete(0, END)
            titulo_entry.insert(END, values[1])
            precio_entry.delete(0,END)
            precio_entry.insert(END, values[2])
            inventario_entry.delete(0,END)
            inventario_entry.insert(END,values[3])
            
            
    def limpiar_campos():
        isbn_entry.config(state="normal")
        isbn_entry.delete(0,END)
        titulo_entry.config(state="normal")
        titulo_entry.delete(0,END)
        precio_entry.config(state="normal")
        precio_entry.delete(0,END)
        inventario_entry.config(state="normal")
        inventario_entry.delete(0,END)
        
        
    guardar_boton = Button(ventana_agregar_libro, text="Guardar", command=guardar)
    guardar_boton.pack(pady=10)
    tabla_frame = Frame(ventana_agregar_libro)

    limpiar_button = Button(ventana_agregar_libro, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack(pady=3)        
        
        
    tabla_frame.pack(pady=10)

    tabla_libros = ttk.Treeview(tabla_frame, columns=("ISBN", "Titulo","Precio","Inventario"), show="headings")
    tabla_libros.heading("ISBN", text="ISBN")
    tabla_libros.heading("Titulo", text="Titulo")
    tabla_libros.heading("Precio", text="Precio")
    tabla_libros.heading("Inventario", text="Inventario")
    tabla_libros.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_libros.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_libros.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_libros.yview)

    tabla_libros.bind("<ButtonRelease-1>", cargar_usuario)

    cargar_usuarios()

def actualizarLibro():
    ventana_actualizar_libro = Toplevel()
    ventana_actualizar_libro.title("Actualizar Usuario")
    ventana_actualizar_libro.geometry("900x500")

    
    def cargar_libros():
        usuarios = obtener_Libros()
        tabla_libros.delete(*tabla_libros.get_children())
        for usuario in usuarios:
            tabla_libros.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3]))
            
    def cargar_Libro(event):
        selected_row = tabla_libros.focus()
        if selected_row:
            values = tabla_libros.item(selected_row)["values"]
            isbnActual_entry.config(state="normal")
            isbnActual_entry.delete(0, END)
            isbnActual_entry.insert(END, values[0])
            nombreActual_entry.delete(0, END)
            nombreActual_entry.insert(END, values[1])
            precioActual_entry.delete(0, END)
            precioActual_entry.insert(END, values[2])
            inventarioActual_entry.delete(0,END)
            inventarioActual_entry.insert(END, values[3])
            
  
    def guardar_actualizacion():
        isbn = isbn_entry.get()
        anteriorI = isbnActual_entry.get()
        nombre = nombre_entry.get()
        anteriorN = nombreActual_entry.get()
        precio = precio_entry.get()
        anteriorP = precioActual_entry.get()
        inventario = inventario_entry.get()
        anteriorInvent = inventarioActual_entry.get()
        
        if anteriorI != "":
            if validarLibros(anteriorI):
                if validarLibros(isbn):
                    messagebox.showerror("Error","El ISBN ya existe.")
                else:
                    actualizar_Libro(anteriorI,isbn,anteriorN,nombre,anteriorP,precio,anteriorInvent,inventario)
                    cargar_libros()
                    messagebox.showinfo("Realizado","El Libro ha sido actualizado")
            else:
                messagebox.showerror("Error","El Isbn no existe.")
        else:
            messagebox.showerror("Error","Debe de haber un ISBN")
            cargar_libros()
    
    def limpiar_campos():
        isbn_entry.config(state="normal")
        isbn_entry.delete(0,END)
        isbnActual_entry.delete(0,END)
        nombre_entry.delete(0,END)
        nombreActual_entry.delete(0,END)
        precio_entry.delete(0,END)
        precioActual_entry.delete(0,END)
        inventario_entry.delete(0,END)
        inventarioActual_entry.delete(0,END)
        
    tabla_frame = Frame(ventana_actualizar_libro)
    tabla_frame.pack(pady=10)

    tabla_libros = ttk.Treeview(tabla_frame, columns=("ISBN", "Titulo","Precio","Inventario"), show="headings")
    tabla_libros.heading("ISBN", text="ISBN")
    tabla_libros.heading("Titulo", text="Titulo")
    tabla_libros.heading("Precio", text="Precio")
    tabla_libros.heading("Inventario", text="Inventario")
    tabla_libros.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_libros.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_libros.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_libros.yview)

    tabla_libros.bind("<ButtonRelease-1>", cargar_Libro)

    cargar_libros()
    
    #PRIMER FRAME 
    frame1 = Frame(ventana_actualizar_libro)
    frame1.pack(pady=10)
    
    isbn_label = Label(frame1, text="ISBN Nuevo:")
    isbn_label.pack(side=LEFT, padx = 5)
    isbn_entry = Entry(frame1)
    isbn_entry.pack(side=LEFT, padx = 5)
    
    isbnActual_label = Label(frame1, text="ISBN Actual:")
    isbnActual_label.pack(side=LEFT, padx = 5)
    isbnActual_entry = Entry(frame1)
    isbnActual_entry.pack(side=LEFT, padx = 5)
    
    #SEGUNDO FRAME
    frame2 = Frame(ventana_actualizar_libro)
    frame2.pack(pady=10)
    
    nombre_label = Label(frame2, text="Titulo Nuevo:")
    nombre_label.pack(side=LEFT, padx = 5)
    nombre_entry = Entry(frame2)
    nombre_entry.pack(side=LEFT, padx = 5)    

    nombreActual_label = Label(frame2, text="Titulo Actual:")
    nombreActual_label.pack(side=LEFT, padx = 5)
    nombreActual_entry = Entry(frame2)
    nombreActual_entry.pack(side=LEFT, padx = 5)    

    #TERCER FRAME
    
    frame3 = Frame(ventana_actualizar_libro)
    frame3.pack(pady=10)

    precio_label = Label(frame3, text="Precio Nuevo:")
    precio_label.pack(side=LEFT, padx = 5)
    precio_entry = Entry(frame3)
    precio_entry.pack(side=LEFT, padx = 5)    

    precioActual_label = Label(frame3, text="Precio Actual:")
    precioActual_label.pack(side=LEFT, padx = 5)
    precioActual_entry = Entry(frame3)
    precioActual_entry.pack(side=LEFT, padx = 5)    
    
    #CUARTO FRAME
    
    frame4 = Frame(ventana_actualizar_libro)
    frame4.pack(pady=10)
    
    inventario_label = Label(frame4, text="Inventario Nuevo:")
    inventario_label.pack(side=LEFT, padx = 5)
    inventario_entry = Entry(frame4)
    inventario_entry.pack(side=LEFT, padx = 5)    

    inventarioActual_label = Label(frame4, text="Inventario Actual:")
    inventarioActual_label.pack(side=LEFT, padx = 5)
    inventarioActual_entry = Entry(frame4)
    inventarioActual_entry.pack(side=LEFT, padx = 5)    
    

    guardar_button = Button(ventana_actualizar_libro, text="Guardar", command=guardar_actualizacion)
    guardar_button.pack(pady=10)

    limpiar_button = Button(ventana_actualizar_libro, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack(pady=3)

def borrarLibro():
    ventana_eliminar_libro = Toplevel()
    ventana_eliminar_libro.title("Eliminar Usuario")
    ventana_eliminar_libro.geometry("900x500")

    
    def cargar_libros():
        usuarios = obtener_Libros()
        tabla_libros.delete(*tabla_libros.get_children())
        for usuario in usuarios:
            tabla_libros.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3]))
            
    def cargar_Libro(event):
        selected_row = tabla_libros.focus()
        if selected_row:
            values = tabla_libros.item(selected_row)["values"]
            isbnActual_entry.config(state="normal")
            isbnActual_entry.delete(0, END)
            isbnActual_entry.insert(END, values[0])
            
    def eliminar_libros():
        id = isbnActual_entry.get()
        if id != "":
            if validarLibros(id):
                eliminar_libro(id)
                cargar_libros()
                messagebox.showinfo("Eliminado","El Libro ha sido Eliminado")
            else:
                messagebox.showerror("Error","No hay un libro con ese ISBN.")
        else:
            messagebox.showerror("Error","Debe de haber un ISBN")
            cargar_libros()            
            
    
    def limpiar_campos():
        isbnActual_entry.delete(0,END)
        
    tabla_frame = Frame(ventana_eliminar_libro)
    tabla_frame.pack(pady=10)

    tabla_libros = ttk.Treeview(tabla_frame, columns=("ISBN", "Titulo","Precio","Inventario"), show="headings")
    tabla_libros.heading("ISBN", text="ISBN")
    tabla_libros.heading("Titulo", text="Titulo")
    tabla_libros.heading("Precio", text="Precio")
    tabla_libros.heading("Inventario", text="Inventario")
    tabla_libros.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_libros.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_libros.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_libros.yview)

    tabla_libros.bind("<ButtonRelease-1>", cargar_Libro)

    cargar_libros()
    
    isbnActual_label = Label(ventana_eliminar_libro, text="ID A Eliminar:")
    isbnActual_label.pack()
    isbnActual_entry = Entry(ventana_eliminar_libro)
    isbnActual_entry.pack()
        
    borrar_button = Button(ventana_eliminar_libro, text="Borrar", command=eliminar_libros)
    borrar_button.pack(pady=10)
    
    limpiar_button = Button(ventana_eliminar_libro, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack(pady=3)

def buscarLibro():
  
    ventana_buscar_libro = Toplevel()
    ventana_buscar_libro.title("Buscar Libro")
    ventana_buscar_libro.geometry("900x500")
  
    def cargar_libros():
        usuarios = obtener_Libros()
        tabla_libros.delete(*tabla_libros.get_children())
        for usuario in usuarios:
            tabla_libros.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3]))
            
    def cargar_Libro(event):
        selected_row = tabla_libros.focus()
        if selected_row:
            values = tabla_libros.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
  
    def limpiar_campos():
        id_entry.delete(0,END)

    def buscar():
        id = id_entry.get()
        if id != "":
            conexion, cursor = conectar_db("libreria.db")
            cursor.execute("SELECT * FROM libros WHERE isbn = ?", (id,))
            resultado = cursor.fetchone()
            conexion.close()
            if resultado is not None:
                mensaje = (f"Titulo: {resultado[1]} ISBN: {id} Precio: {resultado[2]} Inventario: {resultado[3]}")
                messagebox.showinfo("Se ha encontrado el Libro: ", mensaje)    
        else:
            messagebox.showerror("Error", "El isbn no existe.")
            
    tabla_frame = Frame(ventana_buscar_libro)
    tabla_frame.pack(pady=10)

    tabla_libros = ttk.Treeview(tabla_frame, columns=("ISBN", "Titulo","Precio","Inventario"), show="headings")
    tabla_libros.heading("ISBN", text="ISBN")
    tabla_libros.heading("Titulo", text="Titulo")
    tabla_libros.heading("Precio", text="Precio")
    tabla_libros.heading("Inventario", text="Inventario")
    tabla_libros.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_libros.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_libros.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_libros.yview)

    tabla_libros.bind("<ButtonRelease-1>", cargar_Libro)

    cargar_libros()

    id_label = Label(ventana_buscar_libro, text="Digite el ISBN a buscar: ")
    id_label.pack(pady=20)
    id_entry = Entry(ventana_buscar_libro)
    id_entry.pack()
    
    guardar_button = Button(ventana_buscar_libro, text="Buscar", command=buscar)
    guardar_button.pack(pady=10)

    limpiar_button = Button(ventana_buscar_libro, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack()  

def listaLibros():
    ventana_Lista_libro = Toplevel()
    ventana_Lista_libro.title("LISTA DE LIBROS")
    ventana_Lista_libro.geometry("900x400")

    def cargar_libros():
        usuarios = obtener_Libros()
        tabla_libros.delete(*tabla_libros.get_children())
        for usuario in usuarios:
            tabla_libros.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3]))

    tabla_frame = Frame(ventana_Lista_libro)
    tabla_frame.pack(pady=10)

    tabla_libros = ttk.Treeview(tabla_frame, columns=("ISBN", "Titulo","Precio","Inventario"), show="headings")
    tabla_libros.heading("ISBN", text="ISBN")
    tabla_libros.heading("Titulo", text="Titulo")
    tabla_libros.heading("Precio", text="Precio")
    tabla_libros.heading("Inventario", text="Inventario")
    tabla_libros.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_libros.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_libros.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_libros.yview)

    tabla_libros.bind("<ButtonRelease-1>")

    cargar_libros()

# VENTAS

def ingresarVenta():
    ventana_ingresar_venta = Toplevel()
    ventana_ingresar_venta.title("INGRESAR VENTA")
    ventana_ingresar_venta.geometry("1300x600")

    def cargar_libros():
        usuarios = mixdeClienteVentas()
        tabla_ventas.delete(*tabla_ventas.get_children())
        for usuario in usuarios:
            tabla_ventas.insert("", index='end', values=(usuario[0], usuario[1],usuario[5],usuario[2],usuario[3],usuario[4]))

    def cargar_Venta(event):
        selected_row = tabla_ventas.focus()
        if selected_row:
            values = tabla_ventas.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
            id_entry.config(state="disabled")
            cliente_entry.delete(0, END)
            cliente_entry.insert(END, values[1])
            isbn_entry.delete(0,END)
            isbn_entry.insert(END, values[2])
            venta_entry.delete(0,END)
            venta_entry.insert(END,values[3])
            precio_entry.delete(0,END)
            precio_entry.insert(END, values[4])

    def ingresarventa():
        idCliente = cliente_entry.get()
        idLibro = isbn_entry.get()
        venta = venta_entry.get()
        
        if idCliente != "" and idLibro != "" and venta != "":
                if validarIDClientes(idCliente):
                    if validarLibros(idLibro):
                        if int(cantidadLibros(idLibro)) < int(venta) :
                            messagebox.showinfo("Cantidad","No hay la cantidad suficiente de libros.")
                        else:
                            ingresar_ventas(idCliente,idLibro,int(venta))
                            cargar_libros()
                            messagebox.showinfo("Agregado","Venta agregada correctamente.")        
                    else:
                        messagebox.showerror("Error","El Isbn del libro no existe.")
                else:
                    messagebox.showerror("Error", "El ID del cliente no existe.")
        else:
            messagebox.showerror("Error", "Todos los campos deben estar registrados.")

    tabla_frame = Frame(ventana_ingresar_venta)
    tabla_frame.pack(pady=10)

    tabla_ventas = ttk.Treeview(tabla_frame, columns=("ID","ID Cliente","Cliente","Libro","Cantidad","Total"), show="headings")
    tabla_ventas.heading("ID", text="ID")
    tabla_ventas.heading("ID Cliente", text="ID Cliente")
    tabla_ventas.heading("Cliente", text="Cliente")
    tabla_ventas.heading("Libro", text="ISBN")
    tabla_ventas.heading("Cantidad", text="Cantidad")
    tabla_ventas.heading("Total", text="Total")
    tabla_ventas.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_ventas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_ventas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_ventas.yview)

    tabla_ventas.bind("<ButtonRelease-1>", cargar_Venta)

    cargar_libros()
    
    lblId = Label(ventana_ingresar_venta, text="ID:")
    lblId.pack()
    id_entry = Entry(ventana_ingresar_venta)
    id_entry.pack()
    id_entry.config(state="disabled")
    
    lblcliente = Label(ventana_ingresar_venta, text="ID Cliente:")
    lblcliente.pack()
    cliente_entry = Entry(ventana_ingresar_venta)
    cliente_entry.pack()
    
    lblIsbn = Label(ventana_ingresar_venta, text="Agregar ISBN:")
    lblIsbn.pack()
    isbn_entry = Entry(ventana_ingresar_venta)
    isbn_entry.pack()

    lblventa = Label(ventana_ingresar_venta, text="Cantidad a Comprar:")
    lblventa.pack()
    venta_entry = Entry(ventana_ingresar_venta)
    venta_entry.pack()
    
    lblprecio = Label(ventana_ingresar_venta, text="Total:")
    lblprecio.pack()
    precio_entry = Entry(ventana_ingresar_venta)
    precio_entry.pack()


    def limpiar_campos():
        isbn_entry.config(state="normal")
        isbn_entry.delete(0,END)
        cliente_entry.config(state="normal")
        cliente_entry.delete(0,END)
        id_entry.delete(0,END)
        venta_entry.config(state="normal")
        venta_entry.delete(0,END)
        precio_entry.delete(0,END)
          
    guardar_boton = Button(ventana_ingresar_venta, text="Guardar", command=ingresarventa)
    guardar_boton.pack(pady=10)
    tabla_frame = Frame(ventana_ingresar_venta)

    limpiar_button = Button(ventana_ingresar_venta, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack(pady=3)   

def actualizarVenta():
    ventana_actualizar_venta = Toplevel()
    ventana_actualizar_venta.title("ACTUALIZAR VENTA")
    ventana_actualizar_venta.geometry("1100x600")

    def cargar_libros():
        usuarios = mixdeClienteVentas()
        tabla_ventas.delete(*tabla_ventas.get_children())
        for usuario in usuarios:
            tabla_ventas.insert("", index='end', values=(usuario[0], usuario[1],usuario[5],usuario[2],usuario[3],usuario[4]))

    def cargar_Venta(event):
        selected_row = tabla_ventas.focus()
        if selected_row:
            values = tabla_ventas.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
            cliente_entry.delete(0, END)
            cliente_entry.insert(END, values[1])
            isbn_entry.delete(0,END)
            isbn_entry.insert(END, values[2])
            venta_entry.delete(0,END)
            venta_entry.insert(END,values[3])
            precio_entry.delete(0,END)
            precio_entry.insert(END, values[4])

    def actualizarventa():
        id = id_entry.get()
        cliente = cliente_entry.get()
        clienteNuevo = clienteNuevo_entry.get()
        isbn = isbn_entry.get()
        isbnNuevo = isbnNuevo_entry.get()
        cantidadNueva = ventaNueva_entry.get()
        
        if id != "":
        
                if validarIDClientes(cliente):
                    if validadIDClientesVentas(cliente):
                        if validarLibros(isbn):
                            if isbnNuevo != "":
                                if not validarLibrosVentas(isbnNuevo):
                                    messagebox.showerror("Error","El isbn no tiene una venta.")
                            else:
                                pass
                            if cantidadNueva != "":
                                if (cantidadLibros(isbn)) < int(cantidadNueva):
                                    messagebox.showerror("Cantidad","No hay la suficiente cantidad de libros deseados.")
                            else:
                                pass
                                
                            if validarVenta(id):
                                actualizarVentas(id,clienteNuevo,isbnNuevo,isbn,cantidadNueva)
                                cargar_libros()
                                messagebox.showinfo("Actualizado","La venta ha sido actualizada.")
                            else:
                                messagebox.showerror("Error","El id no existe.")
                            
                        else:
                            messagebox.showerror("Error","El libro no se encuentra registrado.")
                    else:
                        messagebox.showerror("Error","El id del cliente no tiene una venta.")
                else:
                    messagebox.showerror("Error","El cliente no existe.")
        else:
            messagebox.showerror("Error","Debe haber un id.")


    tabla_frame = Frame(ventana_actualizar_venta)
    tabla_frame.pack(pady=10)

    tabla_ventas = ttk.Treeview(tabla_frame, columns=("ID","ID Cliente","Cliente","Libro","Cantidad","Total"), show="headings")
    tabla_ventas.heading("ID", text="ID")
    tabla_ventas.heading("ID Cliente", text="ID Cliente")
    tabla_ventas.heading("Cliente", text="Cliente")
    tabla_ventas.heading("Libro", text="ISBN")
    tabla_ventas.heading("Cantidad", text="Cantidad")
    tabla_ventas.heading("Total", text="Total")
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_ventas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_ventas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_ventas.yview)

    tabla_ventas.bind("<ButtonRelease-1>", cargar_Venta)

    cargar_libros()

    frameU = Frame(ventana_actualizar_venta)
    frameU.pack(pady=10)

    lblId = Label(frameU, text="ID:")
    lblId.pack(side=LEFT)
    id_entry = Entry(frameU)
    id_entry.pack(side=LEFT, padx = 5)
    
    lblprecio = Label(frameU, text="Total:")
    lblprecio.pack(side=LEFT)
    precio_entry = Entry(frameU)
    precio_entry.pack(side=LEFT, padx = 5)

    frame1 = Frame(ventana_actualizar_venta)
    frame1.pack(pady=10)
    
    lblcliente = Label(frame1, text="ID Cliente:")
    lblcliente.pack(side=LEFT)
    cliente_entry = Entry(frame1)
    cliente_entry.pack(side=LEFT, padx = 5)
    
    lblclienteNuevo = Label(frame1, text="ID Cliente Nuevo:")
    lblclienteNuevo.pack(side=LEFT)
    clienteNuevo_entry = Entry(frame1)
    clienteNuevo_entry.pack(side=LEFT, padx = 5)

    frame2 = Frame(ventana_actualizar_venta)
    frame2.pack(pady=10)

    lblIsbn = Label(frame2, text="ISBN:")
    lblIsbn.pack(side=LEFT)
    isbn_entry = Entry(frame2)
    isbn_entry.pack(side=LEFT, padx = 5)

    lblIsbnNuevo = Label(frame2, text="ISBN Nuevo:")
    lblIsbnNuevo.pack(side=LEFT)
    isbnNuevo_entry = Entry(frame2)
    isbnNuevo_entry.pack(side=LEFT, padx = 5)

    frame3 = Frame(ventana_actualizar_venta)
    frame3.pack(pady=10)


    lblventa = Label(frame3, text="Cantidad:")
    lblventa.pack(side=LEFT)
    venta_entry = Entry(frame3)
    venta_entry.pack(side=LEFT, padx = 5)
    
    lblventaNueva = Label(frame3, text="Cantidad Nueva:")
    lblventaNueva.pack(side=LEFT)
    ventaNueva_entry = Entry(frame3)
    ventaNueva_entry.pack(side=LEFT, padx = 5)    
    
    def limpiar_campos():
        isbn_entry.config(state="normal")
        isbn_entry.delete(0,END)
        cliente_entry.config(state="normal")
        cliente_entry.delete(0,END)
        id_entry.delete(0,END)
        venta_entry.config(state="normal")
        venta_entry.delete(0,END)
        precio_entry.delete(0,END)
        isbnNuevo_entry.config(state="normal")
        isbnNuevo_entry.delete(0,END)
        clienteNuevo_entry.config(state="normal")
        clienteNuevo_entry.delete(0,END)
        ventaNueva_entry.config(state="normal")
        ventaNueva_entry.delete(0,END)
        

    guardar_boton = Button(ventana_actualizar_venta, text="Guardar", command=actualizarventa)
    guardar_boton.pack(pady=10)
    tabla_frame = Frame(ventana_actualizar_venta)

    limpiar_button = Button(ventana_actualizar_venta, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack(pady=3) 

def listaVentas():
    ventana_Lista_libro = Toplevel()
    ventana_Lista_libro.title("LISTA DE VENTAS")
    ventana_Lista_libro.geometry("1300x200")
    def cargar_libros():
        usuarios = mixdeClienteVentas()
        tabla_ventas.delete(*tabla_ventas.get_children())
        for usuario in usuarios:
            tabla_ventas.insert("", index='end', values=(usuario[0], usuario[1],usuario[5],usuario[2],usuario[3],usuario[4]))

    tabla_frame = Frame(ventana_Lista_libro)
    tabla_frame.pack(pady=10)

    tabla_ventas = ttk.Treeview(tabla_frame, columns=("ID","ID Cliente","Cliente","Libro","Cantidad","Total"), show="headings")
    tabla_ventas.heading("ID", text="ID")
    tabla_ventas.heading("ID Cliente", text="ID Cliente")
    tabla_ventas.heading("Cliente", text="Cliente")
    tabla_ventas.heading("Libro", text="ISBN")
    tabla_ventas.heading("Cantidad", text="Cantidad")
    tabla_ventas.heading("Total", text="Total")

    tabla_ventas.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_ventas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_ventas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_ventas.yview)

    tabla_ventas.bind("<ButtonRelease-1>")

    cargar_libros()

def buscarVenta():
    ventana_buscar_venta = Toplevel()
    ventana_buscar_venta.title("BUSCAR VENTAS")
    ventana_buscar_venta.geometry("1100x500")

    def cargar_libros():
        usuarios = mixdeClienteVentas()
        tabla_ventas.delete(*tabla_ventas.get_children())
        for usuario in usuarios:
            tabla_ventas.insert("", index='end', values=(usuario[0], usuario[1],usuario[5],usuario[2],usuario[3],usuario[4]))

    def cargar_Venta(event):
        selected_row = tabla_ventas.focus()
        if selected_row:
            values = tabla_ventas.item(selected_row)["values"]
            id_entry.config(state="normal")
            id_entry.delete(0, END)
            id_entry.insert(END, values[0])
            
    def buscarVenta():        
        id = id_entry.get()
        if id != "":
            conexion, cursor = conectar_db("libreria.db")
            cursor.execute("SELECT * FROM ventas WHERE id = ?", (id,))
            resultado = cursor.fetchone()
            conexion.close()
            if resultado is not None:
                mensaje = (f"ID: {id} Cliente: {resultado[1]} Libro: {resultado[2]} Venta: {resultado[3]} Precio Total: {resultado[4]}")
                messagebox.showinfo("Se ha encontrado la venta: ", mensaje)    
        else:
            messagebox.showerror("Error", "El ID no existe.")

    tabla_frame = Frame(ventana_buscar_venta)
    tabla_frame.pack(pady=10)

    tabla_ventas = ttk.Treeview(tabla_frame, columns=("ID","ID Cliente","Cliente","Libro","Cantidad","Total"), show="headings")
    tabla_ventas.heading("ID", text="ID")
    tabla_ventas.heading("ID Cliente", text="ID Cliente")
    tabla_ventas.heading("Cliente", text="Cliente")
    tabla_ventas.heading("Libro", text="ISBN")
    tabla_ventas.heading("Cantidad", text="Cantidad")
    tabla_ventas.heading("Total", text="Total")

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_ventas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_ventas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_ventas.yview)

    tabla_ventas.bind("<ButtonRelease-1>", cargar_Venta)

    cargar_libros()
       
    def limpiar_campos():
        id_entry.delete(0,END)

    id_label = Label(ventana_buscar_venta, text="Digite el ISBN a buscar: ")
    id_label.pack(pady=20)
    id_entry = Entry(ventana_buscar_venta)
    id_entry.pack()
    
    guardar_button = Button(ventana_buscar_venta, text="Buscar", command=buscarVenta)
    guardar_button.pack(pady=10)

    limpiar_button = Button(ventana_buscar_venta, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack() 
        
def borrarVenta():

    ventana_eliminar_venta = Toplevel()
    ventana_eliminar_venta.title("Eliminar Usuario")
    ventana_eliminar_venta.geometry("900x500")

    def cargar_libros():
        usuarios = mixdeClienteVentas()
        tabla_ventas.delete(*tabla_ventas.get_children())
        for usuario in usuarios:
            tabla_ventas.insert("", index='end', values=(usuario[0], usuario[1],usuario[5],usuario[2],usuario[3],usuario[4]))
         
    def cargar_Libro(event):
        selected_row = tabla_ventas.focus()
        if selected_row:
            values = tabla_ventas.item(selected_row)["values"]
            idActual_entry.config(state="normal")
            idActual_entry.delete(0, END)
            idActual_entry.insert(END, values[0])
            
    def eliminar_libros():
        id = idActual_entry.get()
        if id != "":
            if validarVenta(id):
                eliminarVentas(id)
                cargar_libros()
                messagebox.showinfo("Eliminado","La venta ha sido eliminada")
            else:
                messagebox.showerror("Error","No hay una venta con ese ID.")
        else:
            messagebox.showerror("Error","Debe de haber un ISBN")
            cargar_libros()            
            
    
    def limpiar_campos():
        idActual_entry.delete(0,END)
        

    tabla_frame = Frame(ventana_eliminar_venta)
    tabla_frame.pack(pady=10)

    tabla_ventas = ttk.Treeview(tabla_frame, columns=("ID","ID Cliente","Cliente","Libro","Cantidad","Total"), show="headings")
    tabla_ventas.heading("ID", text="ID")
    tabla_ventas.heading("ID Cliente", text="ID Cliente")
    tabla_ventas.heading("Cliente", text="Cliente")
    tabla_ventas.heading("Libro", text="ISBN")
    tabla_ventas.heading("Cantidad", text="Cantidad")
    tabla_ventas.heading("Total", text="Total")
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_ventas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_ventas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_ventas.yview)

    tabla_ventas.bind("<ButtonRelease-1>",cargar_Libro)

    cargar_libros()
    
    idActual_label = Label(ventana_eliminar_venta, text="ID A Eliminar:")
    idActual_label.pack()
    idActual_entry = Entry(ventana_eliminar_venta)
    idActual_entry.pack()
        
    borrar_button = Button(ventana_eliminar_venta, text="Borrar", command=eliminar_libros)
    borrar_button.pack(pady=10)
    
    limpiar_button = Button(ventana_eliminar_venta, text="Limpiar", command=limpiar_campos)
    limpiar_button.pack(pady=3)
    
# Estadisticas.

def totalesLibro():

        ventana_totalesLibro = Toplevel()
        ventana_totalesLibro.title("TOTALES LIBRO")
        ventana_totalesLibro.geometry("900x400")
        
        id_label = Label(ventana_totalesLibro, text="Digite el ISBN a buscar: ")
        id_label.pack(pady=20)
        id_entry = Entry(ventana_totalesLibro)
        id_entry.pack()

        def totales():
            id = id_entry.get()
            if id != "":

                conexion, cursor = conectar_db("libreria.db")
                cursor.execute("SELECT * FROM ventas WHERE id_libro = ?", (id,))
                resultado = cursor.fetchone()
                
                cursor.execute("SELECT SUM(venta), SUM(precio_Total) FROM ventas WHERE id_libro = ?",(id,)) 
                total = cursor.fetchall()
                for ventas,precio in total:
                    cantidad = ventas
                    precioT = precio
                
                cursor.execute("SELECT libro FROM libros WHERE isbn = ?", (id,))
                nombreLibro = cursor.fetchone()
                for nombre in nombreLibro:
                    libro = nombre
                conexion.close()
                
                if resultado is not None:
                    mensaje = (f"Libro: {libro} Cantidad: {cantidad} Precio Total: {precioT}")
                    messagebox.showinfo("Se ha encontrado la venta: ", mensaje)    
                else:
                        messagebox.showinfo("Dato","El libro no tiene ninguna compra")
            else:
                messagebox.showerror("Error", "El ID no existe.")

        def limpiar_campos():
            id_entry.delete(0,END)   


        guardar_button = Button(ventana_totalesLibro, text="Buscar", command=totales)
        guardar_button.pack(pady=10)
            
        limpiar_button = Button(ventana_totalesLibro, text="Limpiar", command=limpiar_campos)
        limpiar_button.pack() 
            
                
        def cargar_libros():
                usuarios = mixdeLibrosVentas()
                tabla_libros.delete(*tabla_libros.get_children())
                for usuario in usuarios:
                    tabla_libros.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3]))
            
        def cargar_libro(event):
                selected_row = tabla_libros.focus()
                if selected_row:
                    values = tabla_libros.item(selected_row)["values"]
                    id_entry.config(state="normal")
                    id_entry.delete(0, END)
                    id_entry.insert(END, values[0])
            
        tabla_frame = Frame(ventana_totalesLibro)
        tabla_frame.pack(pady=10)
        
        tabla_libros = ttk.Treeview(tabla_frame, columns=("ISBN", "Titulo","Cantidad","Total"), show="headings")
        tabla_libros.heading("ISBN", text="ISBN")
        tabla_libros.heading("Titulo", text="Titulo")
        tabla_libros.heading("Cantidad", text="Cantidad")
        tabla_libros.heading("Total", text="Total")
        tabla_libros.pack(side=LEFT, fill=Y)
                
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_libros.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        tabla_libros.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=tabla_libros.yview)
            
        tabla_libros.bind("<ButtonRelease-1>",cargar_libro)
            
        cargar_libros()   
                      
def masYmenos():
        ventana_totalesLibro = Toplevel()
        ventana_totalesLibro.title("LIBRO MAS Y MENOS VENDIDO")
        ventana_totalesLibro.geometry("900x400")

        conexion = connect("libreria.db")
        cursor = conexion.cursor()
        
        sentenciaTupla = "SELECT * FROM ventas"
        cursor.execute(sentenciaTupla)
        ventas = cursor.fetchall()
        
        librosVendidos = []        
        for venta in ventas:
            codigoLibro = venta[2]
            cantidadVendida = venta[3]
            encontrado = False
            for libro in librosVendidos:
                if libro[0] == codigoLibro:
                    libro[2] += cantidadVendida
                    encontrado = True
                    break
            if not encontrado:
                
                sentenciaTuplaL = "SELECT * FROM libros"
                cursor.execute(sentenciaTuplaL)
                libros = cursor.fetchall()
                
                nombreLibro = ""
                for libro in libros:
                    if libro[0] == codigoLibro:
                        nombreLibro = libro[1]
                        break
                librosVendidos.append([codigoLibro, nombreLibro, cantidadVendida])
        #maximo
        maxVendidos = max(librosVendidos, key=cantidadVendidos)
        nombreMasVendido = maxVendidos[1]
        codigoMasVendido = maxVendidos[0]
        cantidadmaxima = maxVendidos[2]
        libroMasVendido = (f"ISBN: {codigoMasVendido}   Titulo: {nombreMasVendido}   Cantidad Vendida: {cantidadmaxima}")
        #minimo
        minVendidos = min(librosVendidos, key = cantidadVendidos)
        nombreMenosVendido = minVendidos[1]
        codigoMenosVendido = minVendidos[0]
        cantidadminima = minVendidos[2]
        libroMenosVendido = (f"ISBN: {codigoMenosVendido}   Titulo: {nombreMenosVendido}   Cantidad Vendida: {cantidadminima}")
        
        lblMayor = Label(ventana_totalesLibro, text = "Libro más vendido:",font=("Arial", 24))
        lblMayor.pack(pady = 30)
        entryMayor = Label(ventana_totalesLibro, text = libroMasVendido,font=("Arial", 12))
        entryMayor.pack()

        lblMenor = Label(ventana_totalesLibro, text = "Libro menos vendido:",font=("Arial", 24))
        lblMenor.pack(pady = 20)
        entryMenor = Label(ventana_totalesLibro, text = libroMenosVendido,font=("Arial", 12))
        entryMenor.pack()

def cantidadVendidos(libro):
    return libro[2]     

def ventaTotalLibreria():

    ventana_totalesLibro = Toplevel()
    ventana_totalesLibro.title("VENTAS TOTALES DE LA LIBRERIA")
    ventana_totalesLibro.geometry("1100x400")

    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    sentencia = "SELECT SUM(precio_total) FROM ventas"
    cursor.execute(sentencia)
    total = cursor.fetchone()[0]

    lbltotal = Label(ventana_totalesLibro, text = "Ventas Totales de la libreria:",font=("Arial", 18))
    lbltotal.pack(pady = 10)
    entrytotal = Label(ventana_totalesLibro, text = total,font=("Arial", 12))
    entrytotal.pack()

    def cargar_libros():
        usuarios = obtener_ventas()
        tabla_ventas.delete(*tabla_ventas.get_children())
        for usuario in usuarios:
            tabla_ventas.insert("", index='end', values=(usuario[0], usuario[1],usuario[2],usuario[3],usuario[4]))

    tabla_frame = Frame(ventana_totalesLibro)
    tabla_frame.pack(pady=10)

    tabla_ventas = ttk.Treeview(tabla_frame, columns=("ID", "Cliente","Libro","Cantidad","Total"), show="headings")
    tabla_ventas.heading("ID", text="ID")
    tabla_ventas.heading("Cliente", text="Titulo")
    tabla_ventas.heading("Libro", text="Precio")
    tabla_ventas.heading("Cantidad", text="Cantidad")
    tabla_ventas.heading("Total", text="Total")
    tabla_ventas.pack(side=LEFT, fill=Y)
    
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla_ventas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    tabla_ventas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tabla_ventas.yview)

    tabla_ventas.bind("<ButtonRelease-1>")

    cargar_libros()

def clienteMayorVenta():
    ventana_totalesLibro = Toplevel()
    ventana_totalesLibro.title("CLIENTE MAYOR VENTA")
    ventana_totalesLibro.geometry("600x200")

    conexion = connect("libreria.db")
    cursor = conexion.cursor()

    sentenciaA = """SELECT c.id,c.nombre,MAX(v.precio_total),v.venta
                 FROM ventas v
                 JOIN clientes c
                 ON (v.id_cliente = c.id)
                 """
    cursor.execute(sentenciaA)
    librosTabla = cursor.fetchall()
    for id, nombre,precio_total, venta in librosTabla:
        mensaje = (f"Id: {id}  Nombre: {nombre}  Cantidad: {venta}  Venta Total: {precio_total}")

    lbltotal = Label(ventana_totalesLibro, text = "Cliente con Mayor venta:",font=("Arial", 18))
    lbltotal.pack(pady = 10)
    entrytotal = Label(ventana_totalesLibro, text = mensaje ,font=("Arial", 12))
    entrytotal.pack()

def clienteMayorVolumen():
    ventana_totalesLibro = Toplevel()
    ventana_totalesLibro.title("CLIENTE MAYOR VENTA")
    ventana_totalesLibro.geometry("600x200")

    conexion = connect("libreria.db")
    cursor = conexion.cursor()

    cursor.execute('SELECT id_cliente FROM ventas GROUP BY id_cliente ORDER BY SUM(venta) DESC LIMIT 1')
    id_cliente_mayor_volumen = cursor.fetchone()[0]

    cursor.execute("SELECT c.id,c.nombre,SUM(v.venta),SUM(v.precio_total) FROM ventas v JOIN clientes c ON (v.id_cliente = c.id) WHERE v.id_cliente = ?",(id_cliente_mayor_volumen,))
    librosTabla = cursor.fetchall()
    for id, nombre,venta, precio_total in librosTabla:
        mensaje = (f"Id: {id}  Nombre: {nombre}  Cantidad: {venta}  Venta Total: {precio_total}")

    lbltotal = Label(ventana_totalesLibro, text = "Cliente con Mayor Volumen de venta:",font=("Arial", 18))
    lbltotal.pack(pady = 10)
    entrytotal = Label(ventana_totalesLibro, text = mensaje ,font=("Arial", 12))
    entrytotal.pack()


