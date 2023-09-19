import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded help.py")

    
    # help command
    @app_commands.command(name="teacherhelp", description="👩‍🏫 Show a list of teacher commands")
    async def teacherhelp_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="👩‍🏫 Teacher Discord Bot Commands",
            description="Here are some useful commands for teachers:",
            color=0x27ae60,
        )

        # Add commands with descriptions and emojis
        embed.add_field(name="📋 /schedule", value="View class schedules.", inline=False)
        embed.add_field(name="📢 /announce", value="Send important announcements to students.", inline=False)
        embed.add_field(name="📅 /homework", value="Manage and distribute homework assignments.", inline=False)
        embed.add_field(name="📚 /info", value="Access educational resources and information.", inline=False)
        embed.add_field(name="📖 /grades", value="Manage and view student grades.", inline=False)
        embed.add_field(name="👥 /enroll", value="Enroll students in courses.", inline=False)
        embed.add_field(name="📊 /report", value="Generate reports and analytics.", inline=False)
        embed.add_field(name="👩‍🎓 /students", value="View and manage student profiles.", inline=False)
        embed.add_field(name="👨‍🏫 /teachers", value="Access teacher-specific features.", inline=False)
        embed.add_field(name="📜 /help", value="Show this list of commands.", inline=False)

        # Send the embed as a response
        await interaction.response.send_message(embed=embed)

    
    @app_commands.command(name="studenthelp", description="🎓 Show a list of student commands")
    async def studenthelp_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🎓 Student Discord Bot Commands",
            description="Here are some commands tailored for students:",
            color=0xff5733, 
        )

        # Add commands with descriptions and emojis
        embed.add_field(name="📋 /schedule", value="View your class schedule.", inline=False)
        embed.add_field(name="📢 /announcements", value="Check for important announcements.", inline=False)
        embed.add_field(name="📅 /homework", value="Manage and keep track of homework assignments.", inline=False)
        embed.add_field(name="📚 /resources", value="Access helpful educational resources.", inline=False)
        embed.add_field(name="📊 /grades", value="Check your grades and performance.", inline=False)
        embed.add_field(name="🎉 /events", value="Find and join school events and clubs.", inline=False)
        embed.add_field(name="📜 /help", value="Show this list of commands.", inline=False)

        # Send the embed as a response
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))