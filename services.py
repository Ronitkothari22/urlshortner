from sqlalchemy.orm import Session
from database import URL
import secrets

def create_random_key(length: int = 5) -> str:
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(secrets.choice(chars) for _ in range(length))

def create_db_url(db: Session, target_url: str) -> URL:
    key = create_random_key()
    while get_db_url_by_key(db, key):
        key = create_random_key()

    db_url = URL(target_url=target_url, key=key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_db_url_by_key(db: Session, key: str) -> URL:
    return db.query(URL).filter(URL.key == key).first()