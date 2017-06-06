
# coding: utf-8

# In[18]:

import re
import os
import time
starttime=time.clock()
exonlength=0
list=[]
with open('CCDS.current.txt','rt') as f:
    for line in f:
        if line.startswith('#'):                  
            continue                             
        exons=re.findall('[0-9]+-[0-9]+',line)#匹配像00000-00000这种格式的数据
        for exon in exons:
            list.append(exon)#将每一个外显子存入list中
exons=set(list)#去重
for i in st:
    start = i.split('-')[0]
    end = i.split('-')[1]
    exonlength+=int(end)-int(start)            
print(exonlength)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:




# In[ ]:



