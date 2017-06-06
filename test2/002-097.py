
# coding: utf-8

# In[2]:

from __future__ import division
from collections import OrderedDict
dict = OrderedDict()
name = ""
with open('test.fasta') as f:
    for line in f:
        context = ""
        line=line.strip()
        if line.startswith(">"):
            name = line
            dict[name]=""
        else:context = line
        dict[name]=dict[name]+context
for name in dict:
    print( name,dict[name])
    print ("length=",len(dict[name]))
    print ("N is",round(dict[name].count("N")/len(dict[name]),2))
    print ("G is",round((dict[name].count("G")+dict[name].count("g"))/len(dict[name]),2))
    print ("C is",round((dict[name].count("C") + dict[name].count("c")) / len(dict[name]),2))


# In[ ]:



