#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from client import AutoTranslateClient

def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = AutoTranslateClient()
    client.run(token)


if __name__ == '__main__':
    main()
