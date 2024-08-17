from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.rule import to_me

zfb = on_command("支付宝", rule=to_me(), aliases={"zfb"}, priority=10, block=True)


@zfb.handle()
async def handle_function(args: Message = CommandArg()):
    """
    支付宝到账语音
    """
    if money := args.extract_plain_text():
        await zfb.finish(MessageSegment.record(f"http://api.yujn.cn/api/zfb.php?msg={money}"))
    else:
        await zfb.finish("请输入金额")
