from pydantic import BaseModel
from typing import Optional


class CouponUsage(BaseModel):
    user_id: str
    
class VerifyCouponCodeValidateRequest(BaseModel):
    coupon_code: str
    usage: CouponUsage

class ApplyCouponCodeRequest(BaseModel):
    coupon_code: str
    usage: CouponUsage
class CouponConfig(BaseModel):
    user_total_repeat_count: Optional[int] = None
    user_per_day_repeat_count: Optional[int] = None
    user_per_week_repeat_count: Optional[int] = None
    global_total_repeat_count: Optional[int] = None
    
class AddCouponCodeRequest(BaseModel):
    coupon_code: str
    config: CouponConfig