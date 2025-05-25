import os
from bs4 import BeautifulSoup, Comment  # 修正模块名称并导入Comment类

# 设置源文件夹和目标文件夹
source_folder = 'result_fetched/result'
target_folder = 'result_distilled'

# 创建目标文件夹（如果不存在）
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹中的所有HTML文件
for filename in os.listdir(source_folder):
    if filename.endswith('.html'):
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)
        
        # 检查目标文件是否已存在
        if os.path.exists(target_path):
            print(f"跳过已存在的文件: {filename}")
            continue
        
        # 读取源文件内容
        with open(source_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 删除HTML中的注释
        for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
            comment.extract()

        # 删除所有style元素
        style_elements = soup.find_all('style')
        for element in style_elements:
            element.decompose()

        # 删除所有id为siteNotice的元素
        site_notice_elements = soup.find_all(id='siteNotice')
        for element in site_notice_elements:
            element.decompose()
        
        # 删除所有class为mw-jump-link的元素
        mw_jump_link_elements = soup.find_all(class_='mw-jump-link')
        for element in mw_jump_link_elements:
            element.decompose()
        
        # 删除所有class为mw-indicators的元素
        mw_indicators_elements = soup.find_all(class_='mw-indicators')
        for element in mw_indicators_elements:
            element.decompose()
        
        # 删除所有class为printfooter的元素
        printfooter_elements = soup.find_all(class_='printfooter')
        for element in printfooter_elements:
            element.decompose()
        
        # 删除所有class为noprint的元素
        noprint_elements = soup.find_all(class_='noprint')
        for element in noprint_elements:
            element.decompose()
        
        # 删除所有id为top的元素
        top_elements = soup.find_all(id='top')
        for element in top_elements:
            element.decompose()

        # 删除符合条件的h2和table
        for h2 in soup.find_all('h2'):
            span = h2.find('span', id='导航')
            if span:
                next_sibling = h2.find_next_sibling()
                if next_sibling and next_sibling.name == 'table':
                    h2.decompose()
                    next_sibling.decompose()

        # 提取body标签下id为content的div内容
        content_div = soup.find('div', id='content')
        if content_div:
            # 删除其他属性，只保留src、alt、href、title
            for tag in content_div.find_all(True):
                attrs_to_keep = ['src', 'alt', 'href', 'title']
                attrs_to_remove = [attr for attr in tag.attrs if attr not in attrs_to_keep]
                for attr in attrs_to_remove:
                    del tag[attr]
            
            # 创建新的HTML文档
            distilled_html = f"<html><body>{str(content_div)}</body></html>"
            
            # 保存到目标文件
            with open(target_path, 'w', encoding='utf-8') as file:
                file.write(distilled_html)
            print(f"已处理文件: {filename}")
        else:
            print(f"未找到id为content的div: {filename}")