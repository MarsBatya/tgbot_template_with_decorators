from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.models.role import UserRole
from tgbot.services.repository import Repo
from tgbot.wrappers import Gatherer

gather = Gatherer()

# # you can pass multiple roles:
# @gather.message_handler(commands=["start"], state="*", role=[UserRole.ADMIN])
# # or use another filter:
# @gather.message_handler(commands=["start"], state="*", is_admin=True)
@gather.message_handler(commands=["start"], state="*", role=UserRole.ADMIN)
async def admin_start(m: Message):
    await m.reply("Hello, admin!")