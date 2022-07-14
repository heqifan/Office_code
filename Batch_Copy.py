# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 22:03:02 2022

@author: HYF
"""


import os,sys,shutil

dir_path = r'F:\MetoGrid\TAVG\\'
hdr_path = r'F:\CarbonReport\Data\8DayData\RNEP\RGPP_2009185.hdr'
prj_path = r'F:\CarbonReport\Data\8DayData\RNEP\RGPP_2009185.prj'
for year in range(2002,2011+1):
    for day in range(1,366,8):
        day = "%03d"%(day)
        print(f'{year}_{day}')
        print(f'{dir_path}RGPP\\RGPP_{year}{day}.prj')
        shutil.copyfile(hdr_path,f'{dir_path}TAVG_{year}{day}.hdr')
        shutil.copyfile(prj_path,f'{dir_path}TAVG_{year}{day}.prj')
    