def test_create_product_success(client):
    payload = {"sku": "drnk-01", "name": "Teh Pucuk", "price": 4000, "stock": 10}
    r = client.post("/products", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["sku"] == "drnk-01"
    assert data["stock"] == 10
    assert "price" in data

def test_create_product_duplicate_sku_conflict(client):
    payload = {"sku": "drnk-02", "name": "Aqua", "price": 3500, "stock": 10}
    r1 = client.post("/products", json=payload)
    assert r1.status_code == 201, r1.text

    r2 = client.post("/products", json=payload)
    assert r2.status_code == 409, r2.text

def test_list_products_pagination(client):
    # create some products
    for i in range(5):
        client.post("/products", json={"sku": f"sku-{i}", "name": f"Item {i}", "price": 1000 + i, "stock": 10})

    r = client.get("/products?limit=2&offset=0")
    assert r.status_code == 200, r.text
    data = r.json()
    assert isinstance(data, list)
    assert len(data) <= 2
