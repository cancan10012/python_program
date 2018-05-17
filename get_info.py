import re
def ParaseMessage(strFilePath,strKey,strMessage):
	try:
		text_strFilePath=open(strFilePath)
		regular=text_strFilePath.read() #将文本全部读取到text_all里面
		text_strFilePath.close()
		Message=strMessage
		Message=list(re.findall(regular,Message)[0])#先用正则表达式将原来的message分割开，然后将其转换成一个list重新赋值给message
		Message_dic={'{{program}}':Message[0],'{{branch}}':Message[1],'{{build_engine}}':Message[2],\
		'{{build_version}}':Message[3],'{{diags_version}}':Message[4],'{{revision}}':Message[5]}
		return (Message_dic[strKey])
	except BaseException as error:
		return ('ParaseFail')	

		
#下面是尝试调用子程序的测试程序
if __name__ == '__main__':
	#a=ParaseMessage("Version.txt","{{branch}}","test Diag (this is the anser)\nwho build Ver 0.0.1 (dia 0.0.2). Revision Ver3.9.1.\nBuilt at 20180909")
	#print(a)
	
	print(re.findall("((.*))","(123)"))