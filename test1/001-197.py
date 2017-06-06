
# coding: utf-8

# In[3]:

import pandas as pd
import re
import time
starttime=time.clock() 
#数据录入
data = pd.read_table("CCDS.current.txt",usecols = [0,9])
data = data[data.values[:,1] !="-"]#去除“-”
string="".join(data.values[:,1])#链接cds区域的数据
l=re.findall("\d+-\d+",string)#进行正则判断选择符合条件的组合
num=-sum([eval(i) for i in set(l)])#去重复后，转换后求和。
print(num)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



