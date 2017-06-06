
# coding: utf-8

# In[3]:

from collections import OrderedDict
from operator import itemgetter
seq=OrderedDict()
with open ('test.fasta') as f:
    for line in f:
        line=line.rstrip()
        if line.startswith('>'):
            seqName=line[1:]
            seq[seqName]=''
        else:
            seq[seqName]+=line.upper()
for key,value in seq.items():
    seqlength=len(value)
    Nnumber=value.count('N')
    GCnumber=value.count('G')+value.count('C')
    GCcontent=float(GCnumber/seqlength)*100
    print(key,'\t',seqlength,'\t',Nnumber,'\t',GCcontent)


# In[ ]:




# In[ ]:



