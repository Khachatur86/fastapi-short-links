from fastapi import (
    APIRouter,
    status,
    BackgroundTasks,
)

from schemas.short_url import (
    ShortUrlCreate,
    ShortUrlRead,
)
from api.api_v1.short_urls.crud import storage

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLS"],
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
    background_tasks: BackgroundTasks,
):
    short_url = storage.create(short_url_create)
    background_tasks.add_task(storage.save_state)
    return short_url
