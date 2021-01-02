import discord
from discord.ext import commands
import cowsay
import os
from dotenv import load_dotenv

DESCR = '''A simple Cowsay bot written in Python by github.com/sambhavsaggi'''
load_dotenv()
token = os.getenv('TOKEN')
prefix = os.getenv('PREFIX')
helptext = 'Prefix: `' + prefix + '`\nCharacters: beavis, cheese, daemon, cow, dragon, ghostbusters, kitty, meow, milk, pig, stegosaurus, stimpy, turkey, turtle, tux\nExample: `?cow hi`'

intents = discord.Intents.default()
intents.presences = False
intents.typing = False

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix),
    description=DESCR,
    intents=intents
)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def beavis(ctx, *text):
    await ctx.send('```' + cowsay.beavis(text) + '```')

@bot.command()
async def cheese(ctx, *, text):
    await ctx.send('```' + cowsay.cheese(text) + '```')

@bot.command()
async def daemon(ctx, *, text):
    await ctx.send('```' + cowsay.daemon(text) + '```')

@bot.command()
async def cow(ctx, *, text):
    await ctx.send('```' + cowsay.cow(text) + '```')

@bot.command()
async def dragon(ctx, *, text):
    await ctx.send('```' + cowsay.dragon(text) + '```')

@bot.command()
async def ghostbusters(ctx, *, text):
    await ctx.send('```' + cowsay.ghostbusters(text) + '```')

@bot.command()
async def kitty(ctx, *, text):
    await ctx.send('```' + cowsay.kitty(text) + '```')

@bot.command()
async def meow(ctx, *, text):
    await ctx.send('```' + cowsay.meow(text) + '```')

@bot.command()
async def milk(ctx, *, text):
    await ctx.send('```' + cowsay.milk(text) + '```')

@bot.command()
async def pig(ctx, *, text):
    await ctx.send('```' + cowsay.pig(text) + '```')

@bot.command()
async def stegosaurus(ctx, *, text):
    await ctx.send('```' + cowsay.stegosaurus(text) + '```')

@bot.command()
async def stimpy(ctx, *, text):
    await ctx.send('```' + cowsay.stimpy(text) + '```')

@bot.command()
async def turkey(ctx, *, text):
    await ctx.send('```' + cowsay.turkey(text) + '```')

@bot.command()
async def turtle(ctx, *, text):
    await ctx.send('```' + cowsay.turtle(text) + '```')

@bot.command()
async def tux(ctx, *, text):
    await ctx.send('```' + cowsay.tux(text) + '```')

bot.run(token)
