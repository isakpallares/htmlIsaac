CREATE TABLE clientes(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

;CREATE TABLE libros(
    isbn INTEGER PRIMARY KEY,
    libro TEXT NOT NULL,
    precio DECIMAL NOT NULL,
    inventario INTEGER DEFAULT (0)
);

CREATE TABLE ventas(
    id TEXT PRIMARY KEY,
    id_cliente INTEGER,
    id_libro INTEGER,
    venta INTEGER NOT NULL,
    precio_Total DECIMAL NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_libro) REFERENCES libros(isbn) 
);
