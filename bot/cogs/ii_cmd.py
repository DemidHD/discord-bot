import aiohttp
import disnake
import requests
from disnake.ext import commands

from configs.main_config import API_KEY
from services.services import get_conf_for_gpt


class CMDUserIi(commands.Cog):
    """
    Команды для использования ИИ
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, inter: disnake.MessageInteraction, arg: str = None) -> None:
        messages = await inter.message.reply("❇|Подождите, ваш запрос обрабатывается!")
        if arg is None:
            return await messages.edit("📥| Введите параметры!")
        url = f"https://api.betterapi.net/youdotcom/chat?message={arg}&key={API_KEY}"  # set api url
        json = requests.get(url).json()  # load json form api
        await messages.edit(json["message"])  # print message response


    @commands.command()
    async def gpt(self, inter: disnake.MessageInteraction, arg: str = None) -> None:
        """ChatGPT"""
        messages = await inter.message.reply("❇|Подождите, ваш запрос обрабатывается!")
        try:
            if arg is None:
                return await messages.edit("📥| Введите параметры!")
            result = await get_conf_for_gpt(arg)
            return await messages.edit(result['response'])
        except Exception as e:
            return await messages.edit(f'Произошла ошибка на стороне ChatGPT!\n\n>{e}')


def setup(bot):
    bot.add_cog(CMDUserIi(bot))