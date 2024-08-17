import requests
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.rule import to_me

ping = on_command("ping", rule=to_me(), aliases={"ping"}, priority=10, block=True)


@ping.handle()
async def handle_function(args: Message = CommandArg()):
    """
    答案之书
    """
    if url := args.extract_plain_text():
        response = requests.get("http://api.yujn.cn/api/ping.php", params={
            'url': url
        })
        await ping.finish(response.text)
    else:
        await ping.finish("请输入url")
