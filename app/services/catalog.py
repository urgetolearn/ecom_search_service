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
        query = query.lower()
        results = []

        for p in self.products.values():
            score = 0

            if query in p["title"].lower():
                score += 5
            if query in p["description"].lower():
                score += 3

            # Cheap bias for "sasta"
            if "sasta" in query:
                score += max(0, (p["mrp"] - p["price"]) / 1000)

            score += p["rating"]

            results.append((score, p))

        results.sort(reverse=True, key=lambda x: x[0])
        return [r[1] for r in results]


catalog_service = CatalogService()
