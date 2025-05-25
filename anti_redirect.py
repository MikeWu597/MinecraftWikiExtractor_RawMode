import os

# 设置源文件夹
source_folder = 'result_redirect_removed'

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    # 检查文件是否为普通文件
    if os.path.isfile(file_path):
        # 删除文件名中含有“（消歧义）”的文件
        if "（消歧义）" in filename:
            os.remove(file_path)
            print(f"已删除文件: {filename}")
            continue
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 检查内容是否包含“重定向自”
        if "这个<a href=\"https://zh.wikipedia.org/wiki/Wikipedia:%E6%B6%88%E6%AD%A7%E4%B9%89\" title=\"wzh:Wikipedia:消歧义\">消歧义" in content:
            # 删除文件
            os.remove(file_path)
            print(f"已删除文件: {filename}")
        #else:
            #print(f"未删除文件: {filename}")