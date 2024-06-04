
while True:
                            print(tablaventas)
                            print("==============")
                            print("1. Actualizar Cliente")
                            print("2. Actualizar Libro (ISBN)")
                            print("3. Actualizar Cantidad de libro comprados")
                            print("4. Salir")
                            print("==============")
                            opcion = int(input("Ingrese una opción: "))
                            if opcion == 1:
                                while True:
                                    cliente = int(
                                        input("Ingrese el codigo del nuevo cliente 0. para salir: "))
                                    if cliente == 0:
                                        break
                                    else:
                                        if validarIDClientes(cliente):
                                            sentencia = "UPDATE ventas SET id_cliente = ? WHERE id = ?"
                                            parametro = [cliente, codigoVenta]
                                            cursor.execute(sentencia, parametro)
                                            conexion.commit()
                                            print(
                                                "El codigo del cliente ha sido actualizado.")
                                            break
                                        else:
                                            print("El id del cliente no existe.")
                            elif opcion == 2:
    
                                while True:
    
                                    libro = int(
                                        input("Ingrese el ISBN del libro 0. para salir: "))
                                    if libro == 0:
                                        break
                                    else:
                                        if validarLibros:
        
                                            sentenciaInventarioD = "SELECT venta FROM ventas WHERE id_libro = ?"
                                            parametroDe = [libro]
                                            cursor.execute(sentenciaInventarioD,parametroDe)
                                            devolver = cursor.fetchone()
                                            for de in devolver:
                                                devuelto = de
                                            
                                            cantidadVendida = "SELECT venta FROM ventas WHERE id = ?"
                                            parametroCantidad = [codigoVenta]
                                            cursor.execute(
                                                cantidadVendida, parametroCantidad)
                                            cantidad = cursor.fetchone()
                                            for cant in cantidad:
                                                inventario = cant
        
                                            cantidadLimite = "SELECT inventario FROM libros WHERE isbn = ?"
                                            parametroLimite = [libro]
                                            cursor.execute(cantidadLimite,parametroLimite)
                                            limite = cursor.fetchone()
                                            for l in limite:
                                                cantidadLiminte = l
        
                                            sumadeCompra = "SELECT precio FROM libros WHERE isbn = ?"
                                            parametroCompra = [libro]
                                            cursor.execute(
                                                sumadeCompra, parametroCompra)
                                            multiplicado = cursor.fetchone()
                                            for valor in multiplicado:
                                                precio = inventario * valor
                                                
                                            if int(inventario) > 0 and inventario <= cantidadLiminte:
        
                                                sentenciaDevolver = "UPDATE libros SET inventario = ? WHERE isbn = ?"
                                                parametroD = [devuelto,libro]
                                                cursor.execute(sentenciaDevolver,parametroD)
                                                conexion.commit()
                                                
                                                
                                                sentenciaPrecio = "UPDATE ventas SET precio_total = ? WHERE id = ? "
                                                parametroPrecio = [precio, codigoVenta]
                                                cursor.execute(
                                                    sentenciaPrecio, parametroPrecio)
                                                conexion.commit()
            
                                                sentencia = "UPDATE ventas SET id_libro = ? WHERE id = ?"
                                                parametro = [libro, codigoVenta]
                                                cursor.execute(sentencia, parametro)
                                                conexion.commit()
                                                print("Se ha actualizado con exito")
                                                
                                                nuevaCantidad = cantidadLiminte - inventario
                                                nuevosLibros = "UPDATE libros SET inventario = ? WHERE isbn = ?"
                                                nuevo = [nuevaCantidad, libro]
                                                cursor.execute(
                                                    nuevosLibros, nuevo)
                                                conexion.commit()    
        
        
                                                switch += 1
                                                break
                                            else:
                                                print(f"No hay tanta cantidad de libros, solo {cantidadLiminte}")
                                        else:
                                            print(
                                                "No hay libro que tenga el isbn:", libro)
        
                            elif opcion == 3:
    
                                while True:
                                    if switch == 1:
                                        break
                                    isbnLibro = "SELECT id_libro FROM ventas WHERE id = ?"
                                    parametroLibro = [codigoVenta]
                                    cursor.execute(isbnLibro, parametroLibro)
                                    libro = cursor.fetchone()
                                    for codigo in libro:
                                        isbn = codigo
    
                                    cantLibros = "SELECT inventario FROM libros WHERE isbn = ?"
                                    parametroLibro = [isbn]
                                    cursor.execute(cantLibros, parametroLibro)
                                    inventarios = cursor.fetchone()
                                    for inventario in inventarios:
                                        print(f"hay {inventario} libros.")
    
                                    librosCant = int(
                                        input("Ingrese la nueva cantidad de libros a comprar 0. para salir: "))
                                    if librosCant == 0:
                                        break
                                    else:
                                        if librosCant > 0 and librosCant <= inventario:
        
                                            sumadeCompra = "SELECT precio FROM libros WHERE isbn = ?"
                                            parametroPrecio = [isbn]
                                            cursor.execute(sumadeCompra, parametroPrecio)
                                            multiplicado = cursor.fetchone()
                                            for valor in multiplicado:
                                                precio = librosCant * valor
                                            print("Confirmar venta")
                                            print("==============")
                                            print(
                                                f"Cantidad: {librosCant} Valor total: ${precio}")
                                            while True:
                                                if switch == 1:
                                                    break
                                                opcion = input("Ingrese 'si' o 'no': ")
                                                if opcion == "si":
        
                                                    sentencia = "UPDATE ventas SET venta = ? WHERE id = ?"
                                                    parametro = [librosCant, codigoVenta]
                                                    cursor.execute(sentencia,parametro)
                                                    conexion.commit()
        
                                                    sentenciaPrecio = "UPDATE ventas SET precio_total = ? WHERE id = ?"
                                                    parametroTotal = [
                                                        precio, codigoVenta]
                                                    cursor.execute(
                                                        sentenciaPrecio, parametroTotal)
                                                    conexion.commit()
        
                                                    nuevaCantidad = inventario - librosCant
                                                    nuevosLibros = "UPDATE libros SET inventario = ? WHERE isbn = ?"
                                                    nuevo = [nuevaCantidad, isbn]
                                                    cursor.execute(nuevosLibros, nuevo)
                                                    conexion.commit()
        
                                                    print("Se ha actualizado con exito")
                                                    switch = 1
                                                    break
        
                                                elif opcion == "no":
                                                    switch += 1
        
                                                else:
                                                    print(
                                                        "Ingrese una opción valida...")
                                        else:
                                            print(
                                                f"No hay suficientes libros ({inventario})")
                            elif opcion == 4:
                                print("Saliendo")
                                switch = 1
                                break
                            else:
                                print("Ingrese una opción valida")

        elif continuarOsalir == "0":
            print("Saliendo")
            break
        else:
            print("Ingrese una opción valida")