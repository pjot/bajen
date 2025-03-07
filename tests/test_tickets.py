from unittest.mock import patch
import json

import tickets


@patch("requests.get")
def test_extracts_games(mocked_get):
    with open("tests/page-data.json") as f:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = json.load(f)

    test_slug = "2024-12-12-20-00-uefa-women-s-champions-league-hammarby-fc-barcelona"
    expected = [
        tickets.Game(
            slug=test_slug,
            home="Hammarby IF",
            away="FC Barcelona",
            tickets=21800,
        )
    ]
    assert tickets.from_site([test_slug]) == expected


def test_can_store_data():
    game = tickets.Game(
        slug="hej",
        home="Bajen",
        away="ajk",
        tickets=12345,
    )

    tickets.save([game])

    stored_games = tickets.read()

    assert stored_games == {"hej": game}
