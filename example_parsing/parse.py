#! /usr/bin/env python

import sys

# Open the file
try:
    input = open(sys.argv[1], 'r')
    new_file = sys.argv[2]
except:
    print "The input requires two arguments, an input file and an output file"
    sys.exit(2)

# Read in each line of the file
lines = file.readlines(input)

# Create empty dictionaries
energy_dict = {}
smd_dict = {}

# Go through each line.

for i in lines:

# If it's a line that contains 'ENERGY' it's one that we want, so we keep it and put it in a dictionary
    if 'ENERGY:  ' in i:
        energy_raw1 = i.split('\par')[0]
#        print 'energy_raw1', energy_raw1
        energy_raw = energy_raw1.split(' ')
#        print 'energy_raw', energy_raw
        energy_list = filter(None, energy_raw)
#        print 'energy_list', energy_list
        energies = energy_list[2:len(energy_list)-1]
#        print 'energies', energies
        energy_dict[energy_list[1]] = energies

# If it's a line that contains 'SMD' it's one that we want, so we keep it and put it in a different dictionary
    if 'SMD  ' in i:
        smd_raw1 = i.split('\par')[0]
        smd_raw = smd_raw1.split(' ')
        smd_list = filter(None, smd_raw)
        smds = smd_list[2:len(smd_list)-1]
        smd_dict[smd_list[1]] = smds

#print energy_dict.keys()

# Create a new dictionary that combines both the ENERGY and SMD data
data_dict = {}

for s in energy_dict:
    # The SMD data is only every 10 values, so we just need to add that data in with the ENERGY data if it's there
    if s in smd_dict.keys():
        data_dict[s] = energy_dict[s] + smd_dict[s]
    
    # If there isn't any SMD data for that point, just use the ENERGY data    
    else:
        data_dict[s] = energy_dict[s]

print 'done!'



# Open an output file    
output = open(new_file, 'wt')

# Write the header for the file
output.write('key\tv1\tv2\tv3\tv4\tv5\tv6\tv7\tv8\tv9\tv10\tv11\tv12\tv13\ts14\ts15\ts16\ts17\ts18\n')

#for d in data_dict:
#    print 'key', d, 'data', data_dict[d]


# Write out the data to the file
for data in sorted(data_dict):
#    print 'key', data, 'data', energy_dict[data][12]

# If there's only ENERGY data, just write out that
    if len(data_dict[data]) == 13:
        output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (data, data_dict[data][0], data_dict[data][1], data_dict[data][3], data_dict[data][4], data_dict[data][5], data_dict[data][6], data_dict[data][7], data_dict[data][8], data_dict[data][9], data_dict[data][10], data_dict[data][11], data_dict[data][12]))

# If there's ENERGY and SMD data, write out both
    elif len(data_dict[data]) == 18:
        output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (data, data_dict[data][0], data_dict[data][1], data_dict[data][3], data_dict[data][4], data_dict[data][5], data_dict[data][6], data_dict[data][7], data_dict[data][8], data_dict[data][9], data_dict[data][10], data_dict[data][11], data_dict[data][12], data_dict[data][13], data_dict[data][14], data_dict[data][15], data_dict[data][16], data_dict[data][17]))

# In case there's some data in there you didn't expect
    else:
        print 'wrong length', len(data_dict[data])

