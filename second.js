npx create-react-app frontend
cd frontend
npm install axios 


import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [topProducts, setTopProducts] = useState([]);
    const [order, setOrder] = useState(null);
    const [stock, setStock] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:5000/api/top-products')
            .then(response => setTopProducts(response.data))
            .catch(error => console.error('Error fetching top products:', error));
    }, []);

    const fetchOrder = (userId) => {
        axios.get(`http://localhost:5000/api/orders/${userId}`)
            .then(response => setOrder(response.data))
            .catch(error => console.error('Error fetching order:', error));
    };

    const fetchStock = (productId) => {
        axios.get(`http://localhost:5000/api/stock/${productId}`)
            .then(response => setStock(response.data))
            .catch(error => console.error('Error fetching stock:', error));
    };

    return (
        <div>
            <h1>Top Products</h1>
            <ul>
                {topProducts.map(product => (
                    <li key={product.product_name}>{product.product_name} - {product.total_sold}</li>
                ))}
            </ul>
            {/* Add UI for fetching orders and stock */}
        </div>
    );
}
export default App;