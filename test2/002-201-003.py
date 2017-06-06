
# coding: utf-8

# In[1]:

import sys
import time 
import re
 
start = time.clock()
 
args = sys.argv
 
sum_atcg = {}
 
bases = ["A", "T", "C", "G", "N"]
 
def get_chr(buffer):
        (buffer,tmp) = buffer.split(">",1)
        if ">" not in tmp:
                return (buffer, tmp)
        else:
                get_chr(tmp)
                return (buffer, get_chr(tmp))
def get_list(tmp):
        tmp_list = []
        while len(tmp) > 1 and type(tmp) == tuple:
                tmp_list.append(tmp[0])
                tmp = tmp[1]
        tmp_list.append(tmp)
        return tmp_list
with open(args[1], "r") as Fin:
        tmp = Fin.readline()
        chr_id = re.split(r"\s", tmp)[0][1:]
        sum_atcg[chr_id] = {}
        for base in bases:
                sum_atcg[chr_id][base] = 0
        while 1:
                buffer = Fin.read(1024 * 1024)
                if not buffer:
                        break
 
                if ">" in buffer:
                        #print(get_chr(buffer))
                        (buffer ,tmps) = get_chr(buffer)
                        #print(tmps,len(tmps))
                        if len(tmps) > 1:
                                tmps = get_list(tmps)
                        #print(tmps)
                        buffer = buffer.upper()
                        for base in bases:
                                sum_atcg[chr_id][base] += buffer.count(base)
                        for tmp in tmps:
                                (tmp, buffer) = tmp.split("\n", 1)
                                chr_id = re.split(r"\s", tmp)[0]
                                sum_atcg[chr_id] = {}
                                for base in bases:
                                        sum_atcg[chr_id][base] = 0
                                buffer = buffer.upper()
                                for base in bases:
                                        sum_atcg[chr_id][base] += buffer.count(base)
                else:
                        buffer = buffer.upper()
                        for base in bases:
                                sum_atcg[chr_id][base] += buffer.count(base)
for chr_id, atcg_count in sum_atcg.items():
        GC = atcg_count["G"] + atcg_count["C"]
        SUM = sum(atcg_count.values())
        print(chr_id)
        for base in bases:
                print("%s: %s" % (base, atcg_count[base]))
        print("SUM:  %s" % (SUM))
        print("GC: %s" % (GC/SUM))
        print("N: %s" % (atcg_count["N"]/SUM))
end = time.clock()
print("used %s s" % str(end - start))


# In[ ]:



