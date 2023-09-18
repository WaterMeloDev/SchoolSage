import discord
import json
from discord.ext import commands
from colorama import Fore


class JoinEvent(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} Loaded join.py!")

    # Join Event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('src/data/blacklisted.json', 'r') as f:
            blacklisted = json.load(f)
        if str(member.id) in blacklisted:
            await member.kick(reason="shadowbanned")
        else:
            channel = await self.client.fetch_channel(1149594511761227858)
            embed = discord.Embed(title=f"Welcome to the group chat!", color=0x5865F2)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1149599961164562473/1152745491537346682/welcome.gif")
            embed.add_field(name=f"Hello {member}", value=f"Our school group chat is for updates, study tips, and fun discussions with fellow students. Feel free to ask questions.", inline=False)
            embed.set_footer(text="Developed by: WaterMeloDev", icon_url="https://cdn.discordapp.com/attachments/1149599961164562473/1152740621799407647/melo.jpg")
            await channel.send(embed=embed)
    
    # Leave Event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = await self.client.fetch_channel(1149594511761227858)
        await channel.send(f"{member} has left the group chat.")

async def setup(client):
    await client.add_cog(JoinEvent(client))