import requests
from bs4 import BeautifulSoup
import random
import time

BASE_URL = "https://www.gsmarena.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_iphone_models():
    url = f"{BASE_URL}/apple-phones-48.php"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    phones = soup.select(".makers li a")
    products = []

    for phone in phones:
        name = phone.text.strip()

        products.append({
            "title": name,
            "description": "Apple iPhone smartphone",
            "price": random.randint(35000, 120000),   # market simulated
            "mrp": random.randint(120000, 140000),
            "rating": round(random.uniform(3.8, 4.8), 1),
            "stock": random.randint(0, 50),
            "unitsSold": random.randint(1000, 200000),
            "metadata": {
                "storage": random.choice(["64GB", "128GB", "256GB", "512GB"]),
                "color": random.choice(["black", "white", "red", "blue"]),
                "brand": "Apple"
            }
        })

    return products
