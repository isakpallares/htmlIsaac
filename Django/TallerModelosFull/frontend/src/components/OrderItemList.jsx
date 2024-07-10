import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderItemList = () => {
    const [orderItems, setOrderItems] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/orderitems/')
            .then(response => setOrderItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div className="container">
            <h1>Order Items</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Order</th>
                        <th>Product</th>
                        <th>Quantity</th>
                        <th>Date Added</th>
                    </tr>
                </thead>
                <tbody>
                    {orderItems.map(orderItem => (
                        <tr key={orderItem.id}>
                            <td>{orderItem.order_id}</td>
                            <td>{orderItem.producto_nombre}</td>
                            <td>{orderItem.cantidad}</td>
                            <td>{orderItem.fecha_anadida}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default OrderItemList;
