from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from database import Base


class Score(Base):
    __tablename__ = 'scores'

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    game: Mapped[str] = Column(String, index=True)
    level: Mapped[str] = Column(String, index=True)
    player: Mapped[str] = Column(String, index=True)
    score: Mapped[float] = Column(Float, index=True, default=0)
