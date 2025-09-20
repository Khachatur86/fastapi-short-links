from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from .dependencies import prefetch_short_url
from .crud import SHORT_URLS
from schemas.short_url import ShortUrl

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLS"],
)


@router.get("/", response_model=list[ShortUrl])
def get_short_urls():
    return SHORT_URLS


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
