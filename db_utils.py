from typing import Optional, Type

from sqlalchemy.orm import Session

from models import Users


def add_user_to_db(db: Session, username: str, email: str) -> Users:
    """
    This function adds a new user to the database.

    Parameters
    ----------
    db: Session
    username: str
    email: str

    Returns
    -------
    Users
    """
    new_user = Users(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db: Session, username: str) -> Optional[Type[Users]]:
    """
    This function searches for a user by username.

    Parameters
    ----------
    db: Session
    username: str

    Returns
    -------
    Optional[Type[Users]]
    """
    return db.query(Users).filter_by(username=username).first()
