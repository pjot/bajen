import requests
import json
from pydantic import BaseModel

URL = "https://hammarbyfotboll.se/page-data/matcher/page-data.json"


class Game(BaseModel):
    slug: str
    home: str
    away: str
    tickets: int

    def __str__(self):
        return f"{self.home} - {self.away} ({self.tickets})"


def from_site(slugs: list[str]) -> list[Game]:
    site_data = requests.get(URL).json()

    tracked_games = [
        Game(
            slug=g["slug"]["current"],
            home=g["local"]["title"],
            away=g["external"]["title"],
            tickets=g["ticketsSold"],
        )
        for g in site_data["result"]["pageContext"]["matches"]
        if g["slug"]["current"] in slugs
    ]
    return tracked_games


def read() -> dict[str, Game]:
    try:
        with open("data.json") as f:
            games = json.load(f)
            return {slug: Game(**g) for slug, g in games.items()}
    except:
        return {}


def save(games: list[Game]):
    with open("data.json", "w") as f:
        json_data = {g.slug: g.model_dump() for g in games}
        json.dump(json_data, f, indent=4)
