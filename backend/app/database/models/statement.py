from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Statement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=280, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    author_id: int | None = Field(foreign_key="user.id", nullable=False)
    author: "User" = Relationship(back_populates="statements")

    hot_votes: int = Field(default=0, nullable=False)
    bs_votes: int = Field(default=0, nullable=False)

    votes: List["Vote"] = Relationship(back_populates="statement")