from discord.ext import commands
from translation import TranslationService
from custom_types import Language
import io
import aiohttp

class AutoTranslateCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.service = TranslationService()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.command(
            name='translate',
            aliases=['t'],
            description="""
                    Example:
                    !translate English Russian hi
                    !t r e привет""")
    async def translate_command(
            self, context, source: str, target: str, message: str):
        if context.author == self.bot.user:
            return
        source_language = Language.from_string(source)
        target_language = Language.from_string(target)
        translation = self.service.translate(
                source_language,
                target_language,
                message)
        await context.channel.send(translation)
