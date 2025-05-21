import os
import urllib.parse
from curl_cffi import requests
import time
import random
import json

try:
    with open('titles.json', 'r', encoding='utf-8') as f:
        directories = json.load(f)
except Exception as e:
    print(f"Error loading titles.json: {e}")
    exit(1)

# 基础URL
base_url = "https://zh.minecraft.wiki/w/"

# 创建result目录
result_dir = "result"
os.makedirs(result_dir, exist_ok=True)

for directory in directories:
    # URL编码
    encoded_dir = urllib.parse.quote(directory)
    # 拼接完整URL
    full_url = base_url + encoded_dir

    # 构建文件路径
    filename = f"{directory.replace('/', '_')}.html"  # 替换斜杠为下划线以避免路径问题
    file_path = os.path.join(result_dir, filename)

    # 判断文件是否已存在
    if os.path.exists(file_path):
        print(f"File {file_path} already exists. Skipping...")
        continue

    try:
        # 使用curl_cffi发起请求
        response = requests.get(full_url, impersonate="chrome")
        # 打印状态码和部分内容以确认结果
        print(f"Status code for {full_url}: {response.status_code}")

        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Saved content to {file_path}")
    except Exception as e:
        print(f"Error fetching {full_url}: {e}")

    # 添加随机延迟，避免对服务器造成过大压力
    delay = random.uniform(1, 4)  # 随机生成1至4秒之间的延迟时间
    print(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)  # 等待指定的延迟时间