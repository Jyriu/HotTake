from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel


class VoteType(str, Enum):
    """Allowed vote values."""

    HOT = "hot"
    BS = "bs"


class Vote(SQLModel, table=True):
    """Represents a single vote cast by a user on a statement."""

    __table_args__ = (UniqueConstraint("voter_id", "statement_id"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    vote_type: VoteType = Field(nullable=False, description="Either 'hot' or 'bs'.")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # foreign keys
    voter_id: int = Field(foreign_key="user.id", nullable=False)
    statement_id: int = Field(foreign_key="statement.id", nullable=False)

    # relationships
    voter: "User" = Relationship(back_populates="votes")
    statement: "Statement" = Relationship(back_populates="votes")