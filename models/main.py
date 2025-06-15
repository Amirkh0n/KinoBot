from tortoise import Tortoise 


async def on_startup(app):
    await Tortoise.init(
        db_url="sqlite://database/database.db",
        modules={"models": ["models.users", "models.movies"]},
    )
    await Tortoise.generate_schemas()


async def on_shutdown(app):
    await Tortoise.close_connections()