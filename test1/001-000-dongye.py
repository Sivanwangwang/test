
# coding: utf-8

# In[14]:

import re
import os
from collections import OrderedDict
from operator import itemgetter
import time
starttime=time.clock()
exonLength=0
overlapExons=OrderedDict()
with open('exontest.txt','rt') as f:
    for line in f:
        if line.startswith('#'):                  
            continue                             #如果遇到#开头的行，不读取然后继续
        #print(line)
        line = line.strip()                      #去掉右侧的空格，生成新的行
        #print(line)
        lst = line.split('\t')                     #行按照空格进行分割
        #print(lst[-2])
        if lst[-2] == '-':
            continue                             #如果遇到倒数第二列是空的，用‘-’表示，不读取然后继续
        lst[-2] =  re.sub('\[|\]','',lst[-2])     #将提取出的倒数第二列，进行去'[]'处理,re是正则表达式的意思
        #print(lst[-2])
        exons = lst[-2].split(',')                #按,将每个基因的exon分开
        print(exons)
        for exon in exons:
            start = int(exon.split('-')[0])       #提取每个外显子的首与末尾
            #print(exon.split('-')[0])
            end = int(exon.split('-')[1])
            coordinate=lst[0]+':'+exon
            if coordinate not in overlapExons.keys():
                overlapExons[coordinate]=1
                exonLength += end -start              #将所有的外显子的首尾位置相减之后再加起来
            
print(exonLength)
endtime=time.clock()
print(endtime - starttime)


# In[ ]:



