from fastapi import (
    APIRouter,
    status,
    Depends,
)
from api.api_v1.short_urls.dependencies import save_storage_state


from schemas.short_url import (
    ShortUrlCreate,
    ShortUrlRead,
)
from api.api_v1.short_urls.crud import storage

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLS"],
    dependencies=[Depends(save_storage_state)],
)


@router.get("/", response_model=list[ShortUrlRead])
def read_short_urls():
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrlRead,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url_create: ShortUrlCreate,
):
    short_url = storage.create(short_url_create)
    return short_url
