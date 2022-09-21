# -- coding: utf-8 --
import shutil
import winshell
# path = 'images/' #路径
# shutil.rmtree(path) #删除文件夹
# os.mkdir(path)#重建同名文件夹
winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)#清空回收站