import requests
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.rule import to_me

weather = on_command("天气", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True)


@weather.handle()
async def handle_function(args: Message = CommandArg()):
    """
    墨迹天气
    """
    if location := args.extract_plain_text():
        response = requests.get("http://api.yujn.cn/api/tianqi.php", params={
            'msg': location,
            'b': '1'
        })
        await weather.finish(response.text)
    else:
        await weather.finish("请输入地名")
