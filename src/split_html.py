#-*- coding:utf-8 -*-
"""
按照6个中划线的字符串分割html
"""
import re,os


"""
读取html
"""
def read_html(file_name):
	with open(file_name,"rb") as f:
		html_str=f.read()
		f.close()
	return html_str



"""
根据<p>------</p>或者<em>------</em>将html分割成每一页
"""
def split_html(html_str):
	arr=re.split('<\w+?>[-]{6,}<\/\w+?>',html_str)
	#arr=re.split('<.{1,3}>[-]{6,}<\/.{1,3}>',html_str)
	return arr


"""
循环每一页的数据并且将每一页中的字符串按照<p>......</p>取出来，生成一个二维数组
"""
def process_html(htmlarr):
	arr=[]
	for page in htmlarr:
		pagearr=[]
		line_arr=re.findall('<table>.*?<\/table>|<p>.*?<\/p>',page)
		for line in line_arr:
			pagearr.append(line)
		arr.append(pagearr)
	return arr


"""
将每一页每一行的数据写入txt文本中
"""
txtpath=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data","txt","2.txt"))
htmlpath=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data","html","02.html"))

def write_txt(txt_path,pagearr):
	page_index=0
	temp_str=''
	#每一页
	for page in pagearr:
		#每一行
		for line in page:
			#print line
			temp_str=temp_str+line+"\r\n\r\n"
		temp_str=temp_str+"---分页符号"+str(page_index+1)+"---\r\n\r\n"
		page_index+=1
	with open(txt_path,"wb") as f:
		f.write(temp_str.replace("<p>","").replace("</p>",""))



"""
替换文档中的所有的img节点,为节点增加狂傲属性，最后返回替换后的文档字符串
"""
def process_img(htmlstr):
	"""
	re.sub的第一个参数为正则表达式，第二个参数为回调函数，第三个参数为要处理的字符串
	"""
	htmlstr=re.sub(r'<img.*?>',newstr,htmlstr)
	return htmlstr

	


"""
替换img标签时候的处理函数
"""
def newstr(match):
	img=match.group(0)
	img_element_arr=img.split(" ");#  [[<img] [alt='111,222'] [src='123.jpg'>]]
	alt_arr=img_element_arr[1].split(",") #
	img_width=alt_arr[1]
	img_height=alt_arr[2].replace("\"","")
	print img_width+">"+str(emu2px(img_width))+" | "+img_height+">"+str(emu2px(img_height))
	return img_element_arr[0]+" "+img_element_arr[1]+" width='"+str(emu2px(img_width))+"px'"+" height='"+str(emu2px(img_height))+"px' "+img_element_arr[2];


"""
docx中的图片使用的emu绝对单位，转为像素的方法为
"""
def emu2px(emu):
	emu=float(emu)
	return round((emu / 360000 * 96 / 2.54),2)



#teststr="<img alt="id:2147507627;FounderCES,1106280,380880" src='123.jpg'>或者<img alt="id:2147507627;FounderCES,1106280,380880" src='456.jpg'>";

#process_img(teststr)

"""
程序入口方法
"""
def process_start(html_path,txt_path):
	#读取
	htmlstr=read_html(html_path)
	#替换图片节点
	htmlstr=process_img(htmlstr)
	#分割成每一页
	htmlarr=split_html(htmlstr)
	#处理成每一页每一行
	arr=process_html(htmlarr)
	#写入txt中
	write_txt(txt_path,arr)
	#print arr


process_start(htmlpath,txtpath)