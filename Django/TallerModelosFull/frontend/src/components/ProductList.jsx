import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [editingProduct, setEditingProduct] = useState(null);
    const [editedProduct, setEditedProduct] = useState({
        nombre: '',
        precio: '',
        stock: '',
        categoria: ''
    });
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetchProducts();
        fetchCategories();
    }, []);

    const fetchProducts = () => {
        axios.get('http://localhost:8000/api/products/')
            .then(response => setProducts(response.data))
            .catch(error => console.error('Error fetching products:', error));
    };

    const fetchCategories = () => {
        axios.get('http://localhost:8000/api/categories/')
            .then(response => setCategories(response.data))
            .catch(error => console.error('Error fetching categories:', error));
    };

    const editProduct = (product) => {
        setEditingProduct(product.id);
        setEditedProduct({
            nombre: product.nombre,
            precio: product.precio,
            stock: product.stock,
            categoria: product.categoria.id
        });
    };

    const cancelEdit = () => {
        setEditingProduct(null);
        setEditedProduct({
            nombre: '',
            precio: '',
            stock: '',
            categoria: ''
        });
    };

    const updateProduct = (productId) => {
        axios.put(`http://localhost:8000/api/products/${productId}/`, editedProduct)
            .then(response => {
                setProducts(products.map(product => 
                    product.id === productId ? response.data : product
                ));
                setEditingProduct(null);
                setEditedProduct({
                    nombre: '',
                    precio: '',
                    stock: '',
                    categoria: ''
                });
            })
            .catch(error => console.error('Error updating product:', error));
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setEditedProduct(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    return (
        <div className="container">
            <h1>Product List</h1>
            {products.map(product => (
                <div key={product.id} className="mb-4">
                    {editingProduct === product.id ? (
                        <div>
                            <h3>Edit Product</h3>
                            <div className="form-group">
                                <label>Name:</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    name="nombre"
                                    value={editedProduct.nombre}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="form-group">
                                <label>Price:</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    name="precio"
                                    value={editedProduct.precio}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="form-group">
                                <label>Stock:</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    name="stock"
                                    value={editedProduct.stock}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="form-group">
                                <label>Category:</label>
                                <select
                                    className="form-control"
                                    name="categoria"
                                    value={editedProduct.categoria}
                                    onChange={handleChange}
                                >
                                    <option value="">Select a category</option>
                                    {categories.map(category => (
                                        <option key={category.id} value={category.id}>{category.nombre}</option>
                                    ))}
                                </select>
                            </div>
                            <button onClick={() => updateProduct(product.id)} className="btn btn-primary mr-2">
                                Save
                            </button>
                            <button onClick={cancelEdit} className="btn btn-secondary">
                                Cancel
                            </button>
                        </div>
                    ) : (
                        <div>
                            <h3>{product.nombre}</h3>
                            <p>Price: ${product.precio}</p>
                            <p>Stock: {product.stock}</p>
                            <p>Category: {product.categoria.nombre}</p>
                            <button onClick={() => editProduct(product)} className="btn btn-primary mr-2">
                                Edit
                            </button>
                        </div>
                    )}
                </div>
            ))}
        </div>
    );
}

export default ProductList;
