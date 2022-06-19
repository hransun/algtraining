import os
import random
# file = os.popen("wc -l dataset2.csv", 'r').read().split()[0]
# print(os.popen("wc -l dataset2.csv", 'r').read())
# line = random.randint(0, int(file))
# with open('dataset2.csv') as f:
#     count  =0
#     for l in f:
#         if count == int(line):
#             print(l)
#             break
#         else:
#             count +=1
output = os.popen("wc -l dataset2.csv").read().split()[0]
print(output)
import random
index = random.randint(0,int(output))
with open('dataset2.csv') as f:
    count =0
    for line in f:
        if count == index:
            print(line)
            break
        else:
            count +=1
            
        
        
