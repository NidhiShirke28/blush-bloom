from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

MONGO_URI = "mongodb+srv://nidhishirke552_db_user:E4rPSQ6PU5sTFBCD@cluster0.ybjpzds.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["blushbloom"]

@app.route("/")
def home():
    return "MongoDB Connected Successfully"

@app.route("/add-product")
def add_product():
    product = {
        "name": "Lipstick",
        "price": 499,
        "category": "Makeup"
    }
    db.products.insert_one(product)
    return "Product Added Successfully"

@app.route("/products")
def get_products():
    products = list(db.products.find({}, {"_id": 0}))
    return jsonify(products)

@app.route("/add-all-products")
def add_all_products():

    products = [
        {"name":"Rose Cream","price":299,"category":"skincare"},
        {"name":"Aloe Vera Gel","price":249,"category":"skincare"},
        {"name":"Vitamin C Serum","price":199,"category":"skincare"},
        {"name":"Mint Cleanser","price":289,"category":"skincare"},

        {"name":"Herbal Hair Oil","price":199,"category":"haircare"},
        {"name":"Frizz Control Serum","price":249,"category":"haircare"},
        {"name":"Keratin Hair Mask","price":299,"category":"haircare"},
        {"name":"Hibiscus Shampoo","price":199,"category":"haircare"},

        {"name":"Shea Butter Lotion","price":249,"category":"bodycare"},
        {"name":"Detan Body Scrub","price":279,"category":"bodycare"},
        {"name":"Cherry Body Wash","price":199,"category":"bodycare"},
        {"name":"Vanilla Body Mist","price":229,"category":"bodycare"},

        {"name":"Lip & Cheek Tint","price":199,"category":"makeup"},
        {"name":"Nude Lipstick","price":149,"category":"makeup"},
        {"name":"Highlighter","price":199,"category":"makeup"},
        {"name":"Eyeshadow Palette","price":299,"category":"makeup"}
    ]

    db.products.insert_many(products)

    return "All products inserted successfully"

if __name__ == "__main__":
    app.run(debug=True)
   