import os
# print(os.popen("tail -2 dataset2.csv", 'r').read())
x = os.popen("tail -2 dataset2.csv", 'r').read()
print(x)
