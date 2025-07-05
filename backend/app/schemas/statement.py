from datetime import datetime

from sqlmodel import Field, SQLModel

from .user import UserOut


class StatementBase(SQLModel):
    """Shared properties for statements."""

    content: str = Field(max_length=280)


class CreateStatement(StatementBase):
    """Schema for creating a new statement."""

    pass


class StatementOut(StatementBase):
    """Schema returned to clients, including author and vote counts."""

    id: int
    created_at: datetime
    author: UserOut
    hot_votes: int
    bs_votes: int

    class Config:
        orm_mode = True 