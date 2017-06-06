
# coding: utf-8

# In[7]:

import re
from collections import OrderedDict
import time
starttime=time.clock()
sum = 0
overlap = OrderedDict() 
fi = open('CCDS.current.txt','rt')
for each_line in fi:
    if each_line.startswith('#'):
        continue
    each_line = each_line.rstrip()#去掉句尾换行符
    line = each_line.split('\t')#按换行符分开
    if line[-2] == '-':
        continue
    line_ex = re.sub("\[|\]"," ",line[-2])#去掉[]
    target_lines = line_ex.split(",")#去掉,
    for target_line in target_lines:
        start = int(target_line.split('-')[0])
        end = int(target_line.split('-')[1])
        coordinate = line[0] + ':'+ target_line
        if coordinate not in overlap.keys():
            overlap[coordinate] = 1   
            sum += end - start
fi.close()
print(sum)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:




# In[ ]:



