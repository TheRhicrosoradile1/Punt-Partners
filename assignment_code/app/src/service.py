from datetime import datetime
from .repository import *
from .data import coupon_db
# data import coupon_db
from .requests import (CouponUsage, CouponConfig)


async def add_coupon_repeat_count_service(
    coupon_code: str, config: CouponConfig
):
    if coupon_code in coupon_db:
        raise HTTPException(status_code=400, detail="Coupon code already exists")

    coupon_db[coupon_code] = {
        "config": config.dict(),
        "usage": {},
    }

    # TODO: CHANGE THIS TO A LOGGER STATEMENT
    print(f"coupon_code ; {coupon_code} with config {config.dict()}")
    
    return {"message": "Coupon repeat count added successfully"}


async def verify_coupon_service(coupon_code: str, user_id: str):
    if coupon_code not in coupon_db:
        raise HTTPException(status_code=404, detail="Coupon code not found")

    config = coupon_db[coupon_code]["config"]
    current_time = datetime.now()

    # Check global total repeat count
    if config.global_total_repeat_count is not None:
        if config.global_total_repeat_count <= len(coupon_db[coupon_code]["usage"]):
            raise HTTPException(
                status_code=400, detail="Coupon code reached global total repeat count"
            )

    # Check user total repeat count
    if config.user_total_repeat_count is not None:
        if user_id in coupon_db[coupon_code]["usage"]:
            if coupon_db[coupon_code]["usage"][user_id] >= config.user_total_repeat_count:
                raise HTTPException(
                    status_code=400, detail="Coupon code reached user total repeat count"
                )

    # Check user daily repeat count
    if config.user_per_day_repeat_count is not None:
        if user_id in coupon_db[coupon_code]["usage"]:
            last_usage_time = coupon_db[coupon_code]["usage"][user_id]
            if last_usage_time.date() == current_time.date():
                raise HTTPException(
                    status_code=400, detail="Coupon code reached user daily repeat count"
                )

    # Check user weekly repeat count
    if config.user_per_week_repeat_count is not None:
        if user_id in coupon_db[coupon_code]["usage"]:
            last_usage_time = coupon_db[coupon_code]["usage"][user_id]
            if (current_time - last_usage_time).days < 7:
                raise HTTPException(
                    status_code=400, detail="Coupon code reached user weekly repeat count"
                )

    return {"message": "Coupon code is valid"}



async def apply_coupon_service(coupon_code: str, usage: CouponUsage):
    print(f"usage: {usage}")
    if coupon_code not in coupon_db:
        raise HTTPException(status_code=404, detail="Coupon code not found")
    print(f"coupon_db data : {coupon_db}")
    current_time = datetime.now()
    coupon_db[coupon_code]["usage"][usage.user_id] = current_time

    print(f"coupon data : {coupon_db[coupon_code]}")
    
    return {"message": "Coupon code applied successfully"}

