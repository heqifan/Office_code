# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 17:37:47 2022

@author: HYF
"""

import os
import win32com.client as win32
import easygui as eg


def save_as_xlsx(fname):
    excel = win32.DispatchEx('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname + "x", FileFormat=51)  # FileFormat = 51 is for .xlsx extension
    wb.Close()  # FileFormat = 56 is for .xls extension
    excel.Application.Quit()

def pick_package():
    # 打开windows窗口，选择一个文件夹
    return eg.diropenbox()

if __name__ == "__main__":
    package = pick_package()
    files = os.listdir(package)
    for fname in files:
        if fname.endswith(".xls"):
            print(fname + "正在进行格式转换，请稍后~")
            try:
                currentfile = package + "\\" + fname
                save_as_xlsx(currentfile)
                print(currentfile + "格式转换完成，O(∩_∩)O哈哈~")
            except:
                print(currentfile + "格式转换异常，┭┮﹏┭┮")
        else:
            print("跳过非xls文件：" + fname)
    input("输入任意键退出")
