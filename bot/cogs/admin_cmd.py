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

    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, ctx, member: disnake.Member, *, reason='Нарушение правил'):
        """Бан пользователя"""
        await ctx.send(f'Администратор {ctx.author.mention} забанил пользователя {member.mention}', delete_after=2)
        await member.ban(reason=reason)
        await ctx.message.detele()

    @commands.slash_command()
    async def clear_chat(self, interaction, amount: int):
        """Чистка чата"""
        try:
            await interaction.response.send_message(f'Deleted {amount} messages.')
            await interaction.channel.purge(limit=amount + 1)
        except Exception as e:
            print(e)



def setup(bot):
    bot.add_cog(CMDAdmin(bot))
