
# coding: utf-8

# In[2]:

#! usr/bin/env python
 
import re
import time
starttime=time.clock()
exonlength = 0
with open('CCDS.current.txt') as f:
    for line in f:
        if line.startswith('#'):
            continue
        line = line.rstrip()
        line = line.split('\t')
        exons = line[-2]
        if exons == '-':
            continue
        exons = re.sub('\[|\]','',exons)
        exons = exons.split(',')
        for exon in exons:
            exon = exon.split('-')
            start = int(exon[0])
            end = int(exon[1])
            exonlength += end-start
print(exonlength)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



