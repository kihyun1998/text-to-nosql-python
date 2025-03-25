from datetime import datetime, timedelta
from bson import ObjectId
import random

def generate_dummy_users(n=10):
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    countries = ["Korea", "USA", "Japan", "Germany"]
    tags_pool = ["ai", "music", "sports", "gaming", "tech"]
    roles = ["user", "admin", "moderator"]

    users = []
    for _ in range(n):
        user = {
            "_id": ObjectId(),
            "name": random.choice(names),
            "age": random.randint(18, 60),
            "isActive": random.choice([True, False]),
            "email": f"user{random.randint(1000,9999)}@example.com",
            "country": random.choice(countries),
            "tags": random.sample(tags_pool, k=random.randint(1, 3)),
            "createdAt": datetime.utcnow() - timedelta(days=random.randint(0, 365)),
            "role": random.choice(roles)
        }
        users.append(user)
    return users

def generate_dummy_products(n=10):
    names = ["Laptop", "Phone", "Keyboard", "Shoes", "Headphones"]
    categories = ["electronics", "fashion", "gaming"]

    products = []
    for _ in range(n):
        product = {
            "_id": ObjectId(),
            "name": random.choice(names),
            "price": round(random.uniform(10, 500), 2),
            "inStock": random.choice([True, False]),
            "category": random.choice(categories),
        }
        products.append(product)
    return products

def generate_dummy_orders(users, products, n=20):
    statuses = ["pending", "shipped", "cancelled"]

    orders = []
    for _ in range(n):
        user = random.choice(users)
        product = random.choice(products)
        order = {
            "userId": user["_id"],
            "productId": product["_id"],
            "quantity": random.randint(1, 5),
            "status": random.choice(statuses),
            "orderedAt": datetime.utcnow() - timedelta(days=random.randint(0, 60))
        }
        orders.append(order)
    return orders
