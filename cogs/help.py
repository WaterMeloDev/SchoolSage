import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded help.py")

    
    # help command
    @app_commands.command(name="help", description="Shows a list of commands")
    async def help_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Help", color=0x000000)
        embed.add_field(name="/help", value="Shows a list of commands", inline=True)
        embed.add_field(name="/8ball", value="Ask the magic 8ball a question.", inline=True)
        embed.add_field(name="/coinflip", value="Flip a coin.", inline=True)
        embed.add_field(name="/dice", value="Roll a dice.", inline=True)
        embed.add_field(name="/ping", value="Get the bot's ping.", inline=True)
        embed.add_field(name="/kick", value="Kick a member.", inline=True)
        embed.add_field(name="/ban", value="Ban a member.", inline=True)
        embed.add_field(name="/unban", value="Unban a member.", inline=True)
        embed.add_field(name="/shadowban", value="Shadowban a member.", inline=True)
        embed.add_field(name="/warn", value="Warn a member.", inline=True)
        embed.add_field(name="/warnings", value="Get a member's warnings.", inline=True)
        embed.add_field(name="/clearwarns", value="Clear a member's warnings.", inline=True)
        embed.add_field(name="/clear", value="Clear messages.", inline=True)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))