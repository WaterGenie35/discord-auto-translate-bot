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

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        print(f"Received message from {message.author} in {message.channel.name}.")
        guild = self.get_guild(765773043569393674)
        ru_channel = guild.get_channel(766287213888798730)
        en_channel = guild.get_channel(765806897558716446)
        translation = None
        target_channel = None
        if message.channel == ru_channel:
            translation = self.service.translate(
                    Language.RUSSIAN, Language.ENGLISH, message.content)
            target_channel = en_channel
        elif message.channel == en_channel:
            translation = self.service.translate(
                    Language.ENGLISH, Language.RUSSIAN, message.content)
            target_channel = ru_channel

        if target_channel:
            print(f"Sending translation to {target_channel.name}...")
            translation = f"**{message.author.display_name}:** " + translation
            await target_channel.send(translation)
            

