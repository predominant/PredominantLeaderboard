import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello Leaderboards"}


@app.get("/leaderboard/{game}/{level}", response_model=list[schemas.Score])
async def get_scores(game: str, level: str, db: Session = Depends(get_db)):
    scores = crud.get_level_leaderboard(db, game=game, level=level)
    return scores


@app.post("/leaderboard/{game}/{level}/{player}/{score}", response_model=schemas.Score)
async def record_score(game: str, level: str, player: str, score: int, db: Session = Depends(get_db)):
    db_score = crud.set_score(db, game=game, level=level, player=player, score=score)
    return db_score

