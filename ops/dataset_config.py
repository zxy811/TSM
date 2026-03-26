# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu

import os

ROOT_DATASET = r"D:\保研\论文\pig_tsm"  # 项目根目录


def return_ucf101(modality):
    filename_categories = r"D:\保研\论文\UCF101\UCF101TrainTestSplits-RecognitionTask\ucfTrainTestlist\classInd.txt"
    if modality == 'RGB':
        root_data = r"D:\保研\论文\UCF101\picture"
        filename_imglist_train = r"D:\保研\论文\UCF101\label\ucf101_rgb_train_split_1.txt"
        filename_imglist_val = r"D:\保研\论文\UCF101\label\ucf101_rgb_val_split_1.txt"
        prefix = 'image_{:05d}.jpg'
    elif modality == 'Flow':
        root_data = ROOT_DATASET + 'UCF101/jpg'
        filename_imglist_train = 'UCF101/file_list/ucf101_flow_train_split_1.txt'
        filename_imglist_val = 'UCF101/file_list/ucf101_flow_val_split_1.txt'
        prefix = 'flow_{}_{:05d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_pig_fight(modality):
    """生猪争斗行为数据集配置"""
    filename_categories = r"D:\保研\论文\pig_tsm\label\classInd.txt"
    if modality == 'RGB':
        # root_data 应该指向抽帧后的图片根目录（包含 train 和 test 文件夹）
        root_data = r"D:\保研\论文\pig_tsm"
        filename_imglist_train = r"D:\保研\论文\pig_tsm\label\fight_rgb_train_split_1.txt"
        filename_imglist_val = r"D:\保研\论文\pig_tsm\label\fight_rgb_val_split_1.txt"
        prefix = 'image_{:05d}.jpg'
    elif modality == 'Flow':
        raise NotImplementedError('Flow modality not implemented for pig_fight dataset')
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_hmdb51(modality):
    filename_categories = 51
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'HMDB51/images'
        filename_imglist_train = 'HMDB51/splits/hmdb51_rgb_train_split_1.txt'
        filename_imglist_val = 'HMDB51/splits/hmdb51_rgb_val_split_1.txt'
        prefix = 'img_{:05d}.jpg'
    elif modality == 'Flow':
        root_data = ROOT_DATASET + 'HMDB51/images'
        filename_imglist_train = 'HMDB51/splits/hmdb51_flow_train_split_1.txt'
        filename_imglist_val = 'HMDB51/splits/hmdb51_flow_val_split_1.txt'
        prefix = 'flow_{}_{:05d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_something(modality):
    filename_categories = 'something/v1/category.txt'
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'something/v1/20bn-something-something-v1'
        filename_imglist_train = 'something/v1/train_videofolder.txt'
        filename_imglist_val = 'something/v1/val_videofolder.txt'
        prefix = '{:05d}.jpg'
    elif modality == 'Flow':
        root_data = ROOT_DATASET + 'something/v1/20bn-something-something-v1-flow'
        filename_imglist_train = 'something/v1/train_videofolder_flow.txt'
        filename_imglist_val = 'something/v1/val_videofolder_flow.txt'
        prefix = '{:06d}-{}_{:05d}.jpg'
    else:
        print('no such modality:'+modality)
        raise NotImplementedError
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_somethingv2(modality):
    filename_categories = 'something/v2/category.txt'
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'something/v2/20bn-something-something-v2-frames'
        filename_imglist_train = 'something/v2/train_videofolder.txt'
        filename_imglist_val = 'something/v2/val_videofolder.txt'
        prefix = '{:06d}.jpg'
    elif modality == 'Flow':
        # 修正：这里有严重的语法错误
        root_data = ROOT_DATASET + 'something/v2/20bn-something-something-v2-flow'
        filename_imglist_train = 'something/v2/train_videofolder_flow.txt'
        filename_imglist_val = 'something/v2/val_videofolder_flow.txt'
        prefix = '{:06d}.jpg'
    else:
        raise NotImplementedError('no such modality:'+modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_jester(modality):
    filename_categories = 'jester/category.txt'
    if modality == 'RGB':
        prefix = '{:05d}.jpg'
        root_data = ROOT_DATASET + 'jester/20bn-jester-v1'
        filename_imglist_train = 'jester/train_videofolder.txt'
        filename_imglist_val = 'jester/val_videofolder.txt'
    else:
        raise NotImplementedError('no such modality:'+modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_kinetics(modality):
    filename_categories = 400
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'kinetics/images'
        filename_imglist_train = 'kinetics/labels/train_videofolder.txt'
        filename_imglist_val = 'kinetics/labels/val_videofolder.txt'
        prefix = 'img_{:05d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_dataset(dataset, modality):
    # 添加 pig_fight 到数据集字典
    dict_single = {
        'jester': return_jester, 
        'something': return_something, 
        'somethingv2': return_somethingv2,
        'ucf101': return_ucf101, 
        'hmdb51': return_hmdb51,
        'kinetics': return_kinetics,
        'pig_fight': return_pig_fight  # 新增：注册生猪争斗数据集
    }
    
    if dataset in dict_single:
        file_categories, file_imglist_train, file_imglist_val, root_data, prefix = dict_single[dataset](modality)
    else:
        raise ValueError('Unknown dataset '+dataset)

    # UCF101 和 pig_fight 使用绝对路径，不需要再拼接 ROOT_DATASET
    if dataset in ['ucf101', 'pig_fight']:
        file_imglist_train = file_imglist_train
        file_imglist_val = file_imglist_val
        file_categories = file_categories
    else:
        file_imglist_train = os.path.join(ROOT_DATASET, file_imglist_train)
        file_imglist_val = os.path.join(ROOT_DATASET, file_imglist_val)
        if isinstance(file_categories, str):
            file_categories = os.path.join(ROOT_DATASET, file_categories)
    
    if isinstance(file_categories, str):
        with open(file_categories) as f:
            lines = f.readlines()
        categories = [item.rstrip() for item in lines]
    else:  # number of categories
        categories = [None] * file_categories
    n_class = len(categories)
    print('{}: {} classes'.format(dataset, n_class))
    return n_class, file_imglist_train, file_imglist_val, root_data, prefix
