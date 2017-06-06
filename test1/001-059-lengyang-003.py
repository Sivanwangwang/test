
# coding: utf-8

# In[1]:


import re
f=open('CCDS.current.txt','rt')
sum=0
lt=[]
dic={}
for line in f:
    line=line.rstrip()#去掉每一行最后的换行符
    if line.startswith('#'):
        continue
    lst=line.split('\t')#以空格将
    if lst[-2]=='-':
        continue
    exons=re.sub("\[|\]"," ",lst[-2])#去除中括号
    exons=exons.split(',')
    for exon in exons:
        lt.append(exon)
st=set(lt)
for i in st:
    exon_one=i.split('-')
    exon_start = exon_one[0]
    exon_end = exon_one[1]
    sum += int(exon_end) - int(exon_start)
print(sum)


# In[ ]:



