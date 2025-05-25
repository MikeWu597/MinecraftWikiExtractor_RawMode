import os
from bs4 import BeautifulSoup

# 设置源文件夹
source_folder = 'result_redirect_removed'

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.html'):
        file_path = os.path.join(source_folder, filename)
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 查找符合条件的<ul>元素
        for ul in soup.find_all('ul'):
            li_texts = [li.get_text(strip=True) for li in ul.find_all('li')]
            if li_texts == ['查', '论', '编']:
                # 找到<ul>所在的<table>并删除
                table = ul.find_parent('table')
                if table:
                    table.decompose()
        
        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        
        print(f"已处理文件: {filename}")