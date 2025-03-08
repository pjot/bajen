from fastapi import FastAPI
from pydantic import BaseModel
import slugs


app = FastAPI()


class SlugsResponse(BaseModel):
    slugs: list[str]


@app.get("/api/slugs")
def get_slugs() -> SlugsResponse:
    return SlugsResponse(slugs=slugs.get())


@app.delete("/api/slugs/{slug}")
def delete_slug(slug: str) -> SlugsResponse:
    stored = slugs.get()
    stored.remove(slug)
    slugs.store(stored)
    return SlugsResponse(slugs=stored)


@app.put("/api/slugs/{slug}")
def add_slug(slug: str) -> SlugsResponse:
    stored = slugs.get()
    stored.append(slug)
    slugs.store(stored)
    return SlugsResponse(slugs=stored)
