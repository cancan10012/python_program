import re

def PraseMessage(strFilePath,strKeyName,strMessage):
  #Create the Return Value
  strTargetMessage = "{} {} ParseFail {}".format(strFilePath,strKeyName,strMessage)
  bResult = True
  try:
    #Get File Context
    fileObj = open(strFilePath)
    strVer =  fileObj.read()
    fileObj.close()
  
    #Split Context of File and Message in same way
    strlistRex =  re.split("\s",strVer)
    strlistMessage = re.split("\s",strMessage)
    
    #Get the Context and Message Match the Key position
    strRexTarget = ""
    index = 0
    for strRex in strlistRex:
      if len(re.findall(strKeyName,strRex))>0:
        strRexTarget = strRex
        break
      index+=1
    strMessageInIndex = strlistMessage[index]

    #Create a new Rex to Get the Target Message Auto
    liststrReplaceChart = ["\(","\)","\."]
    for strReplaceChart in liststrReplaceChart:
      strRexTarget =  re.sub(strReplaceChart,strReplaceChart,strRexTarget)
    strStepTwo = re.sub("{{.*}}",".+",strRexTarget)
    
    #Get the Target Message with the new Rex
    resultlist =  re.findall(strStepTwo,strMessageInIndex)
    print("strMessageInIndex:"+strMessageInIndex)
    #print("strStepTwo:"+strStepTwo)
    print(resultlist)
  
    if len(resultlist)==1:
      strTargetMessage = resultlist[0]
    else:
      bResult= False

  except Exception as e:
    #do not raise Error ,but return error info !!
    bResult= False
  
  return bResult,strTargetMessage


if __name__ == '__main__':
  srrTestMessage ="pro Diag (branch.000)\nengin build version (diags_version). Revision revision.\n\tBuilt at build_date_time"
  bResult,strTargetMessage = PraseMessage("./version.txt","{{program}}",srrTestMessage)
  if(bResult):
    print (strTargetMessage)
  else:
    print ("Error")