
# coding: utf-8

# In[2]:

from collections import OrderedDict
import time
sum_atcg = OrderedDict()
bases = ["A","T","C","G","N"]
sum_all = 0
start =time.clock()
with open('test.fasta','r') as f:
    for line in f:
        if line.startswith('>'):
            chr_id = line[1:]
            sum_atcg[chr_id] = {}
            for base in bases:
                sum_atcg[chr_id][base] = 0
        else:
            line = line.upper().strip()
            sum_all += len(line)   #加了一个计算了全部长度
            for base in bases:
                sum_atcg[chr_id][base] += line.count(base)
    for chr_id ,atcg_count in sum_atcg.items():
        sum_chr = sum(atcg_count.values())
        GC =round( ( atcg_count['G'] + atcg_count["C"])*1.0/sum_chr,2) 
        #不加1.0发现计算结果等于0？还好在视频里学到了，要不然自己遇到要百度很久
        print (GC)
        print (chr_id)
        for base in bases:
            print('%s : %s'%(base,atcg_count[base]))
        print ('SUM_chr : %s'%sum_chr)
        print ('GC: %s'%GC)
    print ('sum_all:%s'%sum_all)
end = time.clock()
print ('used %s s'% (end-start))


# In[ ]:



