
# coding: utf-8

# In[5]:

import re
import time
starttime=time.clock()
sum = 0
lists = []
with open('CCDS.current.txt','rt') as  f :
    for line in f :
        if line.startswith("#"):
            continue
        line = line.rstrip()
        exons = re.findall("\d+-\d+",line)
        for exon in exons:
            lists.append(exon)
    exons_set = set(lists)
    for exon_set in exons_set:
        lst = exon_set.split('-')
        exon_start = lst[0]
        exon_end = lst[1]
        sum += int(exon_end)-int(exon_start)
print(sum)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



