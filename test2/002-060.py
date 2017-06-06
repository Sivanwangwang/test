
# coding: utf-8

# In[10]:

import collections
import os
filepath = 'J:/chromFa/'
fileDict = []
filenames = os.listdir(filepath)
 
for f in filenames:
    if f.startswith('.'): #remove hidden files
        pass
    else:
        fileDict.append(f)
 
chr_dict = collections.OrderedDict()
bases = ['A','T','C','G','N','a','t','c','g','n']
 
for f in fileDict:
    f = open(filepath+f,'r')
    for line in f:
        line = line.strip('\n')
        if line.startswith('>'):
            temp = line[1:]
            chr_dict[temp] = {}
            for base in bases:
                chr_dict[temp][base] = 0
        else:
            for base in bases:
                chr_dict[temp][base] += line.count(base)
                 
for chr_name, atcgn in chr_dict.items():
    length = sum(atcgn.values())
    N = round((atcgn['N']+atcgn['n'])/length,2)
    GC = round((atcgn['G']+atcgn['C']+atcgn['g']+atcgn['c'])/length,2)
    AT= round((atcgn['A']+atcgn['T']+atcgn['a']+atcgn['c'])/length,2)
    print(chr_name, length)
    print('N: '+ str(N))
    print('GC: '+ str(GC))
    print('AT: '+ str(AT))
    print('')
     
f.close()


# In[ ]:



