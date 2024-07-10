import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CategoryList from './components/CategoryList';
import ProductList from './components/ProductList';
import CustomerList from './components/CustomerList';
import OrderList from './components/OrderList';
import OrderItemList from './components/OrderItemList';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/categories" element={<CategoryList/>} />
                <Route path="/orders" element={<OrderList />} />
                <Route path="/customers" element={<CustomerList />} />
                <Route path="/products" element={<ProductList />} />
                <Route path="/orderitems" element={<OrderItemList />} /> 
            </Routes>
        </Router>
    )
}

export default App;
