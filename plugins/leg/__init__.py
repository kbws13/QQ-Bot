import requests
from nonebot import on_command, get_bot
from nonebot.adapters.onebot.v11 import MessageSegment, Event, GroupMessageEvent, PrivateMessageEvent
from nonebot.rule import to_me

leg = on_command("腿", rule=to_me(), aliases={"leg", "腿"}, priority=10, block=True)


@leg.handle()
async def handle_function(event: Event):
    bot = get_bot()
    # 判断消息是否来自群聊
    if isinstance(event, GroupMessageEvent):
        group_id = event.group_id  # 获取群聊ID
        user_id = event.get_user_id()  # 获取用户ID
    elif isinstance(event, PrivateMessageEvent):
        group_id = None  # 私聊消息没有group_id
        user_id = event.get_user_id()  # 获取用户ID
    else:
        await leg.finish("无法识别的消息类型。")
        return

    response = requests.get("https://api.yujn.cn/api/qlyx.php", params={
        'type': 'json',
        'count': 10
    })
    data = response.json()
    images = data['img']

    messages = []
    for img_url in images:
        message = {
            "type": "node",
            "data": {
                "name": "K-Bot",
                "uin": "3931952215",
                "content": [MessageSegment.image(img_url)]
            }
        }
        messages.append(message)

    if group_id:
        # 调用API发送群聊转发消息
        await bot.send_group_forward_msg(group_id=group_id, messages=messages)
    else:
        await bot.send_private_forward_msg(user_id=user_id, messages=messages)
