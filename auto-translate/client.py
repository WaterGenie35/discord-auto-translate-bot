import discord

class AutoTranslateClient(discord.Client):

    def __init__(self):
        discord.Client.__init__(self)
        print("Initialising AutoTranslateClient...")

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        for guild in self.guilds:
            print(f"  Guid: {guild.id}\t{guild.name}")
            for text_channel in guild.text_channels:
                print(f"    Channel: {text_channel.id}\t{text_channel.name}")

