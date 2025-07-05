from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    """Shared properties between all user schemas."""

    email: EmailStr
    username: str = Field(max_length=32)


class CreateUser(UserBase):
    """Schema used when registering a new user (client input)."""

    password: str = Field(min_length=8)


class UserOut(UserBase):
    """Schema returned in API responses."""

    id: int
    created_at: datetime

    class Config:
        orm_mode = True 