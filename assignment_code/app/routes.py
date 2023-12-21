from typing import Annotated

from fastapi import Depends,Header, HTTPException,APIRouter

from .src.requests import AddCouponCodeRequest,ApplyCouponCodeRequest,VerifyCouponCodeValidateRequest
router = APIRouter()

#Route to check the health of the service
@router.get("/health")
async def health_check():
    """
    Return the health of the service 
        200 for health status 
        any other for signifiying error or downtime
    """
    return 200

@router.get("/verify_coupon/{coupon_code}")
async def verify_coupon_code_validity(VerifyCouponCodeValidateRequest):
    pass


@router.post("/add_coupon_repeat_count/{coupon_code}")
async def add_coupon_code_repeats(AddCouponCodeRequest):
    pass


@router.post("/apply_coupon/{coupon_code}")
async def apply_coupon(ApplyCouponCodeRequest):
    if coupon_code not in coupon_db:
        raise HTTPException(status_code=404, detail="Coupon code not found")

    current_time = datetime.now()
    coupon_db[coupon_code]["usage"][usage.user_id] = current_time

    return {"message": "Coupon code applied successfully"}
