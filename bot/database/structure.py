from tortoise import fields, Tortoise
from tortoise.models import Model

class User(Model):
    user_id = fields.IntField(primary_key=True, auto_increment=True)
    telegram_id = fields.BigIntField()
    remaining_requests = fields.IntField(default=0) # Вместо 0 будет значение в/из конфиге
    total_requests = fields.IntField(default=0)
    requests = fields.IntField(default=0) # Вместо 0 будет значение в/из конфиге
    current_model = fields.TextField(default="gpt-xdVERSION") # Значение-заглушка

async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3', # TODO: Добавить миграции на aerich, в будущем переделать в postgresql заместо sqlite
        modules={'models': ['bot.database.structure']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()


    