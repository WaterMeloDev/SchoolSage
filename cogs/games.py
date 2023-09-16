import discord
import random
from discord.ext import commands
from colorama import Fore

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded games.py")

    
    # 8BALL command
    @commands.command(name="8ball", description="ask the magic 8ball a question")
    async def eightball_cmd(self, ctx, *, question: str = None):
        if question == None:
            await ctx.send("Ask a question: Ex: `>8ball Am I cool?`")
        else:
            responses = ["It is certain.",
                        "It is decidedly so.",
                        "Without a doubt.",
                        "Yes - definitely.",
                        "You may rely on it.",
                        "As I see it, yes.",
                        "Most likely.",
                        "Outlook good.",
                        "Yes.",
                        "Signs point to yes.",
                        "Reply hazy, try again.",
                        "Ask again later.",
                        "Better not tell you now.",
                        "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Don't count on it.",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Very doubtful."]
            embed = discord.Embed(title="8ball UwU", description="Ask me questions.", color=0x000000)
            embed.add_field(name="Question:", value=f"{question}", inline=False)
            embed.add_field(name="Answer:", value=f"{random.choice(responses)}", inline=False)
            embed.set_footer(text="You are sus~")
            await ctx.send(embed=embed)

        # COINFLIP command
    @commands.command(name="coinflip", description="flip a coin")
    async def coinflip_cmd(self, ctx):
        responses = ["Heads",
                     "Tails"]
        await ctx.send(f"{random.choice(responses)}")

        # DICE command
    @commands.command(name="dice", description="roll a dice")
    async def dice_cmd(self, ctx):
        responses = ["1",
                     "2",
                     "3",
                     "4",
                     "5",
                     "6"]
        await ctx.send(f"{random.choice(responses)}")

        # PING command
    @commands.command(name="ping", description="get the bot's ping")
    async def ping_cmd(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    await bot.add_cog(Games(bot))