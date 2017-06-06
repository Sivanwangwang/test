
# coding: utf-8

# In[1]:

import re 
import time
starttime=time.clock()
f1=open("CCDS.current.txt") 
exonlenghth=0
line=f1.readlines()
for i in line:
    if i.startswith("#"):
        continue
    i=i.rstrip()
    filt=re.split(r'\t',i)
    if filt[-2]=="-":
        continue
    z=re.sub("\[|\]"," ",filt[-2])
    exons=z.split(",")
    for exon in exons:
        start=int(exon.split("-")[0])
        end=int(exon.split("-")[1])
        exonlenghth+=end-start
print (exonlenghth)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



