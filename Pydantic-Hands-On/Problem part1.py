from pydantic import BaseModel, field_validator
from typing import Optional

class UserAddress(BaseModel):
    city: str
    pincode: int

    @field_validator('city')
    @classmethod
    def city_length_check(cls, value: str) -> str:
        if len(value)<3:
            raise ValueError('Minimum 3 characters required')
        else:
            return value
    
    @field_validator('pincode')
    @classmethod
    def pin_six_digits(cls, value: int) -> int:
        if len(str(value)) !=6:
            raise ValueError('Pin Code must be exactly 6 digits')
        else:
            return value

class User(BaseModel):
    user_id: int
    name: str
    email: str
    age: int
    address: UserAddress
    is_premium: Optional[bool] = False

    @field_validator('email')
    @classmethod
    def valid_email(cls, value: str) -> str:
        if value.endswith('@masai.com'):
            return value
        else:
            raise ValueError('Not a valid email')
            
    @field_validator('age')
    @classmethod
    def age_less_than_18(cls, value: int) -> int:
        if value < 18:
            raise ValueError('Age must be atleast 18')
        return value
        
#Sample data for testing (This data does not give errors)
try:
    data = {
    "user_id": 103,
    "name": "Seetha",
    "email": "Seetharaman@masai.com",
    "age": 22,
    "address": {"city": "Mumbai", "pincode": 110001},
    "isPremium": "True"
    }

    user = User(**data)

    print("Validation Successful for user: ", user.name)
    print(f"Address: {user.address.city}, {user.address.pincode}")

except Exception as e:
    print("Validation error: ", e)
