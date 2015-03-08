import os
import re
from collections import OrderedDict
wordcount={}


for path,dirs,files in os.walk('wc_input/'):
    for file in files:
        file = open(path+file,'r+')
        for word in file.read().lower().split():
            #remove extra symbols
            word = re.sub('[^a-zA-Z]+', ' ', word).strip()
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        file.close()
    # soring dictionary
    ow = OrderedDict(sorted(wordcount.items(), key = lambda t: t[0]))

# output
# remove old output
try:
    os.remove('wc_output/wc_result.txt')
except OSError:
    pass

for (key, value) in ow.iteritems():
    with open('wc_output/wc_result.txt', 'a') as f:
        print ('%s %s' % (key, value))
        f.write(key + ' ')
        f.write(str(value) + '\n')