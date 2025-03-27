from datetime import datetime, timedelta
from bson import ObjectId
import random

def generate_dummy_users(n=10):
    names = ["Alice Kim", "Bob Lee", "Charlie Park", "David Cho", "Eve Han"]
    genders = ["male", "female"]
    tiers = ["bronze", "silver", "gold", "platinum"]
    languages = ["Korean", "English", "Japanese"]
    currencies = ["KRW", "USD", "JPY"]

    users = []
    for _ in range(n):
        dob = datetime.utcnow() - timedelta(days=random.randint(20 * 365, 50 * 365))
        join_date = datetime.utcnow() - timedelta(days=random.randint(0, 1000))
        expires_at = join_date + timedelta(days=random.randint(180, 365))

        user = {
            "_id": ObjectId(),
            "fullName": random.choice(names),
            "dateOfBirth": dob.strftime("%Y-%m-%d"),
            "gender": random.choice(genders),
            "email": f"user{random.randint(1000,9999)}@example.com",
            "phone": f"+82-10-{random.randint(1000,9999)}-{random.randint(1000,9999)}",
            "isVerified": random.choice([True, False]),
            "preferences": {
                "language": random.choice(languages),
                "currency": random.choice(currencies)
            },
            "membership": {
                "tier": random.choice(tiers),
                "joinedAt": join_date,
                "expiresAt": expires_at
            }
        }
        users.append(user)
    return users

def generate_dummy_products(n=10):
    names = ["Laptop", "Keyboard", "Headphones", "Shoes", "Monitor"]
    categories = ["electronics", "fashion", "gaming"]

    products = []
    for _ in range(n):
        discount_value = round(random.uniform(0, 50), 2)
        discount_expires = datetime.utcnow() + timedelta(days=random.randint(1, 30))

        product = {
            "_id": ObjectId(),
            "name": random.choice(names),
            "sku": f"SKU-{random.randint(1000,9999)}",
            "category": random.choice(categories),
            "price": round(random.uniform(50, 500), 2),
            "discount": {
                "amount": discount_value,
                "expiresAt": discount_expires
            },
            "options": random.sample(["RGB", "blue switch", "wireless", "waterproof"], k=2),
            "inStock": random.choice([True, False])
        }
        products.append(product)
    return products

def generate_dummy_orders(users, products, n=20):
    statuses = ["paid", "pending", "cancelled"]
    methods = ["courier", "pickup", "drone"]

    orders = []
    for _ in range(n):
        user = random.choice(users)
        product = random.choice(products)
        order_time = datetime.utcnow() - timedelta(days=random.randint(0, 30))
        shipped_time = order_time + timedelta(days=random.randint(1, 5))

        order = {
            "_id": ObjectId(),
            "userId": user["_id"],
            "productId": product["_id"],
            "quantity": random.randint(1, 5),
            "paymentStatus": random.choice(statuses),
            "shipping": {
                "address": f"Seoul #{random.randint(100, 999)}",
                "method": random.choice(methods),
                "shippedAt": shipped_time
            },
            "orderedAt": order_time
        }
        orders.append(order)
    return orders
