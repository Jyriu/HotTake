from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    username: str = Field(index=True, unique=True, nullable=False, max_length=32)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # relationships
    statements: List["Statement"] = Relationship(back_populates="author")
    votes: List["Vote"] = Relationship(back_populates="voter")