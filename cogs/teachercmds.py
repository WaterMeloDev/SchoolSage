import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore

class Teacher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded teachercmds.py")

async def setup(bot):
    await bot.add_cog(Teacher(bot))