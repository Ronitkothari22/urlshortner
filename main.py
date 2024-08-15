from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from schemas import URLBase, URLInfo
from services import create_db_url, get_db_url_by_key
import validators

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=URLInfo)
def create_url(url: URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Invalid URL")
    db_url = create_db_url(db, url.target_url)
    return db_url

@app.get("/{url_key}")
def forward_to_target_url(url_key: str, db: Session = Depends(get_db)):
    db_url = get_db_url_by_key(db, url_key)
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise HTTPException(status_code=404, detail="URL not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
