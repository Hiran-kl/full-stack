const express = require('express');
const cors = require('cors'); // ✅ You were requiring './cors' — use the installed 'cors' package
const sqlite3 = require('sqlite3').verbose(); // ✅ Typo: 'splite3' ➡ 'sqlite3'

const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Connect to SQLite database
const db = new sqlite3.Database('./ecommerce.db'); // ✅ './' to indicate relative path

// ✅ GET top 5 products by quantity sold
app.get('/api/top-products', (req, res) => {
    const query = `
        SELECT product_name, SUM(quantity) as total_sold
        FROM orders
        GROUP BY product_name
        ORDER BY total_sold DESC
        LIMIT 5;
    `; // ✅ Fixed malformed SQL and string quotes

    db.all(query, [], (err, rows) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json(rows);
    });
});

// ✅ Get orders for a user by user ID
app.get('/api/orders/:userId', (req, res) => {
    const userId = req.params.userId;

    db.all('SELECT * FROM orders WHERE user_id = ?', [userId], (err, rows) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        if (rows.length === 0) {
            return res.status(404).json({ error: 'No orders found for this user' });
        }
        res.json(rows);
    });
});

// ✅ Get stock info for a product
app.get('/api/stock/:productId', (req, res) => {
    const productId = req.params.productId;

    db.get('SELECT stock FROM products WHERE product_id = ?', [productId], (err, row) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        if (!row) {
            return res.status(404).json({ stock: 'Product not found' });
        }
        res.json(row);
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
