from sqlite3 import *
from sqlLibreria import conectar_db, desconectar_db

def validarVenta(valor):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas WHERE id = ?', (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
def validarNombreClientes(valor):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nombre = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
def validarIDClientes(valor):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
def validadIDClientesVentas(valor):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ventas WHERE id_cliente = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
def validarLibros(valor):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE isbn = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
def validarLibrosVentas(valor):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ventas WHERE id_libro = ?", (valor,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado
#CLIENTES
def obtener_Clientes():
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexion.close()
    return clientes

def ingresar_cliente(nombre,id):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes(id,nombre) VALUES (?,?)", (id,nombre))
    conexion.commit()
    conexion.close()
    print("Cliente agregado con exito.")
    
def actualizar_Cliente(idNuevo,nombre,id):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE clientes SET id = ?,nombre = ? WHERE id = ?", (idNuevo,nombre, id))
    conexion.commit()
    conexion.close()

def actualizar_nombre(id,nombre):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE clientes SET nombre = ? WHERE id = ?", (nombre, id))
    conexion.commit()
    conexion.close()   

def buscar_Cliente(id):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id =?", id)
    buscar = cursor.fetchall()
    conexion.close()
    return buscar

def eliminar_Cliente(id):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    id = int(id)
    cursor.execute("DELETE FROM clientes WHERE id =(?)", (id,))
    conexion.commit()
    conexion.close()
    print("Cliente eliminado con exito.")
    
#LIBROS
def obtener_Libros():
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conexion.close()
    return libros

def ingresar_Libros(isbn,libro,precio,inventario):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros(isbn,libro,precio,inventario) VALUES(?,?,?,?)",(isbn,libro,precio,inventario))
    conexion.commit()
    conexion.close()
    print("Libro agregado con exito.")

def actualizar_Libro(isbn,isbnNuevo,libro,libroNuevo,precio,precioNuevo,inventario,inventarioNuevo):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    if isbnNuevo != "" :
        cursor.execute("UPDATE libros SET isbn = ? WHERE isbn = ?",(isbnNuevo,isbn))
        conexion.commit()
        print("isbn Actualizado con exito.")
    else:
        pass
    if isbn != "" and isbnNuevo == "":
        pass
        
    if libroNuevo != "":
        cursor.execute("UPDATE libros SET libro = ? WHERE isbn = ?", (libroNuevo,isbn))
        conexion.commit()
        print("Libro Actualizado con exito.")
    else:
        pass

    if precioNuevo != "":
        cursor.execute("UPDATE libros SET precio = ? WHERE isbn = ?",(precioNuevo,isbn))
        conexion.commit()
        print("Precio Actualizado con exito.")
    else:
        pass

    if inventarioNuevo != "":
        cursor.execute("UPDATE libros SET inventario = ? WHERE isbn = ?", (inventarioNuevo,isbn))
        conexion.commit()
        print("Inventario Actualizado con exito.")
    else:
        pass

    conexion.close()
    
def buscar_libro(isbn):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE isbn = ?", (isbn))
    buscarLibros = cursor.fetchall()
    conexion.close()
    return buscarLibros
    
def eliminar_libro(isbn):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
    conexion.commit()
    conexion.close()
    print("Libro eliminado con exito.")

#VENTAS

def obtener_ventas():
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ventas")
    ventas = cursor.fetchall()
    conexion.close()
    return ventas
    
def ingresar_ventas(id_cliente,id_libro,venta):
 
    conexion = connect("libreria.db") 
    cursor = conexion.cursor()
    cantLibros = "SELECT inventario FROM libros WHERE isbn = ?"
    parametroLibro = [id_libro]
    cursor.execute(cantLibros, parametroLibro)
    inventarios = cursor.fetchone()
    for inventario in inventarios:
        inventarioLibros = inventario

    precio = cursor.execute("SELECT precio FROM libros WHERE isbn = ?",(id_libro,))
    multiplicado = precio.fetchone()
    for valor in multiplicado:
        valorP = valor
        precioTotal = valorP * venta

    librosRestados = inventarioLibros - int(venta)

    cursor.execute(
    "SELECT id FROM ventas ORDER BY id DESC LIMIT 1")
    ultimoid = cursor.fetchone()
        
    if ultimoid:
        ultimoid = ultimoid[0]
        ultimoNumero = int(
            ultimoid.split('-')[1])
    else:
        ultimoNumero = 1035
        
    for i in range(5, 21, 5):   
        numeroNuevo = ultimoNumero + 5
        nuevoId = "V-" + \
            str(numeroNuevo)



    cursor.execute("UPDATE libros SET inventario = ? WHERE isbn = ?", (librosRestados,id_libro))
    conexion.commit()
    
    cursor.execute("INSERT INTO ventas(id,id_cliente,id_libro,venta,precio_total) VALUES(?,?,?,?,?)", (nuevoId,id_cliente,id_libro,venta,precioTotal))

    conexion.commit()
    conexion.close()
    print("Venta agregada con exito.")

def cantidadLibros(id_libro):
    conexion = connect("libreria.db") 
    cursor = conexion.cursor()
    cantLibros = "SELECT inventario FROM libros WHERE isbn = ?"
    parametroLibro = [id_libro]
    cursor.execute(cantLibros, parametroLibro)
    inventarios = cursor.fetchone()
    for inventario in inventarios:
        inventarioLibros = inventario
        
    conexion.close()
    return inventarioLibros
    
def actualizarVentas(id,id_clienteNuevo,id_libroNuevo,id_libro,ventaNueva):
    conexion = connect("libreria.db") 
    cursor = conexion.cursor()   
    
    if id_clienteNuevo != "":
        
        #ACTUALIZAR CLIENTE
        cursor.execute("UPDATE ventas SET id_cliente = ? WHERE id = ?",(id_clienteNuevo,id))
        conexion.commit()
    else:
        pass
    
    if id_libroNuevo != "":
        #ACTUALIZAR ISBN
        
                        #BUSCAR LOS DATOS
        cursor.execute("SELECT inventario FROM libros WHERE isbn = ?",(id_libro,))
        viejo = cursor.fetchone()
        for v in viejo:
            cantidadVieja = v
            
        cursor.execute("SELECT venta FROM ventas WHERE id_libro = ?",(id_libro,))
        devolver = cursor.fetchone()
        for de in devolver:
            devuelto = de + cantidadVieja
        
        cursor.execute("SELECT venta FROM ventas WHERE id = ?",(id,))
        cantidad = cursor.fetchone()
        for cant in cantidad:
            vendido = cant

        
        cursor.execute("SELECT inventario FROM libros WHERE isbn = ?",(id_libroNuevo,))
        limite = cursor.fetchone()
        for l in limite:
            cantidadDeLibros = l
        
        cursor.execute("SELECT precio FROM libros WHERE isbn = ?",(id_libro,))
        multiplicado = cursor.fetchone()
        for valor in multiplicado:
            precio = int(vendido * valor)
        
        
        #DEVOLVER LIBROS
        cursor.execute("UPDATE libros SET inventario = ? WHERE isbn = ?",(devuelto,id_libro))
        conexion.commit()
        
        #ACTUALIZAR PRECIO Y CANTIDAD VENDIDA
        cursor.execute("UPDATE ventas SET precio_total = ? WHERE id = ?",(precio,id))
        conexion.commit()
        
        cursor.execute("UPDATE ventas SET id_libro = ? WHERE id = ?",(id_libroNuevo,id))
        conexion.commit()
        
        nuevaCantidad = cantidadDeLibros - vendido
        cursor.execute("UPDATE libros SET inventario = ? WHERE isbn = ?",(nuevaCantidad,id_libroNuevo))
        conexion.commit()
    else:
        pass
    if id_libro != "" and id_libroNuevo == "":
        pass
    
    if ventaNueva != "":
        #ACTUALIZAR CANTIDAD DE LIBROS
        
        #TOMAR INVENTARIO 
        
        cursor.execute("SELECT inventario FROM libros WHERE isbn = ?",(id_libro,))
        inventarioNuevo = cursor.fetchone()
        for inv in inventarioNuevo:
            inventarioCantidad = inv
            
        #TOMAR EL PRECIO TOTAL 
        cursor.execute("SELECT precio FROM libros WHERE isbn = ?",(id_libro,))
        multiplicador = cursor.fetchone()
        for mu in multiplicador:
            precioCantidad = int(mu) * int(ventaNueva)
            
            
        cursor.execute("SELECT venta FROM ventas WHERE id = ?",(id,))
        venta = cursor.fetchone()
        for vent in venta:
            cantidadVenta = vent
        
        #ACTUALIZAR CANTIDAD
    
        cursor.execute("UPDATE ventas SET venta = ? WHERE id = ?",(ventaNueva,id))
        conexion.commit()
        
        cursor.execute("UPDATE ventas SET precio_total = ? WHERE id = ?",(precioCantidad,id))
        conexion.commit()

        nuevaCantidadLibros = int(inventarioCantidad) + int(cantidadVenta) - int(ventaNueva) 
        cursor.execute("UPDATE libros SET inventario = ? WHERE isbn = ?",(nuevaCantidadLibros,id_libro))
        conexion.commit()
        
    else:
        pass
    
    conexion.close()

def eliminarVentas(id):
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM ventas WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    print("Venta eliminado con exito.")


def mixdeClienteVentas():
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT ventas.id, ventas.id_cliente, ventas.id_libro, ventas.venta, ventas.precio_Total, clientes.nombre FROM ventas JOIN clientes ON ventas.id_cliente = clientes.id")
    mix = cursor.fetchall()
    conexion.close()
    return mix

def mixdeLibrosVentas():
    conexion = connect("libreria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT libros.isbn, libros.libro,ventas.venta,ventas.precio_Total FROM libros JOIN ventas ON libros.isbn = ventas.id_libro")
    mix = cursor.fetchall()
    conexion.close()
    return mix
