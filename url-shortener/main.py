from fastapi import FastAPI, Request

app = FastAPI(
    title="URL Shortener",
)


@app.get("/")
def read_root(
    request: Request,
    name: str = "World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": "Hello World",
        "docs": str(docs_url),
    }
