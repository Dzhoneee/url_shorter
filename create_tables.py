from app.db.database import engine
from app.db.base import Base


Base.metadata.create_all(engine)

print("Tables created")