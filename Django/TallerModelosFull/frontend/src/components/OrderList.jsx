import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderList = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/orders/')
            .then(response => setOrders(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div className="container">
            <h1>Orders</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Customer</th>
                        <th>Order Date</th>
                        <th>Completed</th>
                        <th>Transaction ID</th>
                    </tr>
                </thead>
                <tbody>
                    {orders.map(order => (
                        <tr key={order.id}>
                            <td>{order.customer_nombre}</td>
                            <td>{order.fecha_pedido}</td>
                            <td>{order.completado ? 'Yes' : 'No'}</td>
                            <td>{order.id_transaccion}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default OrderList;
