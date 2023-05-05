from disnake.ext import commands


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
    async def hello(self, ctx):
        """Команда /hello"""
        await ctx.reply('привет!')


def setup(bot):
    bot.add_cog(CMDUsers(bot))