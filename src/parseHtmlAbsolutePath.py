#-*- coding:utf-8 -*-
import mammoth
import sys,os, base64,re,uuid
from utils.remove_file_folder import delete_file_folder
from docx import to_latex
reload(sys)
sys.setdefaultencoding('gbk')

input_argv = sys.argv[1]
inputFile=input_argv
imgIndex=0

#base64转图片
def base64ToFile(baseData,file_name):
	imgData = base64.b64decode(baseData)
	imgFile = open(os.path.join(os.path.abspath(inputFile),os.pardir,os.pardir,"images/",os.path.basename(file_name)),'wb')
	#print imgFile
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
	global imgIndex # 声明imgIndex为全局变量
	imgIndex=imgIndex+1
	img_file_name=inputFile+"-"+str(imgIndex)+"."+img_type
	#print img_file_name
	base64ToFile(img_data,img_file_name)
	return {
        #"relative-src": "../images/"+img_file_name,
		"src":os.path.abspath(os.path.join(os.path.abspath(inputFile),os.pardir,os.pardir,"images/",os.path.basename(img_file_name)))
}


#替换docx中的公式为latex
to_latex(filename=inputFile);


"""
生成html
"""
def gen_html():
	document=u"<!DOCTYPE html><html lang='zh_CN'><head><meta charset='UTF-8'><title>Document</title><style>table,table td,table th{border:1px solid;border-collapse: collapse;}</style></head><body>";
	#print type(document)
	style_map = "u => u"
	with open(inputFile, "rb") as docx_file:
		result = mammoth.convert_to_html(docx_file,convert_image=mammoth.images.img_element(convert_image),style_map=style_map)
		html = result.value
		messages = result.messages
	#document+=html #不能使用+=的方式这样会出现乱码
	document=document+html
	document=document+u"</body></html>"
	document=document.encode('utf-8')
	document=re.sub(r'<img.*?>',newstr,document)
	print document+"@@@end@@@"  #@@@end@@@为结束标志的字符串，node中执行命令行程序的时候是异步获取数据的，当数据


"""
替换img标签时候的处理函数
"""
def newstr(match):
	img=match.group(0)
	img_element_arr=img.split(" ");#  [[<img] [alt='111,222'] [src='123.jpg'>]]
	alt_arr=img_element_arr[1].split(",") #
	img_width=alt_arr[1]
	img_height=alt_arr[2].replace("\"","")
	#print img_width+">"+str(emu2px(img_width))+" | "+img_height+">"+str(emu2px(img_height))
	return "<img "+img_element_arr[1]+" "+img_element_arr[2]+" width='"+str(emu2px(img_width))+"px'"+" height='"+str(emu2px(img_height))+"px'/>";


"""
docx中的图片使用的emu绝对单位，转为像素的方法为
"""
def emu2px(emu):
	emu=float(emu)
	return round((emu / 360000 * 96 / 2.54),2)



#调用
gen_html();