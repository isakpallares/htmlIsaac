import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [nombre, setNombre] = useState('');
    const [precio, setPrecio] = useState('');
    const [stock, setStock] = useState('');
    const [categoria, setCategoria] = useState('');
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetchProducts();
        fetchCategories();
    }, []);

    const fetchProducts = () => {
        axios.get('http://localhost:8000/api/products/')
            .then(response => setProducts(response.data))
            .catch(error => console.error('Error fetching data:', error));
    };

    const fetchCategories = () => {
        axios.get('http://localhost:8000/api/categories/')
            .then(response => setCategories(response.data))
            .catch(error => console.error('Error fetching data:', error));
    };

    const addProduct = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/products/', {
            nombre: nombre,
            precio: parseFloat(precio),
            stock: parseInt(stock),
            categoria: parseInt(categoria)
        })
        .then(response => {
            setProducts([...products, response.data]);
            setNombre('');
            setPrecio('');
            setStock('');
            setCategoria('');
        })
        .catch(error => console.error('Error anadiendo producto:', error));
    };

    const deleteProduct = (id) => {
        axios.delete(`http://localhost:8000/api/products/${id}/`)
            .then(response => {
                setProducts(products.filter(product => product.id !== id));
            })
            .catch(error => console.error('Error eliminando producto:', error));
    };

    return (
        <div className="container">
            <h1>Productos</h1>
            <form onSubmit={addProduct}>
                <div className="form-group">
                    <label>nombre</label>
                    <input
                        type="text"
                        className="form-control"
                        value={nombre}
                        onChange={(e) => setNombre(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Precio</label>
                    <input
                        type="number"
                        className="form-control"
                        value={precio}
                        onChange={(e) => setPrecio(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Stock</label>
                    <input
                        type="number"
                        className="form-control"
                        value={stock}
                        onChange={(e) => setStock(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Categoria</label>
                    <select
                        className="form-control"
                        value={categoria}
                        onChange={(e) => setCategoria(e.target.value)}
                    >
                        <option value="">Select a category</option>
                        {categories.map(category => (
                            <option key={category.id} value={category.id}>{category.nombre}</option>
                        ))}
                    </select>
                </div>
                <button type="submit" className="btn btn-primary">Añadir Producto</button>
            </form>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Precio</th>
                        <th>Stock</th>
                        <th>Categoria</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td>{product.nombre}</td>
                            <td>{product.precio}</td>
                            <td>{product.stock}</td>
                            <td>{product.categoria_nombre}</td>
                            <td>
                                <button onClick={() => deleteProduct(product.id)} className="btn btn-danger">Eliminar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default ProductList;
