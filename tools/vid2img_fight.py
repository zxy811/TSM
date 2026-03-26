from __future__ import print_function, division
import os
import sys
import subprocess
import shutil

def process_videos(split_path, dst_dir_path, split_name):
    """
    处理 train 或 test 文件夹中的视频
    split_path: train 或 test 文件夹路径
    dst_dir_path: 抽帧后图片存放的根目录
    split_name: 'train' 或 'test'
    """
    # 创建输出目录
    dst_split_path = os.path.join(dst_dir_path, split_name)
    if not os.path.exists(dst_split_path):
        os.makedirs(dst_split_path)
        print(f'创建split文件夹: {dst_split_path}')
    
    # 遍历 fight 和 nofight 两个类别
    for class_name in ['fight', 'nofight']:
        class_path = os.path.join(split_path, class_name)
        if not os.path.isdir(class_path):
            print(f'警告：找不到类别文件夹 {class_path}')
            continue
        
        dst_class_path = os.path.join(dst_split_path, class_name)
        if not os.path.exists(dst_class_path):
            os.makedirs(dst_class_path)
            print(f'创建类别文件夹: {dst_class_path}')
        
        # 处理该类别下的所有视频文件
        video_files = [f for f in os.listdir(class_path) if f.endswith(('.avi', '.mp4', '.AVI', '.MP4'))]
        print(f'在 {class_name} 中找到 {len(video_files)} 个视频文件')
        
        for file_name in video_files:
            name, ext = os.path.splitext(file_name)
            dst_directory_path = os.path.join(dst_class_path, name)
            video_file_path = os.path.join(class_path, file_name)
            
            try:
                if os.path.exists(dst_directory_path):
                    if not os.path.exists(os.path.join(dst_directory_path, 'image_00001.jpg')):
                        shutil.rmtree(dst_directory_path)
                        print(f'删除并重建: {dst_directory_path}')
                        os.makedirs(dst_directory_path)
                    else:
                        print(f'跳过已处理: {name}')
                        continue
                else:
                    os.makedirs(dst_directory_path)
                    print(f'创建视频文件夹: {dst_directory_path}')
            except Exception as e:
                print(f"创建目录失败: {dst_directory_path}, 错误: {e}")
                continue
            
            # FFmpeg 路径
            ffmpeg_exe_path = r"D:\保研\论文\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
            
            # 检查 FFmpeg 是否存在
            if not os.path.exists(ffmpeg_exe_path):
                print(f"错误：找不到 FFmpeg，请检查路径: {ffmpeg_exe_path}")
                sys.exit(1)
            
            # 输出文件路径模板
            output_pattern = os.path.join(dst_directory_path, "image_%05d.jpg")
            
            # 构建命令
            cmd = '"{}" -i "{}" -vf scale=-1:480 "{}"'.format(
                ffmpeg_exe_path,
                video_file_path,
                output_pattern
            )
            
            print(f'执行命令: {cmd}')
            try:
                result = subprocess.call(cmd, shell=True)
                if result != 0:
                    print(f'FFmpeg 执行失败，返回码: {result}')
                else:
                    print(f'成功处理: {name}')
            except Exception as e:
                print(f'执行 FFmpeg 出错: {e}')
            print('\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python vid2img_fight.py <视频根目录> <输出目录>")
        print("示例: python vid2img_fight.py D:\\dataset\\videos D:\\dataset\\frames")
        sys.exit(1)
    
    video_root = sys.argv[1]  # 包含 train 和 test 文件夹的根目录
    output_root = sys.argv[2]  # 抽帧后图片存放的根目录
    
    # 处理 train 和 test
    for split in ['train', 'test']:
        split_path = os.path.join(video_root, split)
        if os.path.exists(split_path):
            print(f'\n开始处理 {split} 数据...')
            process_videos(split_path, output_root, split)
        else:
            print(f'警告：找不到 {split} 文件夹: {split_path}')
    
    print('\n所有视频处理完成！')
