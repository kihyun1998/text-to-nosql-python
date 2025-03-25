from fastapi import FastAPI
from pymongo import MongoClient
from dummy_data import generate_dummy_users, generate_dummy_orders, generate_dummy_products

app = FastAPI()

client = MongoClient("mongodb://mongo:27017")
db = client["test_db"]

@app.post("/init")
def init_all():
    db["users"].drop()
    db["products"].drop()
    db["orders"].drop()

    users = generate_dummy_users(10)
    products = generate_dummy_products(10)
    orders = generate_dummy_orders(users, products, 20)

    db["users"].insert_many(users)
    db["products"].insert_many(products)
    db["orders"].insert_many(orders)

    return {
        "users": len(users),
        "products": len(products),
        "orders": len(orders),
        "message": "Collections initialized"
    }
