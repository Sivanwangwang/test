
# coding: utf-8

# In[22]:

from collections import OrderedDict
import time
starttime=time.clock() 
chr_dict = OrderedDict()
temp_chr = ""
with open("J:/hg38.fa/hg38.fa","r") as hg38:
    for line in hg38:
        line = line.strip()
        #print(line)
        if line.startswith(">"):
            temp_chr = line
            print(temp_chr)
            chr_dict[temp_chr] = ""         #染色体号在字典中对应为空的   键值对为染色体号--“”
        else:
            chr_dict[temp_chr] += line      
#把非染色体号的每一行存入字典  键值对为染色体号--序列   在每一遇到下一个>即染色体号时，
#后续的行通通加到temp_chr这个键中，直到出现新的>（出现先的键）
            #print(temp_chr)
for seqname,seq in chr_dict.items():        #seqname为健，seq为值，任何单词都可以用来赋值，打印的时候对应就好了
    #print(seqname)
    #print(seq)
    seqlen = len(seq)
    N = seq.count('N')
    GC =seq.count('G')+seq.count('g')+seq.count('C')+seq.count('c')
    print(seqname,seqlen,'%.3f'%(N/seqlen),"%.2f"%(GC/(seqlen-N)))   #%.3f显示3位小数，%.2f显示2位小数
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



