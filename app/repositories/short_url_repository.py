from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.short_url import ShortURL


class ShortURLRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(self, short_url: ShortURL) -> ShortURL:
        self.session.add(short_url)
        self.session.commit()
        self.session.refresh(short_url)
        return short_url

    def get_by_short_code(self, short_code: str) -> ShortURL | None:
        stmt = select(ShortURL).where(ShortURL.short_code == short_code)
        result = self.session.execute(stmt)
        return result.scalar_one_or_none()

    def get_by_original_url(self, original_url: str) -> ShortURL | None:
        stmt = select(ShortURL).where(ShortURL.original_url == original_url)
        result = self.session.execute(stmt)
        return result.scalar_one_or_none()