from bot.database.structure import User

async def register_user(telegram_id: int): # Надо проверить данную функцию, из-за того, что пока что ей нет применений в коде, написать под конец тесты
        user = await User.filter(telegram_id=telegram_id).first()
        if not user:
            user = await User.create(telegram_id=telegram_id)
        else:
              return user
        
async def get_user(telegram_id: int):
    user = await User.filter(telegram_id=telegram_id).first()
    if not user:
        await register_user(telegram_id)
        user = await User.filter(telegram_id=telegram_id).first()
    return user
    
