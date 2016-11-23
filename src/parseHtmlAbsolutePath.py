#-*- coding:utf-8 -*-
import mammoth
import sys,os, base64,re,uuid
from utils.remove_file_folder import delete_file_folder
from docx import to_latex

input_argv = sys.argv[1];
inputFile=input_argv

#base64转图片
def base64ToFile(baseData,file_name):
	imgData = base64.b64decode(baseData)
	imgFile = open(os.path.join(os.path.abspath(inputFile),os.pardir,os.pardir,"images/",file_name),'wb')
	imgFile.write(imgData)
	imgFile.close()

"""
src标签中的base64编码的图片写到文件中
"""
def convert_image(image):
    with image.open() as image_bytes:
        encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")
	#print image.__dict__
	img_type=image.content_type.split("/")[1]
	img_data=encoded_src
	img_file_name="".join((str(uuid.uuid1()),".",img_type))
	#print img_file_name
	base64ToFile(img_data,img_file_name)
	return {
        "src": os.path.join(os.path.abspath(inputFile),os.pardir,os.pardir,"images/",img_file_name)
}


#替换docx中的公式为latex
to_latex(filename=inputFile);


"""
生成html
"""
def gen_html():
	document=u"<!DOCTYPE html><html lang='zh_CN'><head><meta charset='UTF-8'><title>Document</title><style>table,table td,table th{border:1px solid;border-collapse: collapse;}</style></head><body>";
	print type(document)
	style_map = "u => u"
	with open(inputFile, "rb") as docx_file:
		result = mammoth.convert_to_html(docx_file,convert_image=mammoth.images.img_element(convert_image),style_map=style_map)
		html = result.value
		messages = result.messages
	#document+=html #不能使用+=的方式这样会出现乱码
	document=document+html
	document=document+u"<script type='text/x-mathjax-config'>MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['@@','@@']]}});</script>"
	document=document+u"<script type='text/javascript' async src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML'></script></body></html>"
	document=document.encode('utf-8')
	print html.encode("utf-8")


#调用
gen_html();