GROUP_NUM_1 = 90
GROUP_NUM_2 = 97
GROUP_NUM_3 = 5
label_1 = 1
label_2 = 2
label_3 = 3
filenum = 191
print filenum
filename ='/Users/gaohongyuan/Documents/MATLAB/index%d.txt' % filenum

f = open(filename)

def test(f, label, groupNum):
    trueNum = 0
    for i in range(groupNum):
        l = f.readline()
        if float(l) == label:
            trueNum += 1
    print '%d/%d %f' % (trueNum, groupNum, float(trueNum) / groupNum)

test(f, label_1, GROUP_NUM_1)
test(f, label_2, GROUP_NUM_2)
test(f, label_3, GROUP_NUM_3)

f.close()

f = open(filename)
total=[0,0,0]
num=[0,0,0]
i = 1
for line in f:
    line = float(line)
    total[int(line) - 1] += 1
    if i<=90 and line ==label_1: num[label_1-1] += 1
    if i>90 and i<=187 and line ==label_2: num[label_2-1] += 1
    if i>187 and line ==label_3: num[label_3-1] += 1

    i+=1

for i in range(3):
    print '%d/%d %f' % (num[i], total[i], float(num[i]) / total[i])
print sum(num), sum(num)/192.0
