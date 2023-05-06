import disnake
from disnake.ext import commands


class CMDAdmin(commands.Cog):
    """
    Команды для администрации бота
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member: disnake.Member, *, reason='Нарушение правил'):
        """Исключить пользователя"""
        await ctx.reply(f'Администратор {ctx.author.mention} исключил пользователя {member.mention}')
        await member.kick(reason=reason)
        await ctx.message.delete()




def setup(bot):
    bot.add_cog(CMDAdmin(bot))
