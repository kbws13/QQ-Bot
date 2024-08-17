import requests
from nonebot import on_command, get_bot
from nonebot.adapters.onebot.v11 import Event, GroupMessageEvent, PrivateMessageEvent
from nonebot.rule import to_me

lsjt = on_command("历史", rule=to_me(), aliases={"历史上的今天", "历史", "ls"}, priority=10, block=True)


@lsjt.handle()
async def handle_function(event: Event):
    """
    历史上的今天
    """
    bot = get_bot()
    # 判断消息是否来自群聊
    if isinstance(event, GroupMessageEvent):
        group_id = event.group_id  # 获取群聊ID
        user_id = event.get_user_id()  # 获取用户ID
    elif isinstance(event, PrivateMessageEvent):
        group_id = None  # 私聊消息没有group_id
        user_id = event.get_user_id()  # 获取用户ID
    else:
        await lsjt.finish("无法识别的消息类型。")
        return

    response = requests.get("http://api.yujn.cn/api/lsjt.php")
    data = response.json()

    messages = [{
        "type": "at",
        "data": {
            "qq": f"{user_id}"
        }
    }, {
        "type": "text",
        "data": {
            "text": "\n"
        }
    }]
    for item in data['msg']['list']:
        messages.append(
            {
                "type": "text",
                "data": {
                    "text": item + "\n"
                }
            }
        )

    if group_id:
        # 调用API发送群聊转发消息
        await bot.call_api("send_group_msg", group_id=group_id, message=messages)
    else:
        await bot.call_api("send_private_msg", user_id=user_id, message=messages)
