from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.repositories.short_url_repository import ShortURLRepository
from app.services.short_url_service import ShortURLService


def get_short_url_repository(
        session: Session = Depends(get_session)
) -> ShortURLRepository:
    return ShortURLRepository(session)


def get_short_url_service(
        repository: ShortURLRepository = Depends(get_short_url_repository)
) -> ShortURLService:
    return ShortURLService(repository)