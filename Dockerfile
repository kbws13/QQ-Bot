FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install nonebot2[fastapi] \
    && pip install nonebot-adapter-console \
    && pip install nonebot-adapter-onebot \
    && pip install nonebot-plugin-cloudsignx

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露端口
EXPOSE 8080