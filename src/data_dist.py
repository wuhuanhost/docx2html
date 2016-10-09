# -*- coding: utf-8 -*-
import os
print os.path.dirname(os.path.abspath('__file__'))
cwd_dir = os.getcwd()
print cwd_dir
#docx所在目录
docx_dir= os.path.abspath(os.path.join(cwd_dir,os.path.pardir,"data","docx"))
#html所在的目录
html_dir= os.path.abspath(os.path.join(cwd_dir,os.path.pardir,"data","html"))
#txt文件所在的目录
txt_dir= os.path.abspath(os.path.join(cwd_dir,os.path.pardir,"data","txt"))

#图片所在的目录
img_dir=os.path.abspath(os.path.join(cwd_dir,os.path.pardir,"data","img"))

dd={
	'docx_dir':docx_dir,
	'html_dir':html_dir,
	'txt_dir':txt_dir,
	'img_dir':img_dir
}
