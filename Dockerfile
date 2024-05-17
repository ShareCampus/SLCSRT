# 使用官方Python运行时作为父镜像
FROM python:3.8

# 设置容器内的工作目录
WORKDIR /app

# 将当前目录内容复制到容器内的/app
COPY . /app

# 安装requirements.txt中指定的任何所需包
RUN pip install --no-cache-dir -r requirements.txt

# 让端口80可供此容器外的环境使用
EXPOSE 1145

# 定义环境变量
# ENV NAME World

# 在容器启动时运行app.py
CMD ["python", "main.py"]
