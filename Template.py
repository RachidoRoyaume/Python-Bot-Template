import discord
from discord.ext import commands

# Configuration des intents
intents = discord.Intents.default()
intents.typing = False  # Désactive l'intent "typing" (taper) si vous n'en avez pas besoin
intents.presences = False  # Désactive l'intent "presences" (présences) si vous n'en avez pas besoin

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send("Salut, je suis un bot Discord !")

bot.run('VOTRE_TOKEN')
