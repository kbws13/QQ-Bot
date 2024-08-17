import requests
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.rule import to_me

daan = on_command("答案之书", rule=to_me(), aliases={"答案", "daan"}, priority=10, block=True)


@daan.handle()
async def handle_function(args: Message = CommandArg()):
    """
    答案之书
    """
    response = requests.get("http://api.yujn.cn/api/daan.php")
    await daan.finish(response.text)
