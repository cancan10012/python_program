def ParaseMessage(strFilePath,strKey,strMessage):	
	import re
	text_strFilePath=open(strFilePath)
	strOne=text_strFilePath.read() #将文本全部读取到text_all里面
	text_strFilePath.close()
	#print(strOne)
	strTwo=re.sub("\(","\(",strOne)#左括号加转义
	strThree=re.sub("\)","\)",strTwo)#右括号加转义
	strFour=re.sub("\.","\.",strThree)# . 加转义
	rexOne=re.sub("(%s)"%(strKey),'(.*)',strFour)#把要取的key换成(.*)，括号里是要取出来里面的内容
	rexTwo=re.sub("{{.*?}}",".*",rexOne)#把格式里面没有用到的key全部换成 .* 构成正则表达式
	#print(rexTwo)
	#print(strMessage)
	info=(re.findall(rexTwo,strMessage))[0]#re.findall取出来的是list，将第0项取出来就是要的数据的str
	return(info)	

if __name__ == '__main__':
	a=ParaseMessage("Version.txt","{{branch}}","pro Diag (branch.000)\n\
		engin build version (diags_version). Revision revision.\n  Built at build_date_time")
	print(a)