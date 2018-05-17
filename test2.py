import re
strOne="{{program}} Diag ({{branch}})\n\
{{build_engine}} build {{build_version}} ({{diags_version}}). Revision {{revision}}.\n\
Built at {{build_date_time}}"
strTwo=re.sub("\(","\(",strOne)#左括号加转义
strThree=re.sub("\)","\)",strTwo)#有括号加转义
strFour=re.sub("\.","\.",strThree)# . 加转义
a='{{branch}}'
rexOne=re.sub("(%s)"%(a),'(.*)',strFour)#把要去的key换成(.*)括号取出来里面的内容
rexTwo=re.sub("{{.*?}}",".*",rexOne)#把格式里面没有到的key全部换成 .* 构成正则表达式
text="test Diag (this is the anser)\nwho build Ver 0.0.1 (dia 0.0.2). Revision Ver3.9.1.\nBuilt at 20180909"
info=(re.findall(rexTwo,text))[0]#re.findall取出来的是list，将第0项取出来就是要的数据的str
print(info)