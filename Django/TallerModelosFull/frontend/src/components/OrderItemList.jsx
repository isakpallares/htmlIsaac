import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderItemList = () => {
    const [orderItems, setOrderItems] = useState([]);
    const [orders, setOrders] = useState([]);
    const [products, setProducts] = useState([]);
    const [newOrderItem, setNewOrderItem] = useState({
        order: '',
        producto: '',
        cantidad: 1
    });

    useEffect(() => {
        fetchOrderItems();
        fetchOrders();
        fetchProducts();
    }, []);

    const fetchOrderItems = () => {
        axios.get('http://localhost:8000/api/orderitems/')
            .then(response => setOrderItems(response.data))
            .catch(error => console.error('Error fetching order items:', error));
    };

    const fetchOrders = () => {
        axios.get('http://localhost:8000/api/orders/')
            .then(response => setOrders(response.data))
            .catch(error => console.error('Error fetching orders:', error));
    };

    const fetchProducts = () => {
        axios.get('http://localhost:8000/api/products/')
            .then(response => setProducts(response.data))
            .catch(error => console.error('Error fetching products:', error));
    };

    const addOrderItem = () => {
        axios.post('http://localhost:8000/api/orderitems/', newOrderItem)
            .then(response => {
                setOrderItems([...orderItems, response.data]);
                setNewOrderItem({
                    order: '',
                    producto: '',
                    cantidad: 1
                });
            })
            .catch(error => console.error('Error adding order item:', error));
    };

    const deleteOrderItem = (id) => {
        axios.delete(`http://localhost:8000/api/orderitems/${id}/`)
            .then(() => {
                setOrderItems(orderItems.filter(item => item.id !== id));
            })
            .catch(error => console.error('Error deleting order item:', error));
    };

    const updateOrderItemQuantity = (id, newQuantity) => {
        axios.patch(`http://localhost:8000/api/orderitems/${id}/`, { cantidad: newQuantity })
            .then(response => {
                setOrderItems(orderItems.map(item =>
                    item.id === id ? { ...item, cantidad: newQuantity } : item
                ));
            })
            .catch(error => console.error('Error updating order item quantity:', error));
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewOrderItem(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    return (
        <div className="container">
            <h2>Order Items</h2>
            <div className="mb-4">
                <h3>Add Order Item</h3>
                <div className="form-group">
                    <label>Order:</label>
                    <select
                        className="form-control"
                        name="order"
                        value={newOrderItem.order}
                        onChange={handleChange}
                    >
                        <option value="">Select an order...</option>
                        {orders.map(order => (
                            <option key={order.id} value={order.id}>{order.id}</option>
                        ))}
                    </select>
                </div>
                <div className="form-group">
                    <label>Product:</label>
                    <select
                        className="form-control"
                        name="producto"
                        value={newOrderItem.producto}
                        onChange={handleChange}
                    >
                        <option value="">Select a product...</option>
                        {products.map(product => (
                            <option key={product.id} value={product.id}>{product.nombre}</option>
                        ))}
                    </select>
                </div>
                <div className="form-group">
                    <label>Quantity:</label>
                    <input
                        type="number"
                        className="form-control"
                        name="cantidad"
                        value={newOrderItem.cantidad}
                        onChange={handleChange}
                    />
                </div>
                <button onClick={addOrderItem} className="btn btn-primary">
                    Add Item
                </button>
            </div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Order ID</th>
                        <th>Product</th>
                        <th>Quantity</th>
                        <th>Date Added</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {orderItems.map(item => (
                        <tr key={item.id}>
                            <td>{item.order}</td>
                            <td>{item.producto}</td>
                            <td>{item.cantidad}</td>
                            <td>{item.fecha_anadida}</td>
                            <td>
                                <button onClick={() => deleteOrderItem(item.id)} className="btn btn-danger">
                                    Delete
                                </button>
                                <button onClick={() => updateOrderItemQuantity(item.id, item.cantidad + 1)} className="btn btn-secondary">
                                    +1
                                </button>
                                <button onClick={() => updateOrderItemQuantity(item.id, item.cantidad - 1)} className="btn btn-secondary">
                                    -1
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OrderItemList;
