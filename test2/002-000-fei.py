
# coding: utf-8

# In[ ]:

# !/usr/bin/env python3
#
# Usage example:
#     count_atgc.py tmp.fasta
# 
# Then, you can open the file "atgc_count.txt"
 
import sys
args = sys.argv
 
from collections import OrderedDict
 
chr_dict = OrderedDict()
temp_chr = '' 
 
with open(args[1], 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            temp_chr = line
            chr_dict[temp_chr] = ''
        else:
            chr_dict[temp_chr] += line
with open('atgc_count.txt', 'at') as outcome:
    print('seqID\tseqLength\tcount_A\tcount_T\tGC_content', file=outcome)
    for seqName, seq in chr_dict.items():
        seqLen = len(seq)
        seqID = seqName[1:]
        A = seq.count('A') + seq.count('a')
        T = seq.count('T') + seq.count('t')
        G = seq.count('G') + seq.count('g')
        C = seq.count('C') + seq.count('c')
        N = seq.count('N')
        GC = seq.count('G') + seq.count('g') + seq.count('C') + seq.count('c')
        print('{0}\t{1}\t{2}\t{3}\t{4}'.format(seqID, seqLen, A, T, '%.3f'%(GC/(seqLen-N))), file=outcome)


# In[ ]:



