def create_product(client, sku: str, stock: int, price: float = 5000):
    r = client.post("/products", json={"sku": sku, "name": sku, "price": price, "stock": stock})
    assert r.status_code == 201, r.text
    return r.json()

def test_create_order_reduces_stock(client):
    p = create_product(client, "order-item-1", stock=10, price=5000)

    r = client.post("/orders", json={"items": [{"product_id": p["id"], "qty": 3}]})
    assert r.status_code == 201, r.text
    order = r.json()
    assert order["total"] is not None
    assert len(order["items"]) == 1
    assert order["items"][0]["qty"] == 3

    # stock should be 7 after
    products = client.get("/products").json()
    target = next(x for x in products if x["id"] == p["id"])
    assert target["stock"] == 7

def test_create_order_insufficient_stock(client):
    p = create_product(client, "order-item-2", stock=1, price=5000)

    r = client.post("/orders", json={"items": [{"product_id": p["id"], "qty": 2}]})
    assert r.status_code in (400, 409), r.text  # tergantung implementasi kamu
