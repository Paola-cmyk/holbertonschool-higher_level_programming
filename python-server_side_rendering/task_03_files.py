from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv_file(filepath):
    products = []
    try:
        with open(filepath, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert fields as necessary
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
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id is not None:
        products = [product for product in products if product["id"] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
