import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore


class NewsCmd(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} Loaded news.py!")

    
    # Command to display info about me
    @app_commands.command(name="news", description="View the news from school events")
    @commands.has_permissions(administrator=True)
    async def news_cmd(self, interaction: discord.Interaction, header: str, event_name: str, description: str, thumbnail_url: str):
        embed = discord.Embed(title=f"{header}", color=0x5865F2)
        embed.set_thumbnail(url=f"{thumbnail_url}")
        embed.add_field(name=f"{event_name}", value=f"{description}", inline=False)
        embed.set_footer(text="Developed by: WaterMeloDev", icon_url="https://cdn.discordapp.com/attachments/1149599961164562473/1152740621799407647/melo.jpg")
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(NewsCmd(client))