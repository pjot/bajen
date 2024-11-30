# bajen
Send push to mobile phone when sold tickets are updated

# Instructions
This is meant to be run as a cron job. There is an example in crontab.txt

Needed preparation:
* Create an account at Pushover
* Generate API key at Pushover. The API token and user key should be added to config.py
* Add desired URL slugs to config.py, last part of URL here: https://hammarbyfotboll.se/matcher
