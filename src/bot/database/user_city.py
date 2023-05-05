from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'vk_bot'

    id = db.Column(db.Integer(), primary_key=True)
    city = db.Column(db.String(), default='-')


async def create_or_update(user_id: int, city: str) -> None:
    async with db.with_bind('postgresql://localhost/postgres'):
        await db.gino.create_all()

        if user := await User.query.where(User.id == user_id).gino.first():
            await user.update(city=city).apply()

        else:
            await User.create(id=user_id, city=city)


async def get_city(user_id: int):
    async with db.with_bind('postgresql://localhost/postgres'):
        await db.gino.create_all()

        user = await User.query.where(User.id == user_id).gino.first()

        return user
