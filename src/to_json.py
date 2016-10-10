#-*- coding:utf-8 -*-
import re,json,os

"""
获取每一页的数据
"""

"""
将txt数据生成一个二维数组
"""
def get_page(txt_path):
	with open(txt_path,"rb") as f:
		txt=f.read()
		page_arr=re.split('[-]{3,}.*[-]{3,}',txt)
		page_data=[]
		for page in page_arr:
			line_data=[]
			line_arr=page.replace("\r","").split("\n\n")
			for line in line_arr:
				if line!="":
					line_data.append(line)
				#print type(line)
			page_data.append(line_data)
	return page_data


def to_json(txt_path,json_path):
	page_data=get_page(txt_path)
	page_data=json.dumps(page_data,ensure_ascii=False)
	with open(json_path,"wb") as f:
		f.write(page_data)

txtpath=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data","txt","1.txt"))
jsonpath=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data","json","1.json"))



to_json(txtpath,jsonpath)