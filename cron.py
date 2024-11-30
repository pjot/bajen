import tickets
import push
import config
from datetime import datetime

print("---")
print(f"Running cron at {datetime.now()}")

stored_games = tickets.read()
live_games = tickets.from_site(config.tracked_slugs())
tickets.save(live_games)

for game in live_games:
    print("Live game:", game)
    stored = stored_games.get(game.slug)
    print("Stored game:", stored)
    stored_tickets = stored.tickets if stored else 0

    if stored_tickets < game.tickets:
        title = f"{game.home} - {game.away}"

        diff = game.tickets - stored_tickets
        print(f"Increased by {diff}, sending push")
        message = f"Sålda biljetter: {game.tickets} (+{diff})"

        push.send(title, message)
    else:
        print("No increase, no push")
