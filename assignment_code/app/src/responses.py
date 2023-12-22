from pydantic import BaseModel

from typing import Optional

class Error():
    error_msg:str = None
    error_code:str =None 
    class Config:
        arbitrary_types_allowed=True
    
class GenResponse(BaseModel):
    status_code : int
    message : Optional[str]
    error : Optional[Error]
    class Config:
        arbitrary_types_allowed=True
    
class AddCouponCodeResponse(GenResponse):
    pass

class VerifyCouponCodeValidateResponse(GenResponse):
    pass

class ApplyCouponCodeResponse(GenResponse):
    pass