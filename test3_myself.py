import re

def PraseMessage(strFilePath,strKeyName,strMessage):
	#Create the Return Value
	bResult = True
	strTargetMessage=[]
	try:
		text_strFilePath=open(strFilePath)
		strStepOne=text_strFilePath.read()
		text_strFilePath.close()
		if strStepOne.find(strKeyName)>=0:
			#print(strStepOne)
			strStepTwo=re.sub("\(","\(",strStepOne)#左括号加转义
			strStepThree=re.sub("\)","\)",strStepTwo)#右括号加转义
			strFour=re.sub("\.","\.",strStepThree)# . 加转义
			rexStepOne=re.sub("(%s)"%(strKeyName),'(.*)',strFour)#把要取的key换成(.*)，括号里是要取出来里面的内容
			rexTarget=re.sub("{{.*?}}",".*",rexStepOne)#把格式里面没有用到的key全部换成 .* 构成正则表达式
			#print(rexTarget)
			resultlist=(re.findall(rexTarget,strMessage))
			#print(resultlist)

			if len(resultlist)==1:
				strTargetMessage = resultlist[0]
			else:
				bResult= False
		else:
			bResult=False    
	except Exception as e:

		bResult= False
	
	return(bResult,strTargetMessage)


if __name__ == '__main__':
	srrTestMessage ="pro Diag (branch.000)\nengin build version (diags_version). Revision revision.\n  Built at build_date_time"
	bResult,strTargetMessage = PraseMessage("./version.txt","{{build_date_time}}",srrTestMessage)
	if(bResult):
		print (strTargetMessage)
	else:
		print ("Error")
#print(strTargetMessage)