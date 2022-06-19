import math
d1 , d2 = {}, {}
with open('dataset2.csv') as f:
    f.readline()
    for line in f:
        name,stride,stance = line.rstrip().split(',')
        if stance !='bipedal':
            continue
        d2[name] = float(stride)

with open('dataset1.csv') as f:
    f.readline()
    for line in f:
        name,leg,_ = line.rstrip().split(',')
        if name not in d2:
            continue
        d1[name] = float(leg)

result = []
g = 9.8
for name in d1:
    if name not in d2:
        continue
    stride = d1[name]
    leg = d2[name]
    speed = ((stride / leg) - 1) * math.sqrt(leg * g)
    result.append((speed,name))

result.sort(key=lambda x:x[0],reverse=True)
for i in result:
    print(i[1])
        
    