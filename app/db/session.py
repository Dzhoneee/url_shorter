from sqlalchemy.orm import sessionmaker

from app.db.database import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()