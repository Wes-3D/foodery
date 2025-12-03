from sqlmodel import Session

from app.db.models import User, UserCreate
from app.core.security import hash_password, verify_password

# move to crud
def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": hash_password(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

