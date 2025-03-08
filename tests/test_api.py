from fastapi.testclient import TestClient
from api import app
import slugs
import pytest
import httpx


def _slugs(response: httpx.Response) -> set[str]:
    return set(response.json()["slugs"])


@pytest.fixture()
def api():
    slugs.store([])
    return TestClient(app)


def test_api(api):
    response = api.get("/api/slugs")
    assert _slugs(response) == set()

    response = api.put("/api/slugs/one-game")
    assert _slugs(response) == {"one-game"}
    response = api.get("/api/slugs")
    assert _slugs(response) == {"one-game"}

    response = api.put("/api/slugs/another-game")
    assert _slugs(response) == {"one-game", "another-game"}
    response = api.get("/api/slugs")
    assert _slugs(response) == {"one-game", "another-game"}

    response = api.delete("/api/slugs/one-game")
    assert _slugs(response) == {"another-game"}
    response = api.get("/api/slugs")
    assert _slugs(response) == {"another-game"}
