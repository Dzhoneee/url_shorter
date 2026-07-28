from app.db.database import engine
from app.db.base import Base

from app.models.short_url import ShortURL


Base.metadata.create_all(engine)

print("Tables created")