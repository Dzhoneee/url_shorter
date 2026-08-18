from app.repositories.short_url_repository import ShortURLRepository
from app.db.models.short_url import ShortURL
from app.core.generator import generate_code


class ShortURLService:
    def __init__(self, repository: ShortURLRepository):
        self.repository = repository

    def create_short_url(self, original_url: str) -> ShortURL:
        if not original_url.startswith(("http://", "https://")):
            original_url = "http://" + original_url
        existing_url = self.repository.get_by_original_url(original_url)
        if existing_url is not None:
            return existing_url
        while True:
            short_code = generate_code()
            if self.repository.get_by_short_code(short_code) is None:
                break
        new_model = ShortURL(original_url=original_url, short_code=short_code)
        return self.repository.create(new_model)
