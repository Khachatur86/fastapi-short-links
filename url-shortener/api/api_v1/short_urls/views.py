from typing import Annotated

from annotated_types import Len
from fastapi import (
    APIRouter,
    Depends,
    status,
    Form,
)
from pydantic import AnyHttpUrl

from schemas.short_url import ShortUrl
from .crud import SHORT_URLS
from .dependencies import prefetch_short_url

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLS"],
)


@router.get("/", response_model=list[ShortUrl])
def read_short_urls():
    return SHORT_URLS


@router.post(
    "/",
    response_model=ShortUrl,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    target_url: Annotated[AnyHttpUrl, Form()],
    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
        Form(),
    ],
):
    return ShortUrl(
        target_url=target_url,
        slug=slug,
    )


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
