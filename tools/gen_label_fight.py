import os
import glob
import fnmatch

# ===== 配置路径 =====
# 抽帧后的图片根目录
frames_root = r"D:\保研\论文\pig_tsm"

# 输出标签文件的目录
label_output_path = r"D:\保研\论文\pig_tsm\label"

# 数据集名称
dataset_name = "fight"
# ===================

def count_files(directory, prefix='image_'):
    """统计目录中符合前缀的文件数量"""
    if not os.path.exists(directory):
        return 0
    lst = os.listdir(directory)
    cnt = len(fnmatch.filter(lst, prefix + '*'))
    return cnt

def parse_frames_directory(frames_path, split):
    """
    解析抽帧后的目录结构
    frames_path: 帧图片根目录
    split: 'train' 或 'test'
    返回: {视频名: (完整路径, 帧数, 标签)}
    """
    print(f'解析 {split} 数据集的帧文件夹...')
    
    video_info = {}
    class_mapping = {'fight': 0, 'nofight': 1}
    
    split_path = os.path.join(frames_path, split)
    if not os.path.exists(split_path):
        print(f'警告：找不到 {split} 文件夹: {split_path}')
        return video_info
    
    # 遍历 fight 和 nofight 两个类别
    for class_name in ['fight', 'nofight']:
        class_path = os.path.join(split_path, class_name)
        if not os.path.exists(class_path):
            print(f'警告：找不到类别文件夹: {class_path}')
            continue
        
        label = class_mapping[class_name]
        
        # 遍历该类别下的所有视频文件夹
        video_folders = [d for d in os.listdir(class_path) 
                        if os.path.isdir(os.path.join(class_path, d))]
        
        print(f'  - {class_name}: 找到 {len(video_folders)} 个视频')
        
        for video_name in video_folders:
            video_path = os.path.join(class_path, video_name)
            frame_count = count_files(video_path, prefix='image_')
            
            if frame_count > 0:
                # 构建完整路径（用于写入txt文件）
                full_path = os.path.join(frames_root, split, class_name, video_name)
                video_info[video_name] = (full_path, frame_count, label)
            else:
                print(f'  警告：{video_name} 没有找到帧图片，跳过')
    
    print(f'{split} 数据集解析完成，共 {len(video_info)} 个有效视频\n')
    return video_info

def generate_split_file(video_info, output_file):
    """
    生成训练/测试的txt文件
    格式：视频路径 帧数 标签
    """
    lines = []
    for video_name, (path, frame_count, label) in sorted(video_info.items()):
        line = f'{path} {frame_count} {label}\n'
        lines.append(line)
    
    with open(output_file, 'w') as f:
        f.writelines(lines)
    
    print(f'已生成: {output_file} (共 {len(lines)} 个视频)')

def generate_class_index(output_path):
    """生成类别索引文件 classInd.txt"""
    class_file = os.path.join(output_path, 'classInd.txt')
    with open(class_file, 'w') as f:
        f.write('1 fight\n')
        f.write('2 nofight\n')
    print(f'已生成类别索引文件: {class_file}\n')

def main():
    # 创建输出目录
    if not os.path.exists(label_output_path):
        os.makedirs(label_output_path)
        print(f'创建输出目录: {label_output_path}\n')
    
    # 生成类别索引文件
    generate_class_index(label_output_path)
    
    # 处理 train 数据集
    train_info = parse_frames_directory(frames_root, 'train')
    if train_info:
        train_file = os.path.join(label_output_path, f'{dataset_name}_rgb_train_split_1.txt')
        generate_split_file(train_info, train_file)
    
    # 处理 test 数据集
    test_info = parse_frames_directory(frames_root, 'test')
    if test_info:
        val_file = os.path.join(label_output_path, f'{dataset_name}_rgb_val_split_1.txt')
        generate_split_file(test_info, val_file)
    
    print('\n所有标签文件生成完成！')
    print(f'输出目录: {label_output_path}')
    print(f'生成的文件:')
    print(f'  - classInd.txt')
    print(f'  - {dataset_name}_rgb_train_split_1.txt')
    print(f'  - {dataset_name}_rgb_val_split_1.txt')

if __name__ == '__main__':
    main()
