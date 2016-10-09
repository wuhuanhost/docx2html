# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os, base64,re

htmlDoc="""
	<!DOCTYPE HTML>
	<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
	<img src="" alt="1" />
	<img src="" alt="2" />
	<img src="" alt="3" />
	</body>
	</html>
"""

#脚本运行的根目录
homedir = os.getcwd()
logs=open('f.txt','a')
'''
	解析使用base64编码的图片节点数据
'''
def resloveBaseData(data,index):
	print u"解析base64编码的图片第【",index,u"】张开始"
	#图片的类型
	_imgType=re.search(r'(?<=:).*(?=;)',data).group().split("/")[1]
	#生成的图片名称
	fileName="".join((str(index),".",_imgType))
	print fileName
	#图片数据
	_imgData=re.search(r'(?<=,).*',data).group()
	logs.write("\n")
	logs.write(_imgData)
	base64ToFile(_imgData,fileName)
	print u"解析base64编码的图片第【",index,u"】张结束"
	return "","img\\",fileName;

'''
	base64数据转图片
'''
def base64ToFile(baseData,fileName):
	imgData = base64.b64decode(baseData)
	imgFile = open(os.path.join(homedir,"img",fileName),'wb')
	imgFile.write(imgData)
	imgFile.close()



with open("1.html","r") as f:
	htmlDoc=f.read();

soup = BeautifulSoup(htmlDoc)
#获取页面所有的img节点
listImg=soup.find_all('img')
#print listImg[0]
#img节点的下标
index=0;
for img in listImg:
	_temp=listImg[index]['src']
	#修改图片集合中下标为index的图片的alt属性
	listImg[index]['src']=resloveBaseData(_temp,index)
	#下标增加
	index+=1
print soup






with open("a.html","wb") as f:
	f.write(soup.encode('utf-8'))


#测试
#resloveBase64("data:image/jpeg;base64,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",1)