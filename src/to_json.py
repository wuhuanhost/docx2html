#-*- coding:utf-8 -*-
import re,json

"""
获取每一页的数据
"""
def get_page():
	with open("E:\\docx2html\\data\\txt\\txt.txt","rb") as f:
		txt=f.read()
		page_arr=re.split('[-]{3,}.+?[-]{3,}',txt)
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



def to_json(page_data):
	with open("E:\\docx2html\\data\\json\\json.json","wb") as f:
		f.write(page_data)


page_data=get_page()
#print page_data
to_json(json.dumps(page_data,ensure_ascii=False))


