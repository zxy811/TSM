from __future__ import print_function, division
import os
import sys
import subprocess
import shutil

def class_process(dir_path, dst_dir_path, class_name):
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        return

    dst_class_path = os.path.join(dst_dir_path, class_name)
    if not os.path.exists(dst_class_path):
        os.makedirs(dst_class_path)
        print(f'创建类别文件夹: {dst_class_path}')

    for file_name in os.listdir(class_path):
        if '.avi' not in file_name:
            continue
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
                    print(f'跳过已处理: {dst_directory_path}')
                    continue
            else:
                os.makedirs(dst_directory_path)
                print(f'创建视频文件夹: {dst_directory_path}')
        except Exception as e:
            print(f"创建目录失败: {dst_directory_path}, 错误: {e}")
            continue
        
        # 修正后的 FFmpeg 路径（注意重复的文件夹名）
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

if __name__=="__main__":
    dir_path = sys.argv[1]      # 视频文件总路径
    dst_dir_path = sys.argv[2]   # 抽帧后图片存放路径

    for class_name in os.listdir(dir_path):
        class_process(dir_path, dst_dir_path, class_name)
