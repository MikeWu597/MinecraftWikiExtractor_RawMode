import os
import json
import uuid

# 设置源文件夹和目标文件
source_folder = 'result_pieced\group_6'
output_file = 'combined_output6.jsonl'

# 打开输出文件
with open(output_file, 'w', encoding='utf-8') as jsonl_file:
    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith('.html'):
            file_path = os.path.join(source_folder, filename)
            
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            # 构建JSONL对象
            jsonl_object = {
                "custom_id": str(uuid.uuid4()),
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": "qwen-long-latest",
                    "messages": [
                        {
                            "role": "system",
                            "content": "我正在为RAG生成资料库文本数据。以下是一个来自minecraft wiki的页面，请帮我转换成适合导入RAG中的语言，尽可能不修改原文表述，遇到多媒体内容时，通过alt或者src来推断内容并转换成文字。直接输出你的结果，不需要复述我的话。"
                        },
                        {
                            "role": "user",
                            "content": html_content
                        }
                    ]
                }
            }
            
            # 将JSONL对象写入文件，每行一条记录
            jsonl_file.write(json.dumps(jsonl_object, ensure_ascii=False) + '\n')
            
            print(f"已处理文件: {filename}")

print(f"所有记录已合并到文件: {output_file}")