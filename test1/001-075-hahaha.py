
# coding: utf-8

# In[9]:

import pandas
import re
import time
starttime=time.clock()
table=pandas.read_table("CCDS.current.txt")
string="".join(table.values[:,-2])
l=re.findall("\d+-\d+",string)
num=-sum([eval(i) for i in set(l)])
print(num)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



