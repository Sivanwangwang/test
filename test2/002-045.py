
# coding: utf-8

# In[1]:

from collections import OrderedDict      #collections模块带有OrderedDict有序字典
  
chr_dict = OrderedDict()                         #定义chr_dict做为有序字典
temp_dict = OrderedDict()                     #定义temp_dict做为有序字典
temp_chr = ""
  
with open("test.fasta","r") as test:           #with打开文件
    for line in test:
        line = line.strip()                               #strip()函数去除每行首位的空字符
        if line.startswith(">"):                       #startswith()函数判断行开头是否是‘>’
            temp_chr = line                           #如果是‘>’，把这行赋值给temp_chr
            chr_dict[temp_chr] = ""               
        else:
            chr_dict[temp_chr] += line
#print(chr_dict)                                         #绕糊涂了，打印出来看看
#OrderedDict([('>chr_1', 'ATCGTCGaaAATGAANccNNttGTAAGGTCTNAAccAAttGggG'), 
#('>chr_2', 'ATCGAATGATCGANNNGccTAAGGTCTNAAAAGG'), ('>chr_3', 'ATCGTCGANNNGTAATggGAAGGTCTNAAAAGG'), 
#('>chr_4', 'ATCGTCaaaGANNAATGANGgggTA')])
for seqName, seq in chr_dict.items():
    seqLen = len(seq)
    seq = seq.upper()                                #将seq序列全部转换成大写
    N = seq.count("N")
    GC = seq.count("G") + seq.count("C")
    print(seqName, seqLen, "%.2f"%(N/seqLen), "%.2f"%(GC/(seqLen-N)))  #定义输出结果保留两位小数


# In[ ]:



