import discord
from discord.ext import commands
from colorama import Fore
import json

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded mod.py")

    # kick command
    @commands.command(name="kick", description="kick a member")
    @commands.has_permissions(kick_members=True)
    async def kick_cmd(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member} for {reason}")

    # ban command
    @commands.command(name="ban", description="ban a member")
    @commands.has_permissions(ban_members=True)
    async def ban_cmd(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member} for {reason}")

    # unban command
    @commands.command(name="unban", description="unban a member")
    @commands.has_permissions(ban_members=True)
    async def unban_cmd(self, ctx, *, member):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return
    
    # clear
    @commands.command(name="clear", description="clear messages")
    @commands.has_permissions(manage_messages=True)
    async def clear_cmd(self, ctx, amount=5):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount} messages", delete_after=5)
            
    # shadowban command
    @commands.command(name="shadowban", description="shadowban a member")
    @commands.has_permissions(ban_members=True)
    async def shadowban_cmd(self, ctx, member: discord.Member):
        # delete the message
        await ctx.message.delete()
        # Check if the member is already shadowbanned
        with open('src/data/blacklisted.json', 'r') as f:
            try:
                blacklisted = json.load(f)
            except json.JSONDecodeError:
                blacklisted = []

        if str(member.id) in blacklisted:
            await ctx.send(f"{member} is already shadowbanned.")
        else:
            # Add user to blacklisted.json
            try:
                blacklisted.append(str(member.id))
                with open('src/data/blacklisted.json', 'w') as f:
                    json.dump(blacklisted, f)
            except Exception as e:
                print(f"Error shadowbanning {member}: {e}")
            # Ban user
            await ctx.send(f"Shadowbanned {member}")
            await member.kick(reason="shadowbanned")


    
    @commands.command(name="unshadowban", description="unshadowban a member")
    @commands.has_permissions(ban_members=True)
    async def unshadowban_cmd(self, ctx, member: discord.User):
        await ctx.message.delete()
        try:
            with open('src/data/blacklisted.json', 'r') as f:
                blacklisted = json.load(f)
        except FileNotFoundError:
            blacklisted = []  # Create an empty list if the file doesn't exist

        if str(member.id) in blacklisted:
            blacklisted.remove(str(member.id))
            with open('src/data/blacklisted.json', 'w') as f:
                json.dump(blacklisted, f)
            await ctx.send(f"Unshadowbanned {member}")
        else:
            await ctx.send(f"{member} is not shadowbanned.")
  

async def setup(bot):
    await bot.add_cog(Mod(bot))