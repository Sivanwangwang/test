
# coding: utf-8

# In[1]:


import re
f=open('CCDS.current.txt','r')
g=open('NCCDS.txt','w')
sum=0
dit={}
for line in f:
    if line.startswith('#'):
        continue
    line=line.rstrip()
    exons=re.findall('[0-9]+-[0-9]+',line)
    for exon in exons:
        exon_one=exon.split('-')
        exon_start=exon_one[0]
        exon_end=exon_one[1]
        if exon not in dit.keys():
            dit[exon]=1
        sum+=int(exon_end)-int(exon_start)
print(sum)


# In[ ]:



