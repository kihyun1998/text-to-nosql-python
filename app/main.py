from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import json_util
import json
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

# MongoDB 객체를 JSON으로 변환하는 헬퍼 함수
def parse_json(data):
    return json.loads(json_util.dumps(data))

# 모든 사용자 조회 API
@app.get("/users")
def get_all_users():
    try:
        users = list(db["users"].find({}))
        return parse_json(users)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve users: {str(e)}")

# 모든 제품 조회 API
@app.get("/products")
def get_all_products():
    try:
        products = list(db["products"].find({}))
        return parse_json(products)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve products: {str(e)}")

# 모든 주문 조회 API
@app.get("/orders")
def get_all_orders():
    try:
        orders = list(db["orders"].find({}))
        return parse_json(orders)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve orders: {str(e)}")