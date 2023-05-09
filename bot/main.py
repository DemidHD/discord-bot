import logging
import os

import disnake
import gatey_sdk
from disnake.ext import commands

from configs.main_config import token


bot = commands.Bot(
    command_prefix='/',
    intents=disnake.Intents.all()
)

client = gatey_sdk.Client(
    transport=gatey_sdk.PrintTransport,
    exceptions_capture_code_context=False
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


@bot.event
async def on_command_error(ctx, error) -> None:
    """Отлавливает все ошибки от бота, пока тестовый вариант"""
    client.capture_exception(error, level='error')


if __name__ == '__main__':
    bot.run(token)