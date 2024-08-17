FROM python:3.10-slim

WORKDIR /app

COPY . /app

#RUN pip install nonebot2[fastapi] \
#    && pip install nonebot-adapter-console \
#    && pip install nonebot-adapter-onebot

# 安装应用程序所需的Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 启动应用程序
CMD ["python", "bot.py"]