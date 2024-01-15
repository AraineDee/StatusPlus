import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.event
async def on_message(message):
    if type(message.channel) == discord.channel.DMChannel and message.author != bot.user:
        await bot.process_commands(message)



@bot.command()
async def register(ctx):
    await ctx.send("registering you")





if __name__ == "__main__":
    if TOKEN != "token":
        bot.run(TOKEN)
    else:
        raise Exception("No token passed for bot in .env file")