from aiogram.types import Message

from tgbot.services.repository import Repo
from tgbot.wrappers import Gatherer

gather = Gatherer()

@gather.message_handler(commands=["start"], state="*")
async def user_start(m: Message, repo: Repo):
    await repo.add_user(m.from_user.id)
    await m.reply("Hello, user!")
