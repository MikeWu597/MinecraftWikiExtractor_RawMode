import os
import shutil

def piece_files(source_folder, target_folder, n):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # 获取源文件夹中的所有文件
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # 计算需要的子文件夹数量
    num_subfolders = (len(files) + n - 1) // n
    
    # 将文件分组并保存到子文件夹中
    for i in range(num_subfolders):
        subfolder_name = f"group_{i+1}"
        subfolder_path = os.path.join(target_folder, subfolder_name)
        
        # 创建子文件夹
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        
        # 计算当前子文件夹的文件范围
        start_index = i * n
        end_index = min((i + 1) * n, len(files))
        
        # 复制文件到子文件夹
        for j in range(start_index, end_index):
            source_file_path = os.path.join(source_folder, files[j])
            target_file_path = os.path.join(subfolder_path, files[j])
            shutil.copy(source_file_path, target_file_path)
        
        print(f"已处理文件组: {subfolder_name}")

# 设置源文件夹、目标文件夹和每组文件数量
source_folder = 'result_redirect_removed'
target_folder = 'result_pieced'
n = 1000  # 每组文件数量，你可以根据需要修改这个值

# 调用函数进行文件分组
piece_files(source_folder, target_folder, n)