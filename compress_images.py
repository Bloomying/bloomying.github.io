from PIL import Image
import os

def compress_image(input_path, output_path, max_size_mb=1.0, quality=85):
    """
    压缩图片到指定大小以下
    
    参数:
    input_path: 输入图片路径
    output_path: 输出图片路径
    max_size_mb: 目标最大文件大小（MB）
    quality: 初始质量值 (1-95)
    """
    # 打开图片
    img = Image.open(input_path)
    
    # 如果是RGBA模式，转换为RGB
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # 初始压缩
    img.save(output_path, 'JPEG', quality=quality, optimize=True)
    
    # 如果文件仍然太大，继续降低质量直到达到目标大小
    while os.path.getsize(output_path) > max_size_mb * 1024 * 1024 and quality > 5:
        quality -= 5
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
    
    # 获取压缩前后的文件大小
    original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
    compressed_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
    
    print(f"压缩完成: {os.path.basename(input_path)}")
    print(f"原始大小: {original_size:.2f}MB")
    print(f"压缩后大小: {compressed_size:.2f}MB")
    print(f"压缩率: {(1 - compressed_size/original_size)*100:.2f}%")
    print(f"最终质量: {quality}")
    print("-" * 50)

def batch_compress_images(input_dir, output_dir, max_size_mb=1.0):
    """
    批量压缩文件夹中的图片
    
    参数:
    input_dir: 输入文件夹路径
    output_dir: 输出文件夹路径
    max_size_mb: 目标最大文件大小（MB）
    """
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 支持的图片格式
    supported_formats = {'.jpg', '.jpeg', '.png', '.webp'}
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        # 检查文件扩展名
        if any(filename.lower().endswith(fmt) for fmt in supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"compressed_{filename.split('.')[0]}.jpg")
            
            try:
                compress_image(input_path, output_path, max_size_mb)
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")

if __name__ == "__main__":
    # 使用示例
    input_directory = "original_images"  # 原始图片文件夹
    output_directory = "compressed_images"  # 压缩后图片保存文件夹
    target_size = 1.0  # 目标文件大小（MB）
    
    batch_compress_images(input_directory, output_directory, target_size) 