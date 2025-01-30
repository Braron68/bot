import discord
from bot_logic import gen_pass
from bot_logic import gen_emodji
from discord.ext import commands 
#sm
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hola")

@bot.command()
async def bye(ctx):
    await ctx.send(("✌️"))

@bot.command()
async def password(ctx, longitud: int):
    await ctx.send(gen_pass(longitud))

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')



