import requests
from nonebot import on_command, get_bot
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import Event, GroupMessageEvent, PrivateMessageEvent
from nonebot.params import CommandArg
from nonebot.rule import to_me

linux = on_command("linux", rule=to_me(), aliases={"linux", "Linux"}, priority=10, block=True)


@linux.handle()
async def handle_function(event: Event, args: Message = CommandArg()):
    """
    Linux 命令大全
    """
    if msg := args.extract_plain_text():
        bot = get_bot()
        # 判断消息是否来自群聊
        if isinstance(event, GroupMessageEvent):
            group_id = event.group_id  # 获取群聊ID
            user_id = event.get_user_id()  # 获取用户ID
        elif isinstance(event, PrivateMessageEvent):
            group_id = None  # 私聊消息没有group_id
            user_id = event.get_user_id()  # 获取用户ID
        else:
            await linux.finish("无法识别的消息类型。")
            return

        response = requests.get("http://api.yujn.cn/api/linux.php", params={
            'type': 'json',
            'msg': msg
        })
        data = response.json()
        data = data['data']

        messages = [
            {
                "type": "at",
                "data": {
                    "qq": f"{user_id}"
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "\n"
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "功能:：" + data['order'] + "\n"
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "格式：" + data['format'] + "\n"
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "解释：" + data['message'] + "\n"
                }
            },
        ]

        if group_id:
            # 调用API发送群聊转发消息
            await bot.call_api("send_group_msg", group_id=group_id, message=messages)
        else:
            await bot.call_api("send_private_msg", user_id=user_id, message=messages)
    else:
        await linux.finish("请输入命令")
