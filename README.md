# Discord Auto-Translate Bot

## Overview

1. Link source (channel, language) pair to target (channel, language) pair
2. Bot automatically translates messages from source channel to target channel in source language to target language.

For simplicity, this bot does not perform language detection and simply assume all messages in source channel to be in the source language.
The translation is handled by the google cloud translation api.

## Setup

```bash
$ cd /path/to/discord-auto-translate-bot
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

* Add bot token and google cloud details as in `.env.example`.
* Add google cloud service account credential file as in `google-service-account-credentials.json.example`.

## Run

```bash
$ source venv/bin/activate
$ python3 auto-translate/bot.py
```

## Discord Commands

* TO-DO

## Resources and Links

* [Google Cloud Documentations](https://cloud.google.com/docs)
* [Google Cloud Translation API Documentations](https://cloud.google.com/translate/docs)
* [Google Cloud Console](https://console.cloud.google.com/)
* [`discord.py` Documentations](https://discordpy.readthedocs.io/en/latest/index.html)
* [WriteBots' The Ultimate Guide to Making a Discord Bot](https://www.writebots.com/how-to-make-a-discord-bot/)

## Notes on [nvu's Discord Translator Bot](https://nvu.io/en/bots/discord-translator/)

Since the core functionality described in the overview section is a strict subset of nvu's bot, interested users are encouraged to check out nvu's bot instead, they also use google's api.
This project is only a "hello world" into discord bots so wheel reinvention wasn't a factor.
Also nvu's bot doesn't have a free tier unlike the base google api (500,000 characters per month), so I can still use this in small hobby servers.
