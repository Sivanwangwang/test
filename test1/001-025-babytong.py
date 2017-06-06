
# coding: utf-8

# In[ ]:

import re
sum=0
list_all=[]
 
with open ('H:/tmp/Python/exontest.txt') as f:
    for line in f:
        if line.startswith('#'):
            continue
        lists=line.rstrip().split('\t')
        exons=re.findall('[0-9]+-[0-9]+',lists[-2])
        [list_all.append(exon) for exon in exons if not exon in list_all]  
    for i in list_all:
        exon_one=i.split('-')
        sum+=int(exon_one[1])-int(exon_one[0])
    print(sum)


# In[ ]:



