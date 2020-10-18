from discord.ext import commands
from translation import TranslationService
from custom_types import Language
import io
import aiohttp

class AutoTranslateCog(commands.Cog, name="Auto-translate"):

    def __init__(self, bot):
        self.bot = bot
        self.service = TranslationService()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} has connected to Discord.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        source_channel = message.channel
        guild = source_channel.guild

    @commands.command(name='translate', aliases=['t'])
    async def translate(self, context, source: str, target: str, *, message: str):
        """
        Translates the message from source language to target language
        Examples:
          !translate English Russian hi
          !t r e привет
        """
        if context.author == self.bot.user:
            return
        source_language = Language.from_string(source)
        target_language = Language.from_string(target)
        translation = self.service.translate(
                source_language,
                target_language,
                message)
        await context.channel.send(translation)

    @commands.group(name='link', invoke_without_command=True)
    @commands.has_permissions(manage_channels=True)
    async def link(self, context):
        "Connects channels for automatic translation"
        await context.send_help(context.command)

    @link.command(name='list', aliases=['ls'])
    @commands.has_permissions(manage_channels=True)
    async def list_links(self, context):
        "Shows all existing links"
        print("!link list")

    @link.command(name='create', aliases=['new', 'make', 'mk'])
    @commands.has_permissions(manage_channels=True)
    async def create_link(self, context):
        "Creates a new link between two channels"
        print("!link create")

    @link.command(name='delete', aliases=['del', 'rm'])
    @commands.has_permissions(manage_channels=True)
    async def delete_link(self, context):
        "Deletes an existing link"
        print("!link delete")

    @link.error
    @list_links.error
    @create_link.error
    @delete_link.error
    async def link_error(self, context, error):
        pass
