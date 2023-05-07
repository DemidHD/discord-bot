import logging
import os

import disnake
from disnake.ext import commands

from configs.main_config import token


bot = commands.Bot(
    command_prefix='/',
    intents=disnake.Intents.all()
)

# включаем логирование
logging.basicConfig(level=logging.INFO)


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    """."""
    bot.load_extension(f'cogs.{extension}')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    """."""
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    """."""
    bot.reload_extension(f'cogs.{extension}')


for filename in os.listdir('cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    bot.run(token)