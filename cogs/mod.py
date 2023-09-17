import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore
import json

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded mod.py")

    # kick command
    @app_commands.command(name="kick", description="kick a member")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick_cmd(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"Kicked {member} for {reason}")

    # ban command
    @app_commands.command(name="ban", description="ban a member")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban_cmd(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"Banned {member} for {reason}")

    # unban command
    @app_commands.command(name="unban", description="unban a member")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban_cmd(self, interaction: discord.Interaction, member: discord.User):
        banned_users = await interaction.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await interaction.guild.unban(user)
                await interaction.response.send_message(f"Unbanned {user.mention}")
                return
    
    # clear
    @app_commands.command(name="clear", description="clear messages")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear_cmd(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Cleared {amount} messages", delete_after=5)
            
    # shadowban command
    @app_commands.command(name="shadowban", description="shadowban a member")
    @app_commands.checks.has_permissions(ban_members=True)
    async def shadowban_cmd(self, interaction: discord.Interaction, member: discord.Member):
        # Check if the member is already shadowbanned
        with open('src/data/blacklisted.json', 'r') as f:
            try:
                blacklisted = json.load(f)
            except json.JSONDecodeError:
                blacklisted = []

        if str(member.id) in blacklisted:
            await interaction.response.send_message(f"{member} is already shadowbanned.")
        else:
            # Add user to blacklisted.json
            try:
                blacklisted.append(str(member.id))
                with open('src/data/blacklisted.json', 'w') as f:
                    json.dump(blacklisted, f)
            except Exception as e:
                print(f"Error shadowbanning {member}: {e}")
            # Ban user
            await interaction.response.send_message(f"Shadowbanned {member}")
            await member.kick(reason="shadowbanned")


    
    @app_commands.command(name="unshadowban", description="unshadowban a member")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unshadowban_cmd(self, interaction: discord.Interaction, member: discord.User):
        try:
            with open('src/data/blacklisted.json', 'r') as f:
                blacklisted = json.load(f)
        except FileNotFoundError:
            blacklisted = []  # Create an empty list if the file doesn't exist

        if str(member.id) in blacklisted:
            blacklisted.remove(str(member.id))
            with open('src/data/blacklisted.json', 'w') as f:
                json.dump(blacklisted, f)
            await interaction.response.send_message(f"Unshadowbanned {member}")
        else:
            await interaction.response.send_message(f"{member} is not shadowbanned.")
  

async def setup(bot):
    await bot.add_cog(Mod(bot))