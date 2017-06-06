
# coding: utf-8

# In[1]:

#!/usr/bin/env python

import sys
chr_name = ''
a = 0
t = 0
c = 0
g = 0
n = 0
gc = 0
length = 0
flag = False
 
with open('ATCGN_count.txt', 'w') as f_save:
    print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format('chr_name', 'A', 'T', 'C', 'G', 'N','GC_percent'), file = f_save)
    with open(sys.argv[1], 'r') as f_genome:
        for line in f_genome:
            line = line.strip()
            if line.startswith('>'):
                if flag:
                    print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(chr_name, a, t, c, g, n, round(gc/length,4)), file = f_save)
                    chr_name = ''
                    a = 0
                    t = 0
                    c = 0
                    g = 0
                    n = 0
                    gc = 0
                    length = 0
                chr_name = line[1:]
            else:
                flag = True
                line = line.upper()
                a += line.count('A')
                t += line.count('T')
                c += line.count('C')
                g += line.count('G')
                n += line.count('N')
                gc += g + c
                length += len(line)
        if flag:
            print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(chr_name, a, t, c, g, n, round(gc/length,4)), file = f_save)


# In[ ]:



