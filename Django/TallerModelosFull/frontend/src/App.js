import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CategoryList from './components/CategoryList';
import ProductList from './components/ProductList';
import CustomerList from './components/CustomerList';
import OrderList from './components/OrderList';
import OrderItemList from './components/OrderItemList';

function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/categories" component={CategoryList} />
                    <Route path="/products" component={ProductList} />
                    <Route path="/customers" component={CustomerList} />
                    <Route path="/orders" component={OrderList} />
                    <Route path="/orderitems" component={OrderItemList} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
