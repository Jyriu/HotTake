from typing import Optional

from sqlmodel import SQLModel


class Token(SQLModel):
    """Returned after successful authentication."""

    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    """Payload extracted from JWT (used internally in deps)."""

    user_id: Optional[int] = None 