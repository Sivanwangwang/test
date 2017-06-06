
# coding: utf-8

# In[2]:

import time
starttime=time.clock()
f = open('CCDS.current.txt','r')
f_lines = f.readlines()[1:]
 
cds_length = 0
position = []
 
for line in f_lines:
    line = line.strip('\n').split('\t')
    cds_locations = line[9]
    if cds_locations != ('-'):
        cds_locations = cds_locations.strip("'").strip('[').strip(']').split(', ')
        for cds_location in cds_locations:
            if cds_location not in position:
                position.append(cds_location)
                cds_location = cds_location.split('-')
                cds_length += (int(cds_location[1])-int(cds_location[0])+1)
print(cds_length)
endtime=time.clock()
print(endtime - starttime)
                               


# In[ ]:



