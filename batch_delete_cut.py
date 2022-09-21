# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:50:23 2022

@author: HYF
"""

import os
import glob
import shutil

def movefile(indir:str,keywords:list,outdir:str,option = 'cover'):  #->int
    """
    Description:
    This is scripts is used to move file from a dir to the other dir
    Input：
    indir：原始数据所在的文件夹路径
    keywords: 进行区别的关键词
    outdir： 目标数据所在的文件夹路径
    option:  如果目标文件夹有同名数据的话，是覆盖还是跳过，默认是覆盖
    Output:  
    status： 1成功 0不成功
    Example:  movefile(r'E:\demo' ,['*.A' + str(year) + '*.hdf'],r'D:\result','continue')
    """
    if not os.path.exists(indir):       #判断原始文件路劲是否存在,如果不存在就直接退出
        print('The tardir is not exist:%s' % indir)
        status = 0
    else:
        for key in keywords:
            inlist = glob.glob(indir + os.sep + key)   #获得文件夹下所需要的数据
            print(f'The amount of data that in the "{key}"  is{len(inlist)}')
            for oripath in inlist:
                print(f'Processing......"{oripath}"')
                outdata = outdir + os.sep+ os.path.basename(oripath)   #获得目标文件夹下的数据的名称
                if os.path.exists(outdir):   #判断输出文件夹是否存在，如果存在执行以下操作
                    if os.path.exists(outdata):  #如果输出数据也存在就判断是跳过还是覆盖
                        if option == 'cover':
                            os.remove(outdata)
                            shutil.move(oripath, outdata)
                            print(f'"{oripath}"has been successfully transferred')
                        elif option == 'continue':
                            print(f'"{oripath}"has beenSuccessfully skipped')
                            continue
                    else:    #输出结果文件夹存在但是数据不存在也就直接移动
                        shutil.move(oripath, outdata)
                        print(f'"{oripath}"has been successfully transferred')
                else:
                    os.makedirs(outdir)               #目标文件夹不存在则创建目标文件夹并直接移动
                    shutil.move(oripath, outdata)
        status = 1

    return status

# def Rename(indir:str,key:list,add:str):  #->int
#     """
#     Description:
#     This is scripts is used to move file from a dir to the other dir
#     Input：
#     indir：原始数据所在的文件夹路径
#     keywords: 进行区别的关键词
#     outdir： 目标数据所在的文件夹路径
#     option:  如果目标文件夹有同名数据的话，是覆盖还是跳过，默认是覆盖
#     Output:  
#     status： 1成功 0不成功
#     Example:  movefile(r'E:\demo' ,['*.A' + str(year) + '*.hdf'],r'D:\result','continue')
#     """
#     if not os.path.exists(indir):       #判断原始文件路劲是否存在,如果不存在就直接退出
#         print('The tardir is not exist:%s' % indir)
#         status = 0
#     else:
#         inlist = glob.glob(indir + os.sep + key)   #获得文件夹下所需要的数据
#         print(f'The amount of data that in the "{key}"  is{len(inlist)}')
#         for oripath in inlist:
#             print(f'Processing......"{oripath}"')
#             outdata = indir + os.sep + add + str(os.path.basename(oripath).split('.')[:-1])   #获得目标文件夹下的数据的名称
#             os.rename(src, outdata)
#             print(f'"{oripath}"has been successfully transferred')
#             shutil.move(oripath, outdata)
#             print(f'"{oripath}"has been successfully transferred')
#         status = 1

#     return status

def delfile(indir:str,keywords:list):  #->int
    '''
    Description:
    This is scripts is used to delete file 
    Input:
    indir：原始数据所在的文件夹路径
    keywords: 进行区别的关键词
    Output:
    status： 1成功 0不成功
    Example:  delfile(r'E:\demo' ,['*.A' + str(year) + '*.hdf'])
    '''
    if not os.path.exists(indir):       #判断原始文件路劲是否存在,如果不存在就直接退出
        print('The deldir is not exist:%s' % indir)
        status = 0
    else:
        for key in keywords:
            dellist = glob.glob(indir + os.sep + key)
            print(f'The amount of data that in the "{key}" to be deleted is{len(dellist)}')
            for delpath in dellist:  
                os.remove(delpath)
                print(f'"{delpath}"has been successfully deleted')
        status =1
    return status
            

inpath = r'E:\Integrated_analysis_data\Data\1Y\MODIS_2000_2017_1y_chinese'

outpath = r'E:\Integrated_analysis_data\Data\1Y\W_1980_2020_1y_chinese'

styear = 2000

edyear = 2017

op = 'continue'

for year in range(styear,edyear+1):
#     # keys = ['npp_' + str(year) + '.tfw','npp_' + str(year) + '.tif.aux.xml','npp_' + str(year) + '.tif.xml']
#     #keys = ['*.tfw', '*.xml', '*.tif','*.ovr']
#     #keys = [str(year) + '_npp' + '.tif']
#     #keys = ['RNPP_' + str(year) + '.flt','RNPP_' + str(year) + '.hdr','RNPP_' + str(year) + '.png','RNPP_' + str(year) + '.prj','RNPP_' + str(year) + '.flt.aux.xml','RNPP_' + str(year) + '.flt.ovr']
#     #keys = ['RGPP_' + str(year) + '.flt','RGPP_' + str(year) + '.hdr','RGPP_' + str(year) + '.png','RGPP_' + str(year) + '.prj','RGPP_' + str(year) + '.flt.aux.xml','RGPP_' + str(year) + '.flt.ovr']
#     #keys = ['*_' + str(year) + '_' + '*.tif']
#     keys = ['Ma*']
#     #keys = ['A' + str(year) + '*.tfw','A' + str(year) + '*.xml','A' + str(year) + '*.tif','A' + str(year) + '*.ovr']
#     #keys = ['GLASS*.tif','GLASS*.tfw','GLASS*.xml','GLASS*.ovr']
    indir = inpath + os.sep + str(year)
#     #keys = ['GLASS*.hdf']
#     #keys = ['Mask_Mask_*.tif','Mask_Mask_*.tfw','Mask_Mask_*.xml','Mask_Mask_*.cpg','Mask_Mask_*.dbf','*.Global.tif',
#     #               '*_reproject.tif_reproject.tfw','*_reproject.tif_reproject.tif.*','*_reproject.tif_reproject.xml','*_reproject.tif_reproject.ovr']
    keys = ['Mask*']
    # outdir = outpath + os.sep + str(year)
    # result = movefile(inpath,keys,outdir,op)
    result = delfile(indir,keys)
#     print('-------完成--------' if result==1 else '-------输入文件夹不存在--------')
#     #print(hdfs)
    
# keys = ['Sum_*']
# result = movefile(inpath,keys,outpath,op)