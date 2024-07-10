import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CategoryList = () => {
    const [categories, setCategories] = useState([]);
    const [nombre, setNombre] = useState('');
    const [descripcion, setDescripcion] = useState('');

    useEffect(() => {
        fetchCategories();
    }, []);

    const fetchCategories = () => {
        axios.get('http://localhost:8000/api/categories/')
            .then(response => setCategories(response.data))
            .catch(error => console.error('Error fetching data:', error));
    };

    const addCategory = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/categories/', {
            nombre: nombre,
            descripcion: descripcion
        })
        .then(response => {
            setCategories([...categories, response.data]);
            setNombre('');
            setDescripcion('');
        })
        .catch(error => console.error('Error anadiendo categoria:', error));
    };

    const deleteCategory = (id) => {
        axios.delete(`http://localhost:8000/api/categories/${id}/`)
            .then(response => {
                setCategories(categories.filter(category => category.id !== id));
            })
            .catch(error => console.error('Error eliminando categoria:', error));
    };

    return (
        <div className="container">
            <h1>Categorias</h1>
            <form onSubmit={addCategory}>
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
                    <label>Description</label>
                    <input
                        type="text"
                        className="form-control"
                        value={descripcion}
                        onChange={(e) => setDescripcion(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary">añadir categoria</button>
            </form>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>nombre</th>
                        <th>descripcion</th>
                        <th>acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {categories.map(category => (
                        <tr key={category.id}>
                            <td>{category.nombre}</td>
                            <td>{category.descripcion}</td>
                            <td>
                                <button onClick={() => deleteCategory(category.id)} className="btn btn-danger">eliminar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default CategoryList;
