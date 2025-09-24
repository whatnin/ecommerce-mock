from flask import Flask
from flask_cors import CORS

products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "description": "Noise-canceling over-ear headphones",
        "price": 99.99,
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "description": "Track your fitness and notifications",
        "price": 149.99,
        "image_url": "https://via.placeholder.com/150"
    }
]

app = Flask(__name__)
CORS(app)

@app.route('/api/health')
def health():
    return {'status': 'OK'}

@app.route('/api/products', methods=['GET'])
def get_products():
    return {"products": products}

if __name__ == '__main__':
    app.run(port=5000, debug=True)
