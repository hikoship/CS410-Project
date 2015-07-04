# preprocess
fpre = open('GDS2771_full.soft')
fpost = open('postdata.txt', 'w')

lineNum = 0
for line in fpre:
    lineNum += 1
    if lineNum <= 261:
        continue # eliminate irrelevant discription
    feature = line.split()
    for j in range(2, 194): # eliminate labels
        fpost.write('%s\t' % feature[j])

    fpost.write('\n')



fpre.close()
fpost.close()
