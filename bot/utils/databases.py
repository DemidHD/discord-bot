import aiosqlite
import disnake


class UsersDataBase:
    """
    Database
    """
    def __init__(self):
        self.name = 'dbs/users.db'

    async def create_table(self):
        """Создание таблицы"""
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY, 
                money INTEGER, 
                premium INTEGER
            )'''
            await cursor.execute(query)
            await db.commit()

    async def get_user(self, user: disnake.Member):
        """Получить пользователя"""
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE id = ?'
            await cursor.execute(query, (user.id,))
            return await cursor.fetchone()

    async def add_user(self, user: disnake.Member):
        """Добавить пользователя"""
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user):
                cursor = await db.cursor()
                query = 'INSERT INTO users (id, money, premium) VALUES (?, ?, ?)'
                await cursor.execute(query, (user.id, 0, 0))
                await db.commit()

    async def update_money(self, user: disnake.Member, money: int, premium: int):
        """Обновить баланс"""
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET money = money + ?, premium = premium + ? WHERE id = ?'
            await cursor.execute(query, (money, premium, user.id))
            await db.commit()