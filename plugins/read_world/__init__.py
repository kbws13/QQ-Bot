from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import to_me

read_world = on_command("世界新闻", rule=to_me(), aliases={"世界", "新闻"}, priority=10, block=True)


@read_world.handle()
async def handle_function():
    """
    60秒世界新闻
    """
    await read_world.finish(MessageSegment.image("http://api.yujn.cn/api/60SReadWorld.php"))
