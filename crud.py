from sqlalchemy.orm import Session
from sqlalchemy import desc, and_

import models
import schemas


def get_level_leaderboard(db: Session, game: str, level: str):
    return (
        db
        .query(models.Score)
        .filter(and_(models.Score.game == game, models.Score.level == level))
        .order_by(desc(models.Score.score))
        .limit(10)
        .all()
    )


def set_score(db: Session, game: str, level: str, player: str, score: float):
    db_score = (
        db
        .query(models.Score)
        .filter(and_(models.Score.game == game, models.Score.level == level, models.Score.player == player))
        .first()
    )
    if db_score is None:
        db_score = models.Score(
            game=game,
            level=level,
            player=player,
            score=score,
        )
        db.add(db_score)
        db.commit()
        db.refresh(db_score)
    else:
        db_score.score = score
        db.commit()
    return db_score
