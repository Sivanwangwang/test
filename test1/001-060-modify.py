
# coding: utf-8

# In[2]:

import re
import time
starttime=time.clock()
f_raw = open('CCDS.current.txt','r')
f_raw_lines = f_raw.readlines()[1:] 
cds_length = 0
position = [] 
for line in f_raw_lines:
    line = line.strip('\n').split('\t')
    cds_locations = line[9]
    if cds_locations != ('-'):
        cds_locations = re.sub('\[|\]','',cds_locations).split(', ')
        for cds_location in cds_locations:
            position.append(cds_location)             
position = list(set(position))
for cds_location in position:
    cds_location = cds_location.split('-')
    cds_length += (int(cds_location[1])-int(cds_location[0])+1) 
print (cds_length)
endtime=time.clock()
print(endtime - starttime)
f_raw.close()
                               


# In[ ]:



