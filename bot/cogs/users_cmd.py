import aiohttp
import disnake

from disnake.ext import commands

from bot.configs.main_config import RapidAPI_Key
from bot.utils.generate_line import lines


class CMDUsers(commands.Cog):
    """
    Команды для юзера
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Сообщает о запуске бота"""
        print(f'Bot {self.bot.user} is ready to work!')

    @commands.command()
    async def bot(self, ctx):
        """Состояние бота"""
        return await ctx.reply('бот на месте!')

    @commands.command()
    async def joined(self, ctx, member: disnake.Member = None):
        """Говорит, когда участник присоединился"""
        if member is None:
            return await ctx.reply(f'Укажите пользователя')
        if member.joined_at:
            # formats the join time/date like "5 years ago"
            date_str = disnake.utils.format_dt(member.joined_at, "R")
            return await ctx.send(f"{member} присоединился {date_str}")


    @commands.command()
    async def commands(self, ctx):
        embed = disnake.Embed(
            title="Навигация по командам",
            description="Здесь ты сможешь найти доступные команды и их описание"
        )
        commands_list = ["/gpt"]
        descriptions_for_commands = ["ChatGPT"]
        for command_name, description_command in zip(commands_list, descriptions_for_commands):
            embed.add_field(
                name=command_name,
                value=description_command,
                inline=False  # Будет выводиться в столбик, если True - в строчку
            )
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CMDUsers(bot))