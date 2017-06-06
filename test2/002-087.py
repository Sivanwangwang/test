
# coding: utf-8

# In[6]:

#from __future__ import division
sequences={}
head=""
with open ("test.fasta",'r') as f:
    for line in f:
        if line.startswith('>'):
            head=line.strip()
            sequences[head] =""
        else:
            sequences[head] += line.strip()
#print (sequences)

for i in sequences:
    #print str(i)+" "+ 'N content:',sequences[i].count('N')/len(sequences[i])
    print (str(i)+" "+ 'GC content:',"%.2f"%((sequences[i].count('G')+sequences[i].count('C'))/len(sequences[i])*100))


# In[ ]:



