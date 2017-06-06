
# coding: utf-8

# In[2]:

#! /usr/bin/env python 
import os
import re
from collections import OrderedDict
import time
starttime=time.clock()
#from operator import itemgetter 
cds=0
dic=OrderedDict() 
os.chdir('.')
file=open('CCDS.current.txt','rt')
for line in file:
    line=line.rstrip()
    if line.startswith('#'):
        continue
    lst=line.split('\t')
    if lst[-2] == '-':
        continue
    sub=re.sub('\[|\]','',lst[-2])
    cdss=sub.split(', ')
    for i in cdss:
        cand=lst[0]+':'+i
        if cand not in dic:
            dic[cand]=1
            start=int(i.split('-')[0])
            end=int(i.split('-')[1])
            cds+=end-start+1
#end-start+1#
print(cds)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



