#-*- coding:utf-8 -*-
import os
"""
删除文件和目录的方法
如果是文件直接删除
如果是目录，递归删除目录下的文件
"""
def delete_file_folder(src):
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            delete_file_folder(itemsrc) 
        try:
            os.rmdir(src)
        except:
            pass

#测试
#delete_file_folder("E:\\docx2html\\src\\utils\\123")

print os.path.dirname(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","data","txt.txt"))  
