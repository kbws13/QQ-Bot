from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import to_me

cos = on_command("cos", rule=to_me(), aliases={"cosplay"}, priority=10, block=True)


@cos.handle()
async def handle_function():
    """
    cos图片
    """
    await cos.finish(MessageSegment.image("http://api.yujn.cn/api/cos.php"))
