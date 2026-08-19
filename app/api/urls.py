from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas.url import CreateShortUrlRequest
from app import dependencies as dp
from app.services.short_url_service import ShortURLService
from app.db.models.short_url import ShortURL



router = APIRouter()


@router.get("/")
def root():
    return {"message": "Short URL service is running"}


@router.post("/urls")
def create_short_url(request: CreateShortUrlRequest, 
                     service: ShortURLService = Depends(dp.get_short_url_service)):
    created_url: ShortURL = service.create_short_url(request.url)
    return {
        "original_url": created_url.original_url,
        "short_code": created_url.short_code,
        "short_url": f"http://192.168.1.17:8000/" + created_url.short_code
    }

@router.get("/{short_code}")
def redirection(short_code: str,
                service: ShortURLService = Depends(dp.get_short_url_service)):
    url: ShortURL | None = service.repository.get_by_short_code(short_code)
    if url is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return RedirectResponse(url=url.original_url, status_code=307)
