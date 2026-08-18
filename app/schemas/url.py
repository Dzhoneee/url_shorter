from pydantic import BaseModel


class CreateShortUrlRequest(BaseModel):
    url: str

class CreateShortUrlResponse(BaseModel):
    short_code: str