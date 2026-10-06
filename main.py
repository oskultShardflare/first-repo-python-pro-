```python
import discord
from discord.ext import commands
import requests
import random

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your useful Discord bot!")


@bot.command()
async def dog(ctx):
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    await ctx.send(data['url'])


@bot.command()
async def roll(ctx):
    number = random.randint(1, 100)
    await ctx.send(f"You rolled {number}!")


@bot.command()
async def helpme(ctx):
    await ctx.send("Commands: !hello, !dog, !roll")


bot.run("")
```
