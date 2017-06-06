
# coding: utf-8

# In[4]:

import re
from collections import OrderedDict
import time
starttime=time.clock() 
exonlenghth = 0
overlapexons = OrderedDict()
with open("CCDS.current.txt") as f:
     line = f.readlines()
for i in line:
    if i.startswith("#"):
        continue
    i = i.rstrip()
    filt = re.split(r'\t', i)
    if filt[-2] == "-":
        continue
    z = re.sub("\[|\]", " ", filt[-2])
    exons = z.split(",")
    for exon in exons:
        start = int(exon.split("-")[0])
        end = int(exon.split("-")[1])
        coordinate = filt[0]+':'+exon
        if coordinate not in overlapexons.keys():
            overlapexons[coordinate] = 1
            exonlenghth += end - start
print (exonlenghth)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



