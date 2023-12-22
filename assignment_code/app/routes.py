from typing import Annotated

from fastapi import Depends,Header, HTTPException,APIRouter

from src.requests import ( AddCouponCodeRequest,ApplyCouponCodeRequest,VerifyCouponCodeValidateRequest )
from src.responses import ( AddCouponCodeResponse,VerifyCouponCodeValidateResponse,ApplyCouponCodeResponse )
from src.service import ( verify_coupon_service,add_coupon_repeat_count_service,apply_coupon_service )


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

@router.get("/verify_coupon/user/{user_id}/coupon-code/{coupon_code}",response_model=None)
async def verify_coupon_code_validity(coupon_code : str,user_id:str):
    return await verify_coupon_service(coupon_code,user_id)


@router.post("/add_coupon_repeat_count/")
async def add_coupon_code_repeats(request_body : AddCouponCodeRequest = Depends()):
    coupon_code = request_body.coupon_code
    config  = request_body.config
    return await add_coupon_repeat_count_service(coupon_code,config)


@router.post("/apply_coupon/")
async def apply_coupon(request_body : ApplyCouponCodeRequest):
    coupon_code = request_body.coupon_code
    config  = request_body.usage
    print("REACHED APPLY COUPON CODE: %s" % coupon_code)
    
    return await apply_coupon_service(coupon_code,config)
