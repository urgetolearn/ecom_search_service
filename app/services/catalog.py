class CatalogService:
    def __init__(self):
        self.products = {}
        self.counter = 100

    def add_product(self, product: dict):
        self.counter += 1
        product_id = self.counter
        product["productId"] = product_id
        product["Metadata"] = {}
        self.products[product_id] = product
        return product_id

    def update_metadata(self, product_id: int, metadata: dict):
        if product_id not in self.products:
            return None
        self.products[product_id]["Metadata"].update(metadata)
        return self.products[product_id]

    def search(self, query: str):
        query = query.lower().strip()
        results = []
    
        for p in self.products.values():
            text_score = 0 
            title = p.get("title", "").lower()
            description = p.get("description", "").lower()
            if query in title:
                text_score += 20
            if query in description:
                text_score += 10


        
        if text_score == 0:
            continue

        final_score = text_score
        
        if "sasta" in query or "low price" in query:
            mrp = p.get("mrp", 1)
            price = p.get("price", 0)
            discount = ((mrp - price) / mrp) * 100 if mrp > 0 else 0
            final_score += (discount / 2)

        final_score += (p.get("rating", 0) * 2)
        
        if p.get("stock", 0) > 0:
            final_score += 5

        results.append((final_score, p))

    results.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in results]
catalog_service = CatalogService()
