from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session
from fastapi import FastAPI, Request

from app.db.seed import seed_admin


def init_database(app: FastAPI):
    settings = app.state.settings

    # Create the engine
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=settings.SQLALCHEMY_ECHO, future=True)
    app.state.engine = engine

    # Create session factory
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True, class_=Session)
    app.state.SessionLocal = SessionLocal

    # Create tables based on SQLModel models
    SQLModel.metadata.create_all(engine)

    # Seed initial data
    with SessionLocal() as db:
        seed_admin(db, settings)
        #seed_products(db)
        #seed_recipes(db)


def get_db(request: Request):
    SessionLocal = request.app.state.SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()