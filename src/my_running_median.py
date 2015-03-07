import os
myList = []

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    if len(lst) %2 == 0:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

for path,dirs,files in sorted(os.walk('wc_input/')):
    for file in files:
    	file = open(path + file,'r+')
    	for line in file.read().splitlines():
       		linelength = len(line.split())
       		myList.append(linelength)
       		print float(median(myList))
