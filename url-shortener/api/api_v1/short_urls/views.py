from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
)
from .crud import storage
from .dependencies import prefetch_short_url

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLS"],
)


@router.get("/", response_model=list[ShortUrl])
def read_short_urls():
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrl,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url_create: ShortUrlCreate,
):
    return storage.create(short_url_create)


@router.get(
    "/short-urls/{slug}",
    response_model=ShortUrl,
)
def read_short_urls_details(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
):
    return url
