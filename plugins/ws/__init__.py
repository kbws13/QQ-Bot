from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.rule import to_me, startswith

rule = to_me() & startswith(("!"), ignorecase=False)

websocket = on_message(rule=rule)


@websocket.handle()
async def handle_message(bot: Bot, event: Event):
    print(f"Received message: {event.get_message()}")