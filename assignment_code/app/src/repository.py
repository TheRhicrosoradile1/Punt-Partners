from fastapi import HTTPException

# Filler Object to store data for coupons
coupon_db = {} 

def add_coupon_code(coupon_code):
    if coupon_code in coupon_db:
        raise HTTPException(status_code=400, detail="Coupon code already exists")

    coupon_db[coupon_code] = {
        "config": config.dict(),
        "usage": {},
    }