import discord
from discord import utils
from translation import TranslationService
from custom_types import ServerLinks
from custom_types import Language
import io
import aiohttp


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
                category = ""
                category_id = text_channel.category_id
                if category_id:
                    category_channel = utils.find(
                            lambda category: category.id == category_id,
                            guild.categories)
                    category = f" @ {category_channel.name}"
                print(f"    Channel: {text_channel.id}\t{text_channel.name}{category}")
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
                    Language.RUSSIAN,
                    Language.ENGLISH,
                    message.clean_content)
            target_channel = en_channel
        elif message.channel == en_channel:
            translation = self.service.translate(
                    Language.ENGLISH,
                    Language.RUSSIAN,
                    message.clean_content)
            target_channel = ru_channel

        if target_channel:
            print(f"Sending translation to {target_channel.name}...")
            result = self.postprocess_message(message, translation)
            attachments = await self.get_files_from(message)
            await target_channel.send(
                    result,
                    files=attachments)

    def postprocess_message(self, message, translation):
        translation = f"**{message.author.display_name}:** " + translation
        return translation

    async def get_files_from(self, message):
        if len(message.attachments) == 0:
            return []
        files = []
        async with aiohttp.ClientSession() as session:
            for attachment in message.attachments:
                async with session.get(attachment.url) as response:
                    if response.status != 200:
                        continue
                    data = io.BytesIO(await response.read())
                    f = discord.File(
                            data,
                            filename=attachment.filename,
                            spoiler=attachment.is_spoiler())
                    files.append(f)
        return files
