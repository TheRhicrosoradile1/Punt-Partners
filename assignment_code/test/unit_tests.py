import json
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_add_coupon_repeat_count():
    coupon_code = "TEST123"
    config = {
        "user_total_repeat_count": 3,
        "user_per_day_repeat_count": 1,
        "user_per_week_repeat_count": 1,
        "global_total_repeat_count": 10000,
    }
    response = client.post(f"/add_coupon_repeat_count/{coupon_code}", json=config)
    assert response.status_code == 200
    assert response.json() == {"message": "Coupon repeat count added successfully"}

def test_verify_valid_coupon():
    coupon_code = "TEST123"
    user_id = "user1"
    client.post(f"/add_coupon_repeat_count/{coupon_code}", json={"global_total_repeat_count": 1})
    client.post(f"/apply_coupon/{coupon_code}", json={"user_id": user_id})
    response = client.post(f"/verify_coupon/{coupon_code}", json={"user_id": user_id})
    assert response.status_code == 200
    assert response.json() == {"message": "Coupon code is valid"}

def test_verify_invalid_coupon():
    coupon_code = "TEST456"
    user_id = "user2"
    client.post(f"/add_coupon_repeat_count/{coupon_code}", json={"user_total_repeat_count": 1})
    client.post(f"/apply_coupon/{coupon_code}", json={"user_id": user_id})
    client.post(f"/apply_coupon/{coupon_code}", json={"user_id": user_id})
    response = client.post(f"/verify_coupon/{coupon_code}", json={"user_id": user_id})
    assert response.status_code == 400

def test_apply_coupon():
    coupon_code = "TEST789"
    user_id = "user3"
    client.post(f"/add_coupon_repeat_count/{coupon_code}", json={"global_total_repeat_count": 2})
    response = client.post(f"/apply_coupon/{coupon_code}", json={"user_id": user_id})
    assert response.status_code == 200
    assert response.json() == {"message": "Coupon code applied successfully"}

def test_apply_coupon_invalid():
    coupon_code = "INVALIDCODE"
    user_id = "user4"
    response = client.post(f"/apply_coupon/{coupon_code}", json={"user_id": user_id})
    assert response.status_code == 404
