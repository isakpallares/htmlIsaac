import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);
    const [nombre, setNombre] = useState('');
    const [email, setEmail] = useState('');
    const [telefono, setTelefono] = useState('');

    useEffect(() => {
        fetchCustomers();
    }, []);

    const fetchCustomers = () => {
        axios.get('http://localhost:8000/api/customers/')
            .then(response => setCustomers(response.data))
            .catch(error => console.error('Error fetching data:', error));
    };

    const addCustomer = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/customers/', {
            nombre: nombre,
            email: email,
            telefono: telefono
        })
        .then(response => {
            setCustomers([...customers, response.data]);
            setNombre('');
            setEmail('');
            setTelefono('');
        })
        .catch(error => console.error('Error anadiendo cliente:', error));
    };

    const deleteCustomer = (id) => {
        axios.delete(`http://localhost:8000/api/customers/${id}/`)
            .then(response => {
                setCustomers(customers.filter(customer => customer.id !== id));
            })
            .catch(error => console.error('Error eliminando cliente:', error));
    };

    return (
        <div className="container">
            <h1>Clientes</h1>
            <form onSubmit={addCustomer}>
                <div className="form-group">
                    <label>Nombre</label>
                    <input
                        type="text"
                        className="form-control"
                        value={nombre}
                        onChange={(e) => setNombre(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Email</label>
                    <input
                        type="email"
                        className="form-control"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Phone</label>
                    <input
                        type="text"
                        className="form-control"
                        value={telefono}
                        onChange={(e) => setTelefono(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary">Añadir Cliente</button>
            </form>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Email</th>
                        <th>Telefono</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map(customer => (
                        <tr key={customer.id}>
                            <td>{customer.nombre}</td>
                            <td>{customer.email}</td>
                            <td>{customer.telefono}</td>
                            <td>
                                <button onClick={() => deleteCustomer(customer.id)} className="btn btn-danger">Eliminar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default CustomerList;
