# ADICIONADO PELO BASIC_BOT.PY
import random

import discord
from discord.ext import commands

from config import TOKEN

# FIM DO ADICIONADO


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f"Estamos logados como {bot.user}")


# SEU COMANDO ORIGINAL
@bot.command()
async def hello(ctx):
    await ctx.send(f"Olá! eu sou um bot {bot.user}!")


# =========================================================
#                 ADICIONADO COMANDO NOVOS
# =========================================================


# COMANDO ADD
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


# COMANDO ROLL
@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await ctx.send("O formato deve ser NdN!")
        return

    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))

    await ctx.send(result)


# COMANDO CHOOSE
@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


# COMANDO REPEAT
@bot.command()
async def repeat(ctx, times: int, content="repeating..."):
    for i in range(times):
        await ctx.send(content)


# =========================================================
#               FIM
# =========================================================

# novo
# ==================================================
# NOVO COMANDO - usando uma opção da documentação
# ==================================================


@bot.command(aliases=["oi", "olá", "tem ai","e ai"])
async def saudacao(ctx):
    await ctx.send("Olá! Tudo bem?")


# ==================================================
# FIM DO NOVO COMANDO
# ==================================================

bot.run(TOKEN)
