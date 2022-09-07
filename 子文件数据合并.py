# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:46:52 2022

@author: HYF
"""

import shutil,os

origin_path = r'E:\流域\dem'
target_path = r'E:\流域\all_dem'

for o_dir, sub_f, files in os.walk(origin_path):
    # print('o_dir: ', o_dir) # 当前文件夹「路径」的字符串
    # print('sub_f: ', sub_f) # 当前文件夹的「子文件夹的列表」
    # print('files: ', files) # 当前文件夹的「文件名称的列表」
    
    for i in range(len(files)):
        if files[i].endswith(('.img')): 
            file_path = o_dir + '/' + files[i]
            temp_file_name = o_dir.replace(origin_path, '').replace('/', '_')
            if len(temp_file_name) > 1:
                temp_file_name = temp_file_name[1:len(origin_path)] + '_'
            new_path = target_path + '/' + temp_file_name + files[i]
            shutil.copy2(file_path, new_path)
            
