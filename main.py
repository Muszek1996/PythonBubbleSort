import sys
import json
from pprint import pprint

dataFile = open(sys.argv[1])
jsonfile = json.load(dataFile)
dataFile.close()
print "Przed posortowaniem:"
nonSorted = jsonfile['input_list']
print nonSorted
sorted = nonSorted
for i in xrange(len(sorted)):
    for j in xrange(len(sorted) - 1):
     if sorted[j]> sorted[j + 1]:
         sorted[j], sorted[j + 1]= sorted[j + 1], sorted[j]
print sorted
saveFile = open("sorted.json",'w')
json.dump(sorted,saveFile)