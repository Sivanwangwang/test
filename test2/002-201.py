
# coding: utf-8

# In[1]:

from collections import OrderedDict
 
chr_dict = OrderedDict()
temp_chr = ""
 
with open("test.fasta","rt") as f:
        for line in f:
                line = line.strip()
                if line.startswith(">"):
                        for seqName,seq in chr_dict.items():
                                A = seq.count("A") + seq.count("a")
                                T = seq.count("T") + seq.count("t")
                                C = seq.count("C") + seq.count("c")
                                G = seq.count("G") + seq.count("g")
                                N = seq.count("N") + seq.count("n")
                                print(seqName,A,T,C,G,N)
                        temp_chr = line
                        chr_dict = OrderedDict()
                        chr_dict[temp_chr] = ""
                else:
                        chr_dict[temp_chr] += line
 
for seqName,seq in chr_dict.items():
        A = seq.count("A") + seq.count("a")
        T = seq.count("T") + seq.count("t")
        C = seq.count("C") + seq.count("c")
        G = seq.count("G") + seq.count("g")
        N = seq.count("N") + seq.count("n")
        print(seqName,A,T,C,G,N)


# In[ ]:



