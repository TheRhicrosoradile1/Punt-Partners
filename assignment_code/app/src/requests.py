from pydantic import BaseModel
from typing import Optional



class VerifyCouponCodeValidateRequest():
    pass

class ApplyCouponCodeRequest():
    pass

class CouponConfig(BaseModel):
    user_total_repeat_count: Optional[int] = None
    user_per_day_repeat_count: Optional[int] = None
    user_per_week_repeat_count: Optional[int] = None
    global_total_repeat_count: Optional[int] = None
    
class AddCouponCodeRequest():
    coupon_code: str
    config: CouponConfig