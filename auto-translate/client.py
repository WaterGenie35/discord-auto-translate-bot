import discord
from translation import TranslationService
from custom_types import ServerLinks
from custom_types import Language

class AutoTranslateClient(discord.Client):

    def __init__(self):
        discord.Client.__init__(self)
        print("Initialising AutoTranslateClient...")
        self.service = TranslationService()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        for guild in self.guilds:
            print(f"  Guid: {guild.id}\t{guild.name}")
            for text_channel in guild.text_channels:
                print(f"    Channel: {text_channel.id}\t{text_channel.name}")
        print(self.service.translate(
                Language.ENGLISH, Language.RUSSIAN, "hello"))

