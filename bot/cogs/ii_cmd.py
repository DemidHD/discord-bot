import aiohttp
import disnake
import requests
from disnake.ext import commands

from configs.main_config import API_KEY, RapidAPI_Key



class CMDUserIi(commands.Cog):
    """
    Команды для использования ИИ
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, inter: disnake.MessageInteraction, arg: str = None):
        messages = await inter.message.reply("❇|Подождите, ваш запрос обрабатывается!")
        try:
            if arg is None:
                return await messages.edit("📥| Введите параметры!")
            url = f"https://api.betterapi.net/youdotcom/chat?message={arg}&key={API_KEY}"  # set api url
            json = requests.get(url).json()  # load json form api
            await messages.edit(json["message"])  # print message response
        except Exception:
            return await messages.edit('Ошибка на стороне бота')

    @commands.command()
    async def gpt(self, inter: disnake.MessageInteraction, arg: str = None):
        """ChatGPT"""
        messages = await inter.message.reply("❇|Подождите, ваш запрос обрабатывается!")
        try:
            if arg is None:
                return await messages.edit("📥| Введите параметры!")
            url = "https://chatgpt-api7.p.rapidapi.com/ask"
            payload = {
                "query": f'{arg}',
                "wordLimit": "4096"
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": RapidAPI_Key,
                "X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, headers=headers) as response:
                    result = await response.json()
                    return await messages.edit(result['response'])
        except Exception as e:
            return await messages.edit(f'Произошла ошибка на стороне ChatGPT!\n\n>{e}')



def setup(bot):
    bot.add_cog(CMDUserIi(bot))