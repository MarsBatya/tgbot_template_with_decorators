
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.services.repository import Repo
from tgbot.states.user import UserMain
from tgbot.wrappers import Gatherer

gather = Gatherer()

@gather.message_handler(commands=["start"], state="*")
async def user_start(m: Message, repo: Repo, state: FSMContext):
    await repo.add_user(m.from_user.id)
    await m.reply("Hello, user!")
    await state.set_state(UserMain.SOME_STATE)