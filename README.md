# bajen
Send push to mobile phone when sold tickets are updated on hammarbyfotboll.se

# Instructions
This is meant to be run as a cron job. There is an example in crontab.txt

There is also a small API to manage the tracked slugs.

Needed preparation:
* Create an account at Pushover
* Generate API key at Pushover. The API token and user key should be added to config.py
* Run API: `make api`
* Add slugs to track `curl -XPOST hostname/api/slugs/some-slug`
