import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderList = () => {
    const [orders, setOrders] = useState([]);
    const [customers, setCustomers] = useState([]);
    const [newOrder, setNewOrder] = useState({
        customer: '',
        id_transaccion: ''
    });

    useEffect(() => {
        fetchOrders();
        fetchCustomers();
    }, []);

    const fetchOrders = () => {
        axios.get('http://localhost:8000/api/orders/')
            .then(response => setOrders(response.data))
            .catch(error => console.error('Error fetching orders:', error));
    };

    const fetchCustomers = () => {
        axios.get('http://localhost:8000/api/customers/')
            .then(response => setCustomers(response.data))
            .catch(error => console.error('Error fetching customers:', error));
    };

    const addOrder = () => {
        axios.post('http://localhost:8000/api/orders/', newOrder)
            .then(response => {
                setOrders([...orders, response.data]);
                setNewOrder({ customer: '', id_transaccion: '' });
            })
            .catch(error => console.error('Error adding order:', error));
    };

    const deleteOrder = (orderId) => {
        axios.delete(`http://localhost:8000/api/orders/${orderId}/`)
            .then(() => {
                setOrders(orders.filter(order => order.id !== orderId));
            })
            .catch(error => console.error('Error deleting order:', error));
    };

    return (
        <div className="container">
            <h1>Orders</h1>
            <div className="mb-4">
                <h2>Add Order</h2>
                <div className="form-group">
                    <label>Customer:</label>
                    <select
                        className="form-control"
                        value={newOrder.customer}
                        onChange={(e) => setNewOrder({ ...newOrder, customer: e.target.value })}
                    >
                        <option value="">Select a customer</option>
                        {customers.map(customer => (
                            <option key={customer.id} value={customer.id}>{customer.nombre}</option>
                        ))}
                    </select>
                </div>
                <div className="form-group">
                    <label>Transaction ID:</label>
                    <input
                        type="text"
                        className="form-control"
                        value={newOrder.id_transaccion}
                        onChange={(e) => setNewOrder({ ...newOrder, id_transaccion: e.target.value })}
                    />
                </div>
                <button onClick={addOrder} className="btn btn-primary">
                    Add Order
                </button>
            </div>
            {orders.map(order => (
                <div key={order.id} className="mb-4">
                    <h3>Order ID: {order.id}</h3>
                    <p>Customer: {order.customer_nombre}</p>
                    <p>Transaction ID: {order.id_transaccion}</p>
                    <button onClick={() => deleteOrder(order.id)} className="btn btn-danger">
                        Delete Order
                    </button>
                </div>
            ))}
        </div>
    );
}

export default OrderList;
