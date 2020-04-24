# !usr/bin/env python3
# (c) Anandpskerala

from tamtam import Bot, Dispatcher, run_poller
from tamtam.types import Message
from tamtam.dispatcher.filters import MessageFilters

from config import TOKEN

bot = Bot(TOKEN)
disp = Dispatcher(bot)

@disp.message_handler(MessageFilters.commands("start"))
async def start(message: Message):
    await message.respond(f"Hello {message.sender.name}.")


@disp.message_handler()
async def any_msg(message: Message):
    await message.reply(message.json(indent=4))


run_poller()
