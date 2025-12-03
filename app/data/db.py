from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import FastAPI, Request

#from config import settings
#from config import Config
#from app import crud
from app.data.models import User, UserCreate
from app.core.security import hash_password, verify_password

SQLALCHEMY_DATABASE_URI = "sqlite:///./products.db"
SQLALCHEMY_ECHO = False

FIRST_SUPERUSER = "admin@example.com"
FIRST_SUPERUSER_PASSWORD = "changethis"

def init_database(app: FastAPI):
    #config = app.state.config

    # Create the engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_ECHO, future=True)
    app.state.engine = engine

    # Create session factory
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True, class_=Session)
    app.state.SessionLocal = SessionLocal

    # Create tables based on SQLModel models
    SQLModel.metadata.create_all(engine)

    # Seed initial data
    with SessionLocal() as db:
        #init_admin(db, app)
        seed_admin(db)
        #init_products(db)
        #init_recipes(db)



# move to seed
def seed_admin(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)

    user = db.exec(select(User).where(User.email == FIRST_SUPERUSER)).first()
    if not user:
        user_in = UserCreate(email=FIRST_SUPERUSER, password=FIRST_SUPERUSER_PASSWORD, is_superuser=True)
        user = create_user(session=db, user_create=user_in)


# move to crud
def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": hash_password(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj




def get_db(request: Request):
    SessionLocal = request.app.state.SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()