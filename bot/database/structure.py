import os
import dotenv

from tortoise import fields, Tortoise
from tortoise.models import Model

dotenv.load_dotenv()

class User(Model):
    user_id = fields.IntField(primary_key=True, auto_increment=True)
    telegram_id = fields.BigIntField()
    remaining_requests = fields.IntField(default=0) # Вместо 0 будет значение в/из конфиге
    total_requests = fields.IntField(default=0)
    requests = fields.IntField(default=0) # Вместо 0 будет значение в/из конфиге
    current_model = fields.TextField(default="gpt-xdVERSION") # Значение-заглушка

    class Meta:
        table = "users"

async def init_db():
    await Tortoise.init(
        db_url=os.getenv("DB_URL", "sqlite://db.sqlite3"),
        modules={'models': ['bot.database.structure']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()


