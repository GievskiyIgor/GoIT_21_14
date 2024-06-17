from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from src.database.models import Role

class UserSchema(BaseModel):
    
     
    """
        UserSchema
    
        :param username
        :type username: str
        :param password
        :type password: str
       
        
    """ 
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int =1
    username: str
    email: EmailStr
    avatar: str
    role: Role
    
    class Config:
        from_attributes = True
        
        
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    
class RequestEmail(BaseModel):
    email: EmailStr    
    
    