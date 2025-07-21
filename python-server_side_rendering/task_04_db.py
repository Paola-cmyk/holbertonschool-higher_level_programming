from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# JSON reader
def read_json_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

# CSV reader
def read_csv_file(filepath):
    products = []
    try:
        with open(filepath, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = {
                    "id": int(row.get("id", 0)),
                    "name": row.get("name", ""),
                    "category": row.get("category", ""),
                    "price": float(row.get("price", 0.0))
                }
                products.append(product)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products

# SQLite reader
def read_sqlite_data(db_path, product_id=None):
    if not os.path.exists(db_path):
        print("Database file not found.")
        return []

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception as e:
        print(f"Database error: {e}")
        return []

# Route
@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_data('products.db', product_id)
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filter by id for JSON and CSV if needed
    if product_id is not None and source != 'sql':
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"
    elif source == 'sql' and product_id is not None and not products:
        error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
