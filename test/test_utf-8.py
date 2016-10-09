#encoding=utf-8

content=u"广东松炀再生资源股份有限"
str1=u"测试"
content+=str1
print type(content)
content=content.encode("utf-8")#写入的文件编码格式为utf-8
print type(content)
with open("test-utf-8.txt","w")as f:
    f.write(content)