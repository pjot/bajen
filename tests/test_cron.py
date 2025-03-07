import tickets
import cron
import push


def test_generates_messages():
    stored = {
        "changed": tickets.Game(
            slug="changed",
            home="Bajen",
            away="ajk",
            tickets=123,
        ),
        "same": tickets.Game(
            slug="same",
            home="Bajen",
            away="diff",
            tickets=12,
        ),
    }
    live = [
        tickets.Game(
            slug="changed",
            home="Bajen",
            away="ajk",
            tickets=1123,
        ),
        tickets.Game(
            slug="same",
            home="Bajen",
            away="diff",
            tickets=12,
        ),
    ]

    messages = list(cron.make_messages(stored, live))

    expected = push.Message(
        title="Bajen - ajk",
        message="Sålda biljetter: 1123 (+1000)",
    )
    assert messages == [expected]
