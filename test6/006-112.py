
# coding: utf-8

# In[8]:
 
"""在python中要么使用一直使用tab健，要么一直使用4个空格"""
 
import re
from sys import argv
from collections import OrderedDict
from collections import Counter
hsaKEGG = OrderedDict()

def keg_clean(argv):
    with open(argv[1]) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('A'):
                mch = re.search('A<b>(.+)</b>',line)
                className = mch.group(1)
                hsaKEGG[className] = OrderedDict()
 
            elif line.startswith('B'):
                if not line == 'B':
                    mch = re.search('B\s+<b>(.+)</b',line)
                    subclass = mch.group(1)
                    hsaKEGG[className][subclass] = OrderedDict()
 
            elif line.startswith('C'):
                mch = re.search('(\d+)\s(.+)',line)
                pathID = str(argv[1])[0:3] +  mch.group(1)
                pathName = re.sub('\s\[.+\]','',mch.group(2))
                #这个替换不太懂，有的C开头的行后面没有[PATH:******]   
                pathway = pathID + '\t' + pathName
                hsaKEGG[className][subclass][pathway] = [[],[]]         #新建一个列表，列表包括两列表元素
 
            elif line.startswith('D'):
                lst = line.split(';')                                   #分号切片
                geneInfo =lst[0].split('\t')                            #'\t'切片  但是这里边的空格不是\t 所以无法切割  特别注意的是空格与'\t’不是一回事
                #print(geneInfo)
                mch = re.search('D\s+(\d+)\s(.+)',geneInfo[0])          #
                #mch = re.search('D\s+(\d+)\s(.+)',lst[0])
                #print(mch) 
                if mch==None:
                    gene = geneInfo[0]
                else:
                    geneID = mch.group(1)
                    gene = mch.group(2)
                hsaKEGG[className][subclass][pathway][0].append(gene)
                hsaKEGG[className][subclass][pathway][1].append(geneID)
    with open(str(argv[1])[0:3]+'00001_cleaned.keg','wt') as fh:
        for ke,val in hsaKEGG.items():
            for subk,subv in val.items():
                for ptwy,genelist in subv.items():
                    genes = ';'.join(genelist[0])
                    geneIDs = ';'.join(genelist[1])             #"""列表变字符串，加上衔接字符"""
                    fh.write('\t'.join([ke,subk,ptwy,str(len(genelist[0])),str(len(genelist[1])),genes,geneIDs]) + '\n')#存在没有情况的项放在最后，因为
    pthwyNum = 0
    allGenes_id = []      #去重的id集
    allGenes_name = []    #去重的基因名集
    allGenes_id_total = [] #不去重的id集
    allGenes_name_total = [] #不去重的基因名合集
    name_id= [] #不去重的基因名和id合集
    with open(str(argv[1])[0:3]+'00001_cleaned.keg') as f:
        for line in f:
            line = line.rstrip()
            lst = line.split('\t')
            if len(lst) > 7:
                #print(lst[2])
                pthwyNum += 1
                genelist_name = lst[-2].split(';')
                allGenes_name = allGenes_name + [gene for gene in genelist_name if gene not in allGenes_name]
                genelist_id = lst[-1].split(';')
                allGenes_id = allGenes_id + [gene for gene in genelist_id if gene not in allGenes_id]       #list添加元素的方法1
                for i in genelist_id:
                    allGenes_id_total.append(i)                                                             #list添加元素的方法2
                for j in genelist_name:
                    allGenes_name_total.append(j)
    for i in list(range(0,len(allGenes_id_total))):     #两个list同一位置两两合并
        name_id.append(str(allGenes_id_total[i])+"\t"+allGenes_name_total[i])
    print ("Number of non-empty patways: %d" %pthwyNum)
    print ("Number of genes_name in all pathways: %d" %len(allGenes_name))
    print ("Number of genes_id in all pathways: %d" %len(allGenes_id))
    with open(str(argv[1])[0:3]+'_summary.txt','wt') as f_sum:
        f_sum.write(str(argv[1])[0:3]+":")
        f_sum.write('\n'+"Number of non-empty patways: %d" %pthwyNum)
        f_sum.write('\n'+"Number of genes_name in all pathways: %d" %len(allGenes_name))
        f_sum.write('\n'+"Number of genes_id in all pathways: %d" %len(allGenes_id))
        for i in allGenes_name:
            f_sum.write('\n'+i)
        for i in allGenes_id:
            f_sum.write('\n'+i)
    with open(str(argv[1])[0:3]+'_counter_id.txt','wt') as f_count_id:
        for i,j in Counter(allGenes_id_total).items():
            f_count_id.write('\t'.join([str(i),str(j)])+'\n')
    with open(str(argv[1])[0:3]+'_counter_name.txt','wt') as f_count_name:
        for i,j in Counter(allGenes_name_total).items():
            f_count_name.write('\t'.join([str(i),str(j)])+'\n')                        #jion只能针对字符，所用使用之前要字符串化
    with open(str(argv[1])[0:3]+'_name_id_total.txt','wt') as f_name_id_total:	
        for i in set(name_id):
            	f_name_id_total.write(i+"\n")	

keg_clean(argv)



