from datetime import datetime
from typing import Generator

import tickets
import push
import slugs


def make_messages(
    stored_games: dict[str, tickets.Game], live_games: list[tickets.Game]
) -> Generator[push.Message]:
    for game in live_games:
        stored = stored_games.get(game.slug)
        stored_tickets = stored.tickets if stored else 0

        print("Live game:", game)
        print("Stored game:", stored)

        if stored_tickets < game.tickets:
            title = f"{game.home} - {game.away}"

            diff = game.tickets - stored_tickets
            message = f"Sålda biljetter: {game.tickets} (+{diff})"

            print(f"Increased by {diff}, sending push")
            yield push.Message(
                title=title,
                message=message,
            )


def run():
    print("---")
    print(f"Running cron at {datetime.now()}")

    tracked_slugs = slugs.get()
    if not tracked_slugs:
        print("No tracked slugs.")
        return

    print("Tracked slugs:")
    for s in tracked_slugs:
        print(s)

    stored_games = tickets.read()
    live_games = tickets.from_site(slugs.get())
    tickets.save(live_games)

    for message in make_messages(stored_games, live_games):
        push.send(message)
    else:
        print("No increase, no push")


if __name__ == "__main__":
    run()
