import requests
from nonebot import on_command, get_bot
from nonebot.adapters.onebot.v11 import MessageSegment, Event, GroupMessageEvent, PrivateMessageEvent
from nonebot.rule import to_me

km = on_command("km", rule=to_me(), aliases={"km"}, priority=10, block=True)


@km.handle()
async def handle_function(event: Event):
    """
    福利视频
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
        await km.finish("无法识别的消息类型。")
        return

    response = requests.get("https://api.yujn.cn/api/kuaimao.php", params={
        'type': 'json'
    })
    data = response.json()

    messages = []
    title = {
        "type": "node",
        "data": {
            "name": "K-Bot",
            "uin": "3931952215",
            "content": [MessageSegment.text(data['title'])]
        }
    }
    messages.append(title)
    cover = {
        "type": "node",
        "data": {
            "name": "K-Bot",
            "uin": "3931952215",
            "content": [MessageSegment.image(data['image'])]
        }
    }
    messages.append(cover)
    video = {
        "type": "node",
        "data": {
            "name": "K-Bot",
            "uin": "3931952215",
            "content": [MessageSegment.text(data['video'])]
        }
    }
    messages.append(video)

    if group_id:
        # 调用API发送群聊转发消息
        await bot.send_group_forward_msg(group_id=group_id, messages=messages)
    else:
        await bot.send_private_forward_msg(user_id=user_id, messages=messages)
