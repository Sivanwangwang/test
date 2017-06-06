
# coding: utf-8

# In[1]:

#!/usr/bin/env python

from __future__ import division
from collections import defaultdict
percent=defaultdict(dict)
 
with open ('test.fasta','rt') as f:
    for line in f:
        line=line.rstrip()
        if line.startswith('>'):
            id=line.strip('>')
            percent[id]['len']=0
            percent[id]['gc']=0
            percent[id]['n']=0
        else:
            percent[id]['len']+=len(line)
            percent[id]['gc']+=line.count("G")
            percent[id]['gc']+=line.count("g")
            percent[id]['gc']+=line.count("C")
            percent[id]['gc']+=line.count("c")
            percent[id]['n']+=line.count("N")
            percent[id]['n']+=line.count("n")
for m in percent:
    gc=percent[m]['gc']/percent[m]['len']
    n=percent[m]['n']/percent[m]['len']
    print ('%s\t%d\t%.4f\t%.4f'%(m,percent[m]['len'],gc,n))


# In[ ]:



