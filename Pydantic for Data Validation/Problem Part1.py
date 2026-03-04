from pydantic import BaseModel, field_validator

class UserRegister(BaseModel):
    username: str
    email: str
    age: int

    @field_validator('username')
    @classmethod
    def username_min_five(cls, value: str) -> str:
        if len(value) < 5:
            raise ValueError('Username should have more than 5 characters')
        return value

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
            raise ValueError('Age msut be atleast 18')
        return value
try:
    username = input("Enter Username: ")
    email = input("Enter email address: ")
    age = input("Enter age: ")

    user = UserRegister(username=username, email=email, age=age)
    print("Validated Successfully!")
    print("Username: ", user.username)
    print("Email: ", user.email)
    print("Age: ", user.age)
except Exception as e:
    print("Validation Error: ", e)