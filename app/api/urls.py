from fastapi import APIRouter
from app.schemas.url import CreateShortUrlRequest


router = APIRouter()


@router.get("/")
def root():
    return {"message": "Short URL service is running"}


@router.post("/urls")
def create_short_url(request: CreateShortUrlRequest):
    return {
        "original_url": request.url,
        "short_code": "abcdef",
        "short_url": f"http://localhost:8000/abcdef"
    }