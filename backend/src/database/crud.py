from backend.src.database.base import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()