import hashlib

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        # 分块读取文件内容，适用于大文件
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# 示例用法
file_path = r'D:\Station8-流量分析与入侵检测\流量分析与入侵检测.vmdk'
md5_value = calculate_md5(file_path)
print("MD5 value:", md5_value)