from sqlmodel import SQLModel

from ..database.models.vote import VoteType


class VoteIn(SQLModel):
    """Client payload for voting on a statement."""

    vote_type: VoteType 