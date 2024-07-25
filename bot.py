import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter  # 避免重复命名
from nonebot.adapters.onebot.v11 import Adapter as BotAdapter

# 初始化 NoneBot
nonebot.init()
# BotAdapter.config
# 注册适配器
driver = nonebot.get_driver()
# driver.register_adapter(ConsoleAdapter)
driver.register_adapter(BotAdapter)

# 在这里加载插件
nonebot.load_builtin_plugins("echo")  # 内置插件
# nonebot.load_plugin("thirdparty_plugin")  # 第三方插件
nonebot.load_plugins("plugins")  # 本地插件

if __name__ == "__main__":
    nonebot.run()