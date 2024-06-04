INSERT INTO clientes(id,nombre)
VALUES (3101,"Maria");

INSERT INTO clientes(id,nombre)
VALUES (3102,"Pedro");

INSERT INTO clientes(id,nombre)
VALUES (3103,"Laura");

INSERT INTO libros(isbn,libro,precio,inventario)
VALUES (12552,"iliada",5300,25);

INSERT INTO libros(isbn,libro,precio,inventario)
VALUES (12553,"Platero",2500,10);

INSERT INTO libros(isbn,libro,precio,inventario)
VALUES (12554,"Cien",3600,35);

INSERT INTO ventas(id,id_cliente,id_libro,venta,precio_Total)
VALUES ("V-1020",3100,12552,4,21200);

INSERT INTO ventas(id,id_cliente,id_libro,venta,precio_Total)
VALUES ("V-1025",3103,12553,2,5000);

INSERT INTO ventas(id,id_cliente,id_libro,venta,precio_Total)
VALUES ("V-1030",3100,12554,3,10800);

INSERT INTO ventas(id,id_cliente,id_libro,venta,precio_Total)
VALUES ("V-1035",3101,12553,9,22500);






select * from clientes



