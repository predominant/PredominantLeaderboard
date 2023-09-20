from pydantic import BaseModel


class ScoreBase(BaseModel):
    game: str
    level: str
    player: str
    score: float


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int

    class Config:
        from_attributes = True
