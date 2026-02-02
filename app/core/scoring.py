from app.core.config import WEIGHTS
from app.utils.nlp import fuzzy_match

def text_score(product, query):
    score = 0
    for word in query.split():
        if word in product.title.lower():
            score += 2
        elif fuzzy_match(word, product.title.lower()):
            score += 1
    return score

def rating_score(product):
    return product.rating

def price_score(product, intent, price_limit):
    if intent == "CHEAP":
        return 1 / product.price
    if price_limit and product.price > price_limit:
        return -1
    return 1

def stock_score(product):
    return 1 if product.stock > 0 else -5

def rank_products(products, query, intent, price_limit):
    ranked = []
    for p in products:
        score = (
            WEIGHTS["text"] * text_score(p, query) +
            WEIGHTS["rating"] * rating_score(p) +
            WEIGHTS["price"] * price_score(p, intent, price_limit) +
            WEIGHTS["stock"] * stock_score(p)
        )
        ranked.append((score, p))

    ranked.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in ranked]
