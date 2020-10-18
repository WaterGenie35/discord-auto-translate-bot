#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from discord.ext import commands
from cogs import AutoTranslateCog


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='!')
    bot.add_cog(AutoTranslateCog(bot))
    bot.run(token)


if __name__ == '__main__':
    main()
